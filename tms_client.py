import os
import base64
import requests
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, Any, Union, List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()



# TMS Row Type Constants
class RowTypes:
    """Constants for TMS row types used in various API endpoints."""
    ORDER = "O"           # Order
    MOVEMENT = "M"        # Movement
    SETTLEMENT = "M"      # Settlement (same as Movement)
    CUSTOMER = "C"        # Customer
    LOCATION = "L"        # Location
    PAYEE = "P"          # Payee
    DRIVER = "D"         # Driver
    TRACTOR = "T"        # Tractor
    TRAILER = "E"        # Trailer
    USER = "U"           # User


class TMSClient:
    """
    A client for interacting with the McLeod TMS API.
    
    This client supports both HTTP Basic Authentication (username/password) and API key authentication.
    Maintains a stateful session for making API calls.
    
    Examples:
        Basic usage with username/password:
        >>> with TMSClient("username", "password") as client:
        ...     locations = client.get_json("/locations/new")
        ...     orders = client.get_json("/orders", params={'status': 'active'})
        
        API key authentication:
        >>> with TMSClient(api_key="your-api-key") as client:
        ...     orders = client.get_json("/orders")
        
        API key with custom header format:
        >>> with TMSClient(api_key="your-api-key", api_key_header="ApiKey") as client:
        ...     orders = client.get_json("/orders")
        
        Company switching:
        >>> client.get_json("/orders", company_id="TMS2")
        
        Raw response access:
        >>> response = client.get("/locations/123")
        >>> print(response.status_code)
        >>> data = response.json()
        
        Custom headers and timeouts:
        >>> client.get("/orders", timeout=30, headers={'Custom': 'value'})
        
        POST with JSON data:
        >>> order_data = {"customer": "ACME", "status": "new"}
        >>> result = client.post_json("/orders", data=order_data)
    """
    
    def __init__(self, username: Optional[str] = None, password: Optional[str] = None, 
                 base_url: Optional[str] = None, api_key: Optional[str] = None,
                 api_key_header: str = "Bearer"):
        """
        Initialize the TMS client.
        
        Args:
            username: Username for authentication (required if api_key not provided)
            password: Password for authentication (required if api_key not provided)
            base_url: Base URL for the TMS API (defaults to env var TMS_BASE_URL)
            api_key: API key for authentication (alternative to username/password)
            api_key_header: Header format for API key. Options:
                - "Bearer" (default): Authorization: Bearer <api_key>
                - "ApiKey": Authorization: ApiKey <api_key>
                - "X-API-Key": Custom header X-API-Key: <api_key>
        """
        # Check for API key in environment ONLY if not explicitly provided as parameter
        # This ensures backwards compatibility - explicit parameters take precedence
        api_key_was_provided = api_key is not None
        if api_key is None:
            api_key = os.getenv('TMS_API_KEY')
        
        # Check for username/password in environment ONLY if not explicitly provided as parameters
        # This ensures backwards compatibility - explicit parameters take precedence
        # BUT: if api_key exists (from param or env), don't load username/password from env
        # to avoid conflicts
        if not api_key:
            # Only check env for username/password if api_key doesn't exist
            if username is None:
                username = os.getenv('TMS_USERNAME')
            if password is None:
                password = os.getenv('TMS_PASSWORD')
        
        # Validate authentication method - ensure only one method is used
        if api_key and (username or password):
            raise ValueError("Cannot use both api_key and username/password. Use either api_key OR username/password.")
        
        if api_key:
            self.api_key = api_key
            self.api_key_header = api_key_header
            self.username = None
            self.password = None
            self.basic_auth = None
            auth_method = "API Key"
        elif username and password:
            self.username = username
            self.password = password
            self.api_key = None
            self.api_key_header = None
            # Create base64 encoded basic auth header
            credentials = f"{username}:{password}"
            self.basic_auth = base64.b64encode(credentials.encode()).decode()
            auth_method = "Basic Auth"
        else:
            raise ValueError(
                "Authentication required. Provide either:\n"
                "1. username and password: TMSClient(username='user', password='pass')\n"
                "2. api_key: TMSClient(api_key='your-api-key')\n"
                "3. Environment variables: TMS_USERNAME/TMS_PASSWORD or TMS_API_KEY"
            )
        
        self.base_url = base_url or os.getenv('TMS_BASE_URL')
        
        if not self.base_url:
            raise ValueError(
                "TMS_BASE_URL must be provided. Options:\n"
                "1. Pass as parameter: TMSClient(..., base_url='https://your-domain.com')\n"
                "2. Set environment variable: TMS_BASE_URL=https://your-domain.com\n"
                "3. Create .env file with: TMS_BASE_URL=https://your-domain.com"
            )
            
        # Remove trailing slash if present
        self.base_url = self.base_url.rstrip('/')
        
        # Initialize session
        self.session = requests.Session()
        
        # Cache for doctypes to avoid repeated API calls
        self._doctype_cache: Dict[str, Dict[str, Any]] = {}
        
        # Cache for charge codes (in memory)
        self._charge_codes_cache: Dict[str, Dict[str, Any]] = {}
        
        # Set default headers with appropriate authentication
        headers = {
            'User-Agent': 'TMS-Python-Client/1.0',
            'Accept': 'application/json',
            'X-com.mcleodsoftware.CompanyID': os.getenv('TMS_COMPANY_ID', 'TMS')
        }
        
        if api_key:
            if api_key_header == "X-API-Key":
                headers['X-API-Key'] = api_key
            else:
                headers['Authorization'] = f'{api_key_header} {api_key}'
        else:
            headers['Authorization'] = f'Basic {self.basic_auth}'
        
        self.session.headers.update(headers)
        
        auth_user = username if username else "API Key"
        print(f"TMS Client initialized with {auth_method} for user: {auth_user}")
    
    def _make_request(self, method: str, endpoint: str, company_id: Optional[str] = None, **kwargs) -> requests.Response:
        """
        Make an authenticated request to the TMS API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            endpoint: API endpoint (without base URL)
            company_id: Override Company ID for this request (optional)
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        # Handle per-request company ID override
        if company_id:
            # Create headers with overridden company ID
            headers = kwargs.get('headers', {})
            headers['X-com.mcleodsoftware.CompanyID'] = company_id
            kwargs['headers'] = headers
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                raise Exception(f"Authentication failed (401): Invalid username or password")
            elif response.status_code == 403:
                raise Exception(f"Access denied (403): Insufficient permissions for this resource")
            elif response.status_code == 415:
                # Include response body for 415 errors to debug content type issues
                try:
                    error_details = response.text
                    raise Exception(f"HTTP 415 Unsupported Media Type: {error_details}")
                except:
                    raise Exception(f"HTTP 415 Unsupported Media Type: {e}")
            else:
                raise Exception(f"HTTP {response.status_code}: {e}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
    
    def get(self, endpoint: str, company_id: Optional[str] = None, **kwargs) -> requests.Response:
        """Make a GET request to the API."""
        return self._make_request('GET', endpoint, company_id=company_id, **kwargs)
    
    def post(self, endpoint: str, company_id: Optional[str] = None, **kwargs) -> requests.Response:
        """Make a POST request to the API."""
        return self._make_request('POST', endpoint, company_id=company_id, **kwargs)
    
    def put(self, endpoint: str, company_id: Optional[str] = None, **kwargs) -> requests.Response:
        """Make a PUT request to the API."""
        return self._make_request('PUT', endpoint, company_id=company_id, **kwargs)
    
    def delete(self, endpoint: str, company_id: Optional[str] = None, **kwargs) -> requests.Response:
        """Make a DELETE request to the API."""
        return self._make_request('DELETE', endpoint, company_id=company_id, **kwargs)
    
    def get_json(self, endpoint: str, company_id: Optional[str] = None, **kwargs) -> Dict[Any, Any]:
        """
        Make a GET request and return JSON response.
        
        Args:
            endpoint: API endpoint
            company_id: Override Company ID for this request (optional)
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response
        """
        response = self.get(endpoint, company_id=company_id, **kwargs)
        return response.json()
    
    def get_load_json(self, order_id: Union[str, int], company_id: Optional[str] = None) -> Dict[Any, Any]:
        """
        Retrieve the full JSON for a load (order).
        
        Args:
            order_id: The order/load ID to retrieve
            company_id: Optional override for `X-com.mcleodsoftware.CompanyID`
        
        Returns:
            Parsed JSON for the specified order
        """
        order_id_str = str(order_id)
        return self.get_json(f"/orders/{order_id_str}", company_id=company_id)

    def search_customers(self, query: str, company_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Search for customers by name or ID.
        
        Args:
            query: String to search for customers by name or ID
            company_id: Optional override for `X-com.mcleodsoftware.CompanyID`
        
        Returns:
            List of RowCustomer objects matching the search query
            
        Examples:
            >>> customers = client.search_customers("ACME")
            >>> customers = client.search_customers("12345")  # search by ID
        """
        params = {"q": query} if query else {}
        results = self.get_json("/customers", company_id=company_id, params=params)
        return results if isinstance(results, list) else []

    def search_users(self, query: str, company_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Search for users by ID, name, or email address using the McLeod API.
        
        This method queries the GET /users endpoint and returns a list of RowUser objects
        that match the search criteria. The search parameter supports partial matching,
        so you can search by full user ID, partial ID, name, or email address.
        
        Args:
            query: String to search for users. Can be:
                - Full user ID (e.g., "cfaa-jthom")
                - Partial user ID (e.g., "cfaa" matches all users starting with "cfaa")
                - Name (e.g., "Jack Thompson" or "Jack")
                - Email address (e.g., "jthompson@teamcheema.com")
                - Empty string ("") to get all users (may not be supported by all API versions)
            company_id: Optional override for `X-com.mcleodsoftware.CompanyID` header.
                Defaults to the company ID set during client initialization or TMS_COMPANY_ID env var.
        
        Returns:
            List of RowUser dictionaries matching the search query. Each user object contains:
            
            **Common Fields:**
            - ``id`` (str): Unique user ID (e.g., "cfaa-jthom")
            - ``name`` (str): Full name of the user (e.g., "Jack Thompson")
            - ``email_address`` (str): User's email address
            - ``phone`` (str): User's phone number
            - ``is_active`` (bool): Whether the user account is active
            - ``company_id`` (str): Company the user belongs to (e.g., "TMS")
            - ``active_date`` (str): Date when user was activated (format: YYYYMMDDHHMMSS±ZZZZ)
            - ``login_id`` (str): Login identifier
            - ``windows_login`` (str): Windows login name
            
            **Additional Fields (varies by user):**
            - ``agent`` (bool): Whether user is an agent
            - ``available`` (bool): Whether user is currently available
            - ``department_id`` (str): Department identifier (e.g., "LOGS")
            - ``extension`` (str): Phone extension
            - ``date_format`` (str): User's preferred date format
            - ``time_format`` (str): User's preferred time format
            - ``enable_alerts`` (bool): Whether alerts are enabled
            - ``confirm_record`` (bool): Whether record confirmation is required
            - ``type_carrier`` (bool): Whether user can act as carrier
            - ``type_owner_oper`` (bool): Whether user is owner operator
            - ``type_company_drs`` (bool): Whether user handles company drivers
            - And many more user-specific configuration fields
            
            Returns empty list if no users match the query.
        
        Raises:
            Exception: If API request fails (authentication, network, etc.)
        
        Examples:
            Search by exact user ID:
            >>> users = client.search_users("cfaa-jthom")
            >>> if users:
            ...     user = users[0]
            ...     print(f"Found: {user['name']} ({user['email_address']})")
            Found: Jack Thompson (jthompson@teamcheema.com)
            
            Search by partial ID (returns multiple users):
            >>> users = client.search_users("cfaa")
            >>> print(f"Found {len(users)} users starting with 'cfaa'")
            Found 100 users starting with 'cfaa'
            
            Search by name:
            >>> users = client.search_users("Jack")
            >>> for user in users:
            ...     print(f"{user['id']}: {user['name']}")
            
            Search by email:
            >>> users = client.search_users("jthompson@teamcheema.com")
            >>> user = users[0]
            >>> print(f"User ID: {user['id']}")
            User ID: cfaa-jthom
            
            Search in specific company:
            >>> users = client.search_users("cfaa-jthom", company_id="TMS2")
            >>> # Returns user from TMS2 company database
            
            Check if user exists:
            >>> users = client.search_users("cfaa-newuser")
            >>> if not users:
            ...     print("User not found")
            
            Get all available fields for a user:
            >>> users = client.search_users("cfaa-jthom")
            >>> if users:
            ...     user = users[0]
            ...     print("Available fields:", list(user.keys()))
            ...     print("Department:", user.get('department_id'))
            ...     print("Is Active:", user.get('is_active'))
            ...     print("Phone:", user.get('phone'))
        
        Note:
            The API may limit the number of results returned. For searches that return
            many results (like searching for "cfaa"), the API may paginate or cap results.
            Empty string queries may not be supported by all API versions.
        """
        params = {"q": query} if query else {}
        results = self.get_json("/users", company_id=company_id, params=params)
        return results if isinstance(results, list) else []

    def search_locations(self, query: str, company_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Search for locations by code or name.
        
        Args:
            query: String to search for locations by code or name
            company_id: Optional override for `X-com.mcleodsoftware.CompanyID`
        
        Returns:
            List of RowLocation objects matching the search query
            
        Examples:
            >>> locations = client.search_locations("NYC01")
            >>> locations = client.search_locations("New York")
        """
        params = {"q": query} if query else {}
        results = self.get_json("/locations", company_id=company_id, params=params)
        return results if isinstance(results, list) else []

    def search_carriers(self, query: str, company_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Search for carriers by ID or name.
        
        Args:
            query: String to search for carriers by ID or name (e.g., "CONSVAWA")
            company_id: Optional override for `X-com.mcleodsoftware.CompanyID`
        
        Returns:
            List of RowPayee objects matching the search query. Each carrier object contains:
            
            **Common Fields:**
            - ``id`` (str): Carrier ID (e.g., "CONSVAWA")
            - ``name`` (str): Carrier name
            - ``address1`` (str): Street address
            - ``city`` (str): City
            - ``state`` (str): State code
            - ``zip_code`` (str): ZIP code
            - ``phone_number`` (str): Phone number
            - ``status`` (str): Status code (A=Active)
            - ``email`` (str): Email address(es)
            
            **Nested in drsPayee (carrier-specific data):**
            - ``dot_number`` (str): DOT number
            - ``icc_number`` (str): MC/ICC number
            - ``power_units`` (int): Number of power units
            - ``drivers`` (int): Number of drivers
            - ``liability_amount`` (float): Liability insurance amount
            - ``cargo_ins_amount`` (float): Cargo insurance amount
            - ``safety_rating`` (str): Safety rating
            - ``out_of_service`` (bool): Whether carrier is out of service
            
            Returns empty list if no carriers match the query.
            
        Examples:
            >>> carriers = client.search_carriers("CONSVAWA", company_id="TMS2")
            >>> if carriers:
            ...     c = carriers[0]
            ...     print(f"{c['id']}: {c['name']}")
            ...     drs = c.get('drsPayee', {})
            ...     print(f"DOT#: {drs.get('dot_number')} | MC#: {drs.get('icc_number')}")
        """
        params = {"q": query} if query else {}
        results = self.get_json("/carriers", company_id=company_id, params=params)
        return results if isinstance(results, list) else []

    def get_carrier_by_code(self, carrier_code: str, company_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Get a carrier profile by its 8-character carrier code.
        
        This method queries the GET /carriers endpoint with the carrier code
        and returns a single RowPayee object if found. Carrier codes are typically
        8 characters (e.g., "SUNNTRCA", "CONSVAWA").
        
        Args:
            carrier_code: 8-character carrier code (e.g., "SUNNTRCA")
            company_id: Optional override for `X-com.mcleodsoftware.CompanyID` header.
                Defaults to the company ID set during client initialization or TMS_COMPANY_ID env var.
        
        Returns:
            RowPayee dictionary for the carrier if found, None otherwise. The carrier object contains:
            
            **Common Fields:**
            - ``id`` (str): Carrier ID (8-character code, e.g., "SUNNTRCA")
            - ``name`` (str): Carrier name
            - ``address1`` (str): Street address
            - ``city`` (str): City
            - ``state`` (str): State code
            - ``zip_code`` (str): ZIP code
            - ``phone_number`` (str): Phone number
            - ``status`` (str): Status code (A=Active)
            - ``email`` (str): Email address(es)
            
            **Nested in drsPayee (carrier-specific data):**
            - ``dot_number`` (str): DOT number
            - ``icc_number`` (str): MC/ICC number
            - ``power_units`` (int): Number of power units
            - ``drivers`` (int): Number of drivers
            - ``liability_amount`` (float): Liability insurance amount
            - ``cargo_ins_amount`` (float): Cargo insurance amount
            - ``safety_rating`` (str): Safety rating
            - ``out_of_service`` (bool): Whether carrier is out of service
            
            Returns None if no carrier matches the code.
        
        Raises:
            Exception: If API request fails (authentication, network, etc.)
        
        Examples:
            Get carrier by 8-character code:
            >>> carrier = client.get_carrier_by_code("SUNNTRCA")
            >>> if carrier:
            ...     print(f"Found: {carrier['name']} (ID: {carrier['id']})")
            ...     drs = carrier.get('drsPayee', {})
            ...     print(f"DOT#: {drs.get('dot_number')} | MC#: {drs.get('icc_number')}")
            
            Get carrier from TMS2:
            >>> carrier = client.get_carrier_by_code("SUNNTRCA", company_id="TMS2")
            >>> if carrier:
            ...     print(f"Carrier: {carrier['name']}")
            ...     print(f"Status: {carrier.get('status')}")
            
            Check if carrier exists:
            >>> carrier = client.get_carrier_by_code("INVALID")
            >>> if not carrier:
            ...     print("Carrier not found")
        """
        if not carrier_code:
            return None
        
        # Strip whitespace and uppercase for consistency
        carrier_code = carrier_code.strip().upper()
        
        # Query the /carriers endpoint with the code
        params = {"q": carrier_code}
        results = self.get_json("/carriers", company_id=company_id, params=params)
        
        if not isinstance(results, list) or len(results) == 0:
            return None
        
        # Find exact match by ID (case-insensitive)
        for carrier in results:
            if carrier.get('id', '').upper() == carrier_code:
                return carrier
        
        # If no exact match, return first result (API may return partial matches)
        return results[0] if results else None

    def get_factoring_company(self, factor_code: str, company_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Get factoring company information by factor code using the table row service.
        
        This method uses the GET /{table}/{id} endpoint (table row service) to retrieve
        factoring company data. The endpoint requires the table name "factoring_company"
        and the factor code as the ID.
        
        Args:
            factor_code: Factor code (e.g., "APEXFOTX")
            company_id: Optional override for `X-com.mcleodsoftware.CompanyID` header.
                Defaults to the company ID set during client initialization or TMS_COMPANY_ID env var.
        
        Returns:
            Dictionary containing factoring company information if found, None otherwise.
            The structure depends on the API response but typically includes fields like:
            - ``id`` (str): Factor code
            - ``name`` (str): Factoring company name
            - Additional fields as returned by the API
            
            Returns None if no factoring company matches the code or if the request fails.
        
        Raises:
            Exception: If API request fails (authentication, network, etc.)
        
        Examples:
            Get factoring company by code:
            >>> factor = client.get_factoring_company("APEXFOTX")
            >>> if factor:
            ...     print(f"Found: {factor.get('name')} (ID: {factor.get('id')})")
            
            Get factoring company from TMS2:
            >>> factor = client.get_factoring_company("APEXFOTX", company_id="TMS2")
            >>> if factor:
            ...     print(f"Factor: {factor.get('name')}")
            
            Check if factoring company exists:
            >>> factor = client.get_factoring_company("INVALID")
            >>> if not factor:
            ...     print("Factoring company not found")
        """
        if not factor_code:
            return None
        
        # Strip whitespace and uppercase for consistency
        factor_code = factor_code.strip().upper()
        
        # Use table row service endpoint: GET /{table}/{id}
        # Table is "factoring_company", ID is the factor code
        try:
            result = self.get_json(f"/factoring_company/{factor_code}", company_id=company_id)
            return result if isinstance(result, dict) else None
        except Exception as e:
            # If 404 or similar, return None instead of raising
            if "404" in str(e) or "not found" in str(e).lower():
                return None
            # Re-raise other exceptions
            raise

    def post_json(self, endpoint: str, data: Optional[Dict] = None, company_id: Optional[str] = None, **kwargs) -> Dict[Any, Any]:
        """
        Make a POST request with JSON data and return JSON response.
        
        Args:
            endpoint: API endpoint
            data: Data to send as JSON
            company_id: Override Company ID for this request (optional)
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response
        """
        if data is not None:
            kwargs['json'] = data
        response = self.post(endpoint, company_id=company_id, **kwargs)
        return response.json()
    
    # Search helpers
    def search_orders(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        changed_after_date: Optional[Union[str, datetime]] = None,
        changed_after_type: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Search orders using flexible table.field criteria with optional
        change tracking window.

        This calls the ``/orders/search`` endpoint and allows passing any
        combination of prefixed fields supported by the API (e.g.,
        ``orders.status``, ``shipper.location_id``, ``consignee.state``,
        ``customer.id``, ``freightGroup.*``), along with optional
        ``changedAfterDate`` and ``changedAfterType`` parameters.

        Args:
            filters: Mapping of query keys to values. Keys should include the
                proper table/field prefix as required by the API
                (for example: {"orders.status": "D", "shipper.location_id": "WARE*"}).
                Supported prefixes:
                - orders: Use `orders` or no prefix
                - stop: Use `shipper` or `consignee` prefixes
                - customer: Use `customer` prefix
                - freight_group: Use `freightGroup` prefix
            company_id: Optional override for Company ID header.
            changed_after_date: Datetime or string for ``changedAfterDate``.
                If a ``datetime`` is provided, it is formatted as
                ``YYYYMMDDHHMMSS±ZZZZ``. Naive datetimes default to ``-0700``.
            changed_after_type: One of ``"Add"`` or ``"Update"``.
            order_by: Optional order by expression. Multiple columns may be
                provided as a comma-delimited string per API docs.
                Format: prefix.field+direction, prefix.field+direction
                Default: orders.id+DESC
            record_length: Optional page size.
            record_offset: Optional page offset.

        Returns:
            List of RowOrders objects returned by the search.

        Examples:
            >>> # Search delivered orders
            >>> client.search_orders({"orders.status": "D"})
            
            >>> # Search by shipper and consignee
            >>> client.search_orders({
            ...     "shipper.location_id": "WARE*",
            ...     "consignee.state": "AL"
            ... })
            
            >>> # Search with change tracking
            >>> client.search_orders(
            ...     {"orders.status": "P"},
            ...     changed_after_date="20250102000000+0000",
            ...     changed_after_type="Add",
            ...     record_length=100,
            ...     record_offset=0,
            ... )
            
            >>> # Search with custom sorting
            >>> client.search_orders(
            ...     {"orders.status": "P"},
            ...     order_by="shipper.sched_arrive_early+ASC"
            ... )
        """
        # Start with a shallow copy to avoid mutating caller input
        params: Dict[str, Any] = dict(filters or {})

        # changedAfterDate formatting
        if changed_after_date is not None:
            if isinstance(changed_after_date, datetime):
                dt = changed_after_date
                # Default -0700 if naive
                if dt.tzinfo is None:
                    from datetime import timezone
                    dt = dt.replace(tzinfo=timezone(timedelta(hours=-7)))
                params["changedAfterDate"] = dt.strftime("%Y%m%d%H%M%S%z")
            else:
                # Allow caller to pass exact string expected by API
                params["changedAfterDate"] = str(changed_after_date)

        # changedAfterType validation/normalization
        if changed_after_type is not None:
            normalized = str(changed_after_type).strip().lower()
            if normalized in ("add",):
                params["changedAfterType"] = "Add"
            elif normalized in ("update", "updated"):
                params["changedAfterType"] = "Update"
            else:
                raise ValueError("changedAfterType must be 'Add' or 'Update'")

        # Sorting and pagination
        if order_by:
            params["orderBy"] = order_by
        if record_length is not None:
            params["recordLength"] = int(record_length)
        if record_offset is not None:
            params["recordOffset"] = int(record_offset)

        results = self.get_json("/orders/search", company_id=company_id, params=params)
        # Ensure list return type
        return results if isinstance(results, list) else []

    def search_orders_by_bol(
        self,
        bol_numbers: Union[str, List[str]],
        company_id: Optional[str] = None,
        include_full: bool = False,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Search orders (loads) by Bill of Lading number(s) using ``/orders/search``.

        This queries the header field ``orders.blnum``. If multiple BOL numbers are
        provided, the API is queried once per number and results are de-duplicated
        by order ``id``.

        Args:
            bol_numbers: Single BOL string or list of BOL strings
            company_id: Optional override for Company ID header
            include_full: When True, fetch full order JSON for each hit
            record_length: Optional page size for each individual query
            record_offset: Optional offset for each individual query

        Returns:
            List of order dictionaries (full orders when ``include_full`` is True,
            otherwise the RowOrders objects returned by the search endpoint).
        """
        # Normalize input
        if isinstance(bol_numbers, str):
            bol_list = [bol_numbers.strip()]
        else:
            bol_list = [str(b).strip() for b in bol_numbers if str(b).strip()]

        if not bol_list:
            return []

        # Accumulate results, dedupe by order id
        orders_by_id: Dict[str, Dict[str, Any]] = {}

        for bol in bol_list:
            params: Dict[str, Any] = {"orders.blnum": bol}
            if record_length is not None:
                params["recordLength"] = int(record_length)
            if record_offset is not None:
                params["recordOffset"] = int(record_offset)

            try:
                results = self.get_json("/orders/search", company_id=company_id, params=params)
            except Exception as e:
                # Continue to next BOL if one search fails
                continue

            if not isinstance(results, list):
                continue

            for row in results:
                order_id = str(row.get("id")) if isinstance(row, dict) else None
                if order_id and order_id not in orders_by_id:
                    orders_by_id[order_id] = row

        # Optionally expand to full order payloads
        if include_full:
            full_orders: List[Dict[str, Any]] = []
            for order_id in list(orders_by_id.keys()):
                try:
                    full_orders.append(self.get_load_json(order_id, company_id=company_id))
                except Exception:
                    # Fallback to the summary row if full fetch fails
                    full_orders.append(orders_by_id[order_id])
            return full_orders

        return list(orders_by_id.values())

    def search_movements(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        changed_after_date: Optional[Union[str, datetime]] = None,
        changed_after_type: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Search movements using flexible table.field criteria with optional
        change tracking window.

        This calls the ``/movements/search`` endpoint and allows passing any
        combination of prefixed fields supported by the API (e.g.,
        ``movement.status``, ``origin.location_id``, ``destination.state``,
        ``driver.user``/``driver2.user``, ``tractor.trctr``/``trctr2``,
        ``trailer.trlr``/``trlr2``), along with optional
        ``changedAfterDate`` and ``changedAfterType`` parameters.

        Args:
            filters: Mapping of query keys to values. Keys should include the
                proper table/field prefix as required by the API
                (for example: {"destination.state": "AL"}).
            company_id: Optional override for Company ID header.
            changed_after_date: Datetime or string for ``changedAfterDate``.
                If a ``datetime`` is provided, it is formatted as
                ``YYYYMMDDHHMMSS±ZZZZ``. Naive datetimes default to ``-0700``.
            changed_after_type: One of ``"Add"`` or ``"Update"``.
            order_by: Optional order by expression. Multiple columns may be
                provided as a comma-delimited string per API docs.
            record_length: Optional page size.
            record_offset: Optional page offset.

        Returns:
            List of movement rows returned by the search.

        Examples:
            >>> client.search_movements(
            ...     {"destination.state": "AL", "movement.status": "P"},
            ...     changed_after_date="20250102000000+0000",
            ...     changed_after_type="Add",
            ...     record_length=100,
            ...     record_offset=0,
            ... )
        """
        # Start with a shallow copy to avoid mutating caller input
        params: Dict[str, Any] = dict(filters or {})

        # changedAfterDate formatting
        if changed_after_date is not None:
            if isinstance(changed_after_date, datetime):
                dt = changed_after_date
                # Default -0700 if naive
                if dt.tzinfo is None:
                    from datetime import timezone
                    dt = dt.replace(tzinfo=timezone(timedelta(hours=-7)))
                params["changedAfterDate"] = dt.strftime("%Y%m%d%H%M%S%z")
            else:
                # Allow caller to pass exact string expected by API
                params["changedAfterDate"] = str(changed_after_date)

        # changedAfterType validation/normalization
        if changed_after_type is not None:
            normalized = str(changed_after_type).strip().lower()
            if normalized in ("add",):
                params["changedAfterType"] = "Add"
            elif normalized in ("update", "updated"):
                params["changedAfterType"] = "Update"
            else:
                raise ValueError("changedAfterType must be 'Add' or 'Update'")

        # Sorting and pagination
        if order_by:
            params["orderBy"] = order_by
        if record_length is not None:
            params["recordLength"] = int(record_length)
        if record_offset is not None:
            params["recordOffset"] = int(record_offset)

        results = self.get_json("/movements/search", company_id=company_id, params=params)
        # Ensure list return type
        return results if isinstance(results, list) else []

    def search_settlements(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        changed_after_date: Optional[Union[str, datetime]] = None,
        changed_after_type: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Search settlements using flexible table.field criteria with optional
        change tracking window.

        This calls the ``/settlements/search`` endpoint and allows passing any
        combination of prefixed fields supported by the API (e.g.,
        ``settlement.ok2pay_date``, ``settlement.ready_to_pay_flag``, ``movement.loaded``,
        ``payee.id``), along with optional ``changedAfterDate`` and
        ``changedAfterType`` parameters.

        Args:
            filters: Mapping of query keys to values. Keys should include the
                proper table/field prefix as required by the API
                (for example: {"settlement.ready_to_pay_flag": "n", "movement.loaded": "L"}).
                Supported prefixes:
                - settlement: Use `settlement` or no prefix
                - movement: Use `movement` prefix
                - payee: Use `payee` prefix
            company_id: Optional override for Company ID header.
            changed_after_date: Datetime or string for ``changedAfterDate``.
                If a ``datetime`` is provided, it is formatted as
                ``YYYYMMDDHHMMSS±ZZZZ``. Naive datetimes default to ``-0700``.
            changed_after_type: One of ``"Add"`` or ``"Update"``.
            order_by: Optional order by expression. Multiple columns may be
                provided as a comma-delimited string per API docs.
                Format: prefix.field+direction, prefix.field+direction
                Default: settlement.transfer_date+DESC
            record_length: Optional page size (default 100 if auto_paginate is True).
            record_offset: Optional page offset (ignored if auto_paginate is True).
            auto_paginate: When True, automatically fetches all pages by incrementing
                record_offset until no more results are returned. Use this to get all
                results when there may be more than one page.

        Returns:
            List of RowSettlement objects returned by the search.

        Examples:
            >>> # Search settlements on hold (not ready to pay)
            >>> client.search_settlements({"settlement.ready_to_pay_flag": "n"})
            
            >>> # Search by payee and ok to pay date
            >>> client.search_settlements({
            ...     "settlement.payee_id": "*",
            ...     "settlement.ok2pay_date": ">=t-7"
            ... })
            
            >>> # Search settlements for loaded movements
            >>> client.search_settlements({
            ...     "settlement.ready_to_pay_flag": "n",
            ...     "movement.loaded": "L"
            ... })
            
            >>> # Search with change tracking
            >>> client.search_settlements(
            ...     {"settlement.loaded": "L"},
            ...     changed_after_date="20250102000000+0000",
            ...     changed_after_type="Add",
            ...     record_length=100,
            ...     record_offset=0,
            ... )
            
            >>> # Search with custom sorting
            >>> client.search_settlements(
            ...     {"settlement.payee_id": "*"},
            ...     order_by="settlement.ok2pay_date+DESC"
            ... )
            
            >>> # Search with auto-pagination to get ALL results
            >>> all_settlements = client.search_settlements(
            ...     {"settlement.ready_to_pay_flag": "n"},
            ...     auto_paginate=True
            ... )
        """
        # Auto-pagination using offset-based pagination
        if auto_paginate:
            all_rows: List[Dict[str, Any]] = []
            page_size = int(record_length) if record_length is not None else 100
            max_pages = 1000  # Safety limit (100,000 records max)
            offset = 0
            
            for page_num in range(1, max_pages + 1):
                page_results = self.search_settlements(
                    filters=filters,
                    company_id=company_id,
                    changed_after_date=changed_after_date,
                    changed_after_type=changed_after_type,
                    order_by=order_by,
                    record_length=page_size,
                    record_offset=offset,
                    auto_paginate=False,  # Prevent recursion
                )
                
                if not page_results or len(page_results) == 0:
                    break
                
                all_rows.extend(page_results)
                
                # If we got fewer results than requested, we're done
                if len(page_results) < page_size:
                    break
                
                offset += page_size
            
            return all_rows
        
        # Single-page request (no auto-pagination)
        # Start with a shallow copy to avoid mutating caller input
        params: Dict[str, Any] = dict(filters or {})

        # changedAfterDate formatting
        if changed_after_date is not None:
            if isinstance(changed_after_date, datetime):
                dt = changed_after_date
                # Default -0700 if naive
                if dt.tzinfo is None:
                    from datetime import timezone
                    dt = dt.replace(tzinfo=timezone(timedelta(hours=-7)))
                params["changedAfterDate"] = dt.strftime("%Y%m%d%H%M%S%z")
            else:
                # Allow caller to pass exact string expected by API
                params["changedAfterDate"] = str(changed_after_date)

        # changedAfterType validation/normalization
        if changed_after_type is not None:
            normalized = str(changed_after_type).strip().lower()
            if normalized in ("add",):
                params["changedAfterType"] = "Add"
            elif normalized in ("update", "updated"):
                params["changedAfterType"] = "Update"
            else:
                raise ValueError("changedAfterType must be 'Add' or 'Update'")

        # Sorting and pagination
        if order_by:
            params["orderBy"] = order_by
        if record_length is not None:
            params["recordLength"] = int(record_length)
        if record_offset is not None:
            params["recordOffset"] = int(record_offset)

        results = self.get_json("/settlements/search", company_id=company_id, params=params)
        # Ensure list return type
        return results if isinstance(results, list) else []

    def get_settlements_on_hold(
        self,
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Get settlements that are on hold (not ready to pay).

        This is a convenience method that searches for settlements where
        ``ready_to_pay_flag`` is "n" (not ready to pay). Equivalent to calling
        ``search_settlements({"settlement.ready_to_pay_flag": "n"})``.

        Args:
            company_id: Optional override for Company ID header.
            order_by: Optional order by expression. Multiple columns may be
                provided as a comma-delimited string.
                Default: settlement.transfer_date+DESC
            record_length: Optional page size (default 100 if auto_paginate is True).
            record_offset: Optional page offset (ignored if auto_paginate is True).
            auto_paginate: When True, automatically fetches all pages by incrementing
                record_offset until no more results are returned. Use this to get all
                results when there may be more than one page.

        Returns:
            List of RowSettlement objects that are on hold.

        Examples:
            >>> # Get all settlements on hold
            >>> settlements = client.get_settlements_on_hold()
            
            >>> # Get settlements on hold with pagination
            >>> page = client.get_settlements_on_hold(
            ...     record_length=100,
            ...     record_offset=0
            ... )
            
            >>> # Get settlements on hold sorted by ok to pay date
            >>> settlements = client.get_settlements_on_hold(
            ...     order_by="settlement.ok2pay_date+DESC"
            ... )
            
            >>> # Get settlements on hold from different company
            >>> tms2_settlements = client.get_settlements_on_hold(company_id="TMS2")
            
            >>> # Get all settlements on hold (auto-paginate)
            >>> all_on_hold = client.get_settlements_on_hold(auto_paginate=True)
            
            >>> # Process results
            >>> for settlement in settlements:
            ...     print(f"Settlement ID: {settlement.get('id')}")
            ...     print(f"Payee: {settlement.get('payee_id')}")
            ...     print(f"Amount: ${settlement.get('amount', 0)}")
        """
        return self.search_settlements(
            filters={"settlement.ready_to_pay_flag": "n"},
            company_id=company_id,
            order_by=order_by,
            record_length=record_length,
            record_offset=record_offset,
            auto_paginate=auto_paginate,
        )

    def update_deduction_status(
        self,
        deduction_id: str,
        status: str,
        company_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Update the ready_to_pay_flag (process status) for a single deduction.
        
        Uses PUT /drs_pending_deduct/update to change the status.
        
        Args:
            deduction_id: The deduction ID to update
            status: New status for ready_to_pay_flag. Valid values:
                - "Y" - Process (ready to pay)
                - "N" - Hold (not ready to pay)  
                - "V" - Void
            company_id: Override Company ID for this request (optional)
            
        Returns:
            Updated deduction object from the API
            
        Raises:
            ValueError: If status is not Y, N, or V
            
        Examples:
            >>> # Put a deduction on hold
            >>> updated = client.update_deduction_status("zz1j7hpdj951c0gCFAATS3", "N", company_id="TMS2")
            
            >>> # Mark deduction ready to process
            >>> updated = client.update_deduction_status("zz1j7hpdj951c0gCFAATS3", "Y", company_id="TMS2")
        """
        status = status.upper()
        if status not in ("Y", "N", "V"):
            raise ValueError(f"Invalid status '{status}'. Must be 'Y' (Process), 'N' (Hold), or 'V' (Void)")
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        payload = {
            "__type": "drs_pending_deduct",
            "id": deduction_id,
            "ready_to_pay_flag": status
        }
        
        response = self.put(
            "/drs_pending_deduct/update",
            json=payload,
            headers=headers,
            company_id=company_id
        )
        return response.json()

    def update_settlement_status(
        self,
        movement_id: Union[str, int],
        status: str,
        company_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Update the ready_to_pay_flag (process status) for all settlements AND 
        deductions on a movement.
        
        Finds all settlements and deductions for the given movement_id and updates
        their ready_to_pay_flag to the specified status.
        
        Args:
            movement_id: The movement ID to find settlements/deductions for
            status: New status for ready_to_pay_flag. Valid values:
                - "Y" - Process (ready to pay)
                - "N" - Hold (not ready to pay)  
                - "V" - Void
            company_id: Override Company ID for this request (optional)
            
        Returns:
            Dict with 'settlements' and 'deductions' lists of updated objects
            
        Raises:
            ValueError: If status is not Y, N, or V
            Exception: If no settlements found or update fails
            
        Examples:
            >>> # Put a movement's settlements and deductions on hold
            >>> result = client.update_settlement_status("1258474", "N")
            >>> print(f"Updated {len(result['settlements'])} settlements")
            >>> print(f"Updated {len(result['deductions'])} deductions")
            
            >>> # Mark ready to process
            >>> result = client.update_settlement_status("1258474", "Y")
            
            >>> # Update in different company
            >>> result = client.update_settlement_status("1258474", "N", company_id="TMS2")
        """
        # Validate status
        status = status.upper()
        if status not in ("Y", "N", "V"):
            raise ValueError(f"Invalid status '{status}'. Must be 'Y' (Process), 'N' (Hold), or 'V' (Void)")
        
        movement_id_str = str(movement_id)
        
        # Find all settlements for this movement
        settlements = self.search_settlements(
            {"movement.id": movement_id_str},
            company_id=company_id,
        )
        
        if not settlements:
            raise Exception(f"No settlements found for movement_id {movement_id_str}")
        
        updated_settlements = []
        updated_deductions = []
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        # Update settlements
        for settlement in settlements:
            payload = {
                "__type": "settlement",
                "id": settlement.get("id"),
                "ready_to_pay_flag": status
            }
            
            response = self.put(
                "/settlement/update",
                json=payload,
                headers=headers,
                company_id=company_id
            )
            updated_settlements.append(response.json())
        
        # Find and update all deductions for this movement
        try:
            deductions = self.search_deductions(
                {"drs_pending_deduct.movement_id": movement_id_str},
                company_id=company_id,
            )
        except Exception:
            deductions = []
        
        for deduction in deductions:
            deduction_id = deduction.get("id")
            if deduction_id:
                payload = {
                    "__type": "drs_pending_deduct",
                    "id": deduction_id,
                    "ready_to_pay_flag": status
                }
                
                response = self.put(
                    "/drs_pending_deduct/update",
                    json=payload,
                    headers=headers,
                    company_id=company_id
                )
                updated_deductions.append(response.json())
        
        return {
            "settlements": updated_settlements,
            "deductions": updated_deductions
        }

    def search_misc_billing_history(
        self,
        bill_date_after: Union[str, datetime],
        company_id: Optional[str] = None,
        include_user: Optional[bool] = None,
        include_customer: Optional[bool] = None,
    ) -> List[Dict[str, Any]]:
        """
        Search miscellaneous billing history records by bill date.
        
        Retrieves a list of historical miscellaneous bills with bill_date 
        occurring after the specified date.
        
        Args:
            bill_date_after: Date to search after. Can be:
                - datetime object (formatted as YYYYMMDDHHMMSS±ZZZZ, naive defaults to -0700)
                - String in API format (YYYYMMDDHHMMSS±ZZZZ) or relative format (e.g., "t-100")
            company_id: Optional override for Company ID header
            include_user: Whether to include billing user details with each bill
            include_customer: Whether to include customer details with each bill
            
        Returns:
            List of RowMiscBillHist objects (misc_bill_hist records) matching the criteria
            
        Examples:
            >>> # Search using datetime
            >>> from datetime import datetime
            >>> bills = client.search_misc_billing_history(
            ...     datetime(2023, 4, 1, 0, 0, 0)
            ... )
            
            >>> # Search using string date
            >>> bills = client.search_misc_billing_history(
            ...     "20230401000000-0700"
            ... )
            
            >>> # Include user and customer details
            >>> bills = client.search_misc_billing_history(
            ...     "20230401000000-0700",
            ...     include_user=True,
            ...     include_customer=True
            ... )
        """
        # Format the date parameter
        if isinstance(bill_date_after, datetime):
            dt = bill_date_after
            # Default -0700 if naive
            if dt.tzinfo is None:
                from datetime import timezone
                dt = dt.replace(tzinfo=timezone(timedelta(hours=-7)))
            date_str = dt.strftime("%Y%m%d%H%M%S%z")
        else:
            # Allow caller to pass exact string expected by API
            date_str = str(bill_date_after)
        
        # Build query parameters
        # API expects: bill_date=>=YYYYMMDDHHMMSS±ZZZZ
        params = {
            "bill_date": f">={date_str}"
        }
        
        # Add optional parameters
        if include_user is not None:
            params["includeUser"] = bool(include_user)
        if include_customer is not None:
            params["includeCustomer"] = bool(include_customer)
        
        # Make the API request
        results = self.get_json("/billing/miscBilling/history", company_id=company_id, params=params)
        
        # Ensure list return type
        return results if isinstance(results, list) else []

    def search_billing_history(
        self,
        bill_date: Union[str, datetime, None] = None,
        company_id: Optional[str] = None,
        include_users: Optional[bool] = None,
        include_customer: Optional[bool] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
        **additional_filters: Any,
    ) -> List[Dict[str, Any]]:
        """
        Search freight billing history records by bill_date and other criteria.
        
        Retrieves a list of historical freight billing records matching the given
        request parameters. Supports relative date formats (e.g., "t-1" for yesterday)
        and formatted dates, plus any combination of fields from the billing_history table.
        
        Args:
            bill_date: Date to search for. Can be:
                - Relative format string (e.g., "t-1" for yesterday, "t-100" for last 100 days)
                - Comparison format (e.g., ">=t-100" for last 100 days)
                - datetime object (formatted as YYYYMMDDHHMMSS±ZZZZ, naive defaults to -0700)
                - String in API format (YYYYMMDDHHMMSS±ZZZZ)
                - None to search without date filter
            company_id: Optional override for Company ID header
            include_users: Whether to include user detail records with each invoice
            include_customer: Whether to include customer details with each invoice
            record_length: Optional page size (default 100, max 100)
            record_offset: Optional offset (NOTE: API ignores this; use auto_paginate instead)
            auto_paginate: When True, fetches all pages using cursor-based pagination 
                with 'id > last_id'. Use this to get all results when there may be >100.
            **additional_filters: Additional search criteria from billing_history table.
                Examples: is_summary_bill="Y", blnum="12345*", ship_date=">=t-100"
                
        Returns:
            List of RowBillingHistory objects (billing_history records) matching the criteria
            
        Examples:
            >>> # Search yesterday (may be capped at 100)
            >>> bills = client.search_billing_history("t-1")
            
            >>> # Search with auto-pagination to get ALL results
            >>> all_bills = client.search_billing_history("t-1", auto_paginate=True)
            
            >>> # Range query with pagination
            >>> all_bills = client.search_billing_history(">=t-100", auto_paginate=True)
            
            >>> # Include user and customer details
            >>> bills = client.search_billing_history(
            ...     "t-1",
            ...     include_users=True,
            ...     include_customer=True,
            ...     auto_paginate=True
            ... )
        """
        import sys
        
        params: Dict[str, Any] = {}
        
        # Handle bill_date parameter
        if bill_date is not None:
            if isinstance(bill_date, datetime):
                dt = bill_date
                # Default -0700 if naive
                if dt.tzinfo is None:
                    from datetime import timezone
                    dt = dt.replace(tzinfo=timezone(timedelta(hours=-7)))
                params["bill_date"] = dt.strftime("%Y%m%d%H%M%S%z")
            else:
                params["bill_date"] = str(bill_date)
        
        # Add optional parameters
        if include_users is not None:
            params["includeUsers"] = bool(include_users)
        if include_customer is not None:
            params["includeCustomer"] = bool(include_customer)
        # Enforce 100-record pages by default for consistency across companies
        page_size = int(record_length) if record_length is not None else 100
        params["recordLength"] = page_size
        if record_offset is not None:
            params["recordOffset"] = int(record_offset)
        
        # Add any additional filters from billing_history table
        params.update(additional_filters)
        
        # Auto-pagination using cursor-based 'id > last_id'
        if auto_paginate:
            all_rows: List[Dict[str, Any]] = []
            max_pages = 100  # Safety limit (10,000 records max)
            last_id = None
            
            for page_num in range(1, max_pages + 1):
                # Create params for this page
                page_params = dict(params)
                
                # Add id filter to get next batch (skip first page)
                if last_id is not None:
                    page_params["id"] = f">{last_id}"
                
                page = self.get_json("/billing/history", company_id=company_id, params=page_params)
                
                if not isinstance(page, list) or len(page) == 0:
                    break
                
                all_rows.extend(page)
                
                # Continue only when we got exactly the enforced page_size
                if len(page) != page_size:
                    if len(page) > page_size:
                        print(
                            f"WARNING: API ignored recordLength={page_size} and returned {len(page)} rows; "
                            f"treating as last page.",
                            file=sys.stderr,
                        )
                    break
                
                # Get the last id for next iteration
                last_id = page[-1].get('id')
                if not last_id:
                    print(f"WARNING: No 'id' field in response, cannot paginate further", 
                          file=sys.stderr)
                    break
            
            return all_rows

        # Single-page request (no auto-pagination)
        return_rows = self.get_json("/billing/history", company_id=company_id, params=params)
        if not isinstance(return_rows, list):
            return []

        # Enforce page_size on single-page calls for consistent pagination to consumers
        if len(return_rows) > page_size:
            print(
                f"WARNING: API ignored recordLength={page_size} and returned {len(return_rows)} rows; "
                f"trimming to first {page_size} for pagination consistency.",
                file=sys.stderr,
            )
            return_rows = return_rows[:page_size]

        return return_rows

    # Convenience methods for common operations
    def get_available_images(self, row_type: str, row_id: str, company_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get available images for a specific record type and ID.
        
        Args:
            row_type: Type of record (use RowTypes constants)
            row_id: ID of the record
            company_id: Override Company ID for this request (optional)
            
        Returns:
            List of available images for the specified record
            
        Examples:
            >>> client.get_available_images(RowTypes.ORDER, "12345")
            >>> client.get_available_images(RowTypes.LOCATION, "67890", company_id="TMS2")
        """
        return self.get_json(f"/images/{row_type}/{row_id}", company_id=company_id)
    
    def get_enriched_images(self, row_type: str, row_id: str, company_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get available images with enriched document type information.
        
        This method combines image data with document type details to provide
        human-readable descriptions and full document type metadata.
        
        Args:
            row_type: Type of record (use RowTypes constants)
            row_id: ID of the record
            company_id: Override Company ID for this request (optional)
            
        Returns:
            List of images with enriched document type information
            
        Examples:
            >>> enriched_images = client.get_enriched_images(RowTypes.ORDER, "5000003")
            >>> for image in enriched_images:
            ...     print(f"{image['description']} ({image['imageCount']} files)")
        """
        # Get the basic images
        images = self.get_available_images(row_type, row_id, company_id)
        
        if not images:
            return images
            
        # Get document types for enrichment
        try:
            doc_types = self.get_available_doctypes(row_type, row_id, company_id=company_id)
            
            # Create lookup map: documentTypeId -> doc_type_info
            doc_type_map = {}
            if isinstance(doc_types, list):
                for doc_type in doc_types:
                    if 'id' in doc_type:
                        doc_type_map[str(doc_type['id'])] = doc_type
                        
            # Enrich images with document type info
            enriched_images = []
            for image in images:
                enriched_image = image.copy()
                
                doc_type_id = str(image.get('documentTypeId', ''))
                if doc_type_id in doc_type_map:
                    doc_type_info = doc_type_map[doc_type_id]
                    # Get clean document type name by removing first 3 characters (e.g., "01-")
                    full_description = doc_type_info.get('description', image.get('descr', 'Unknown'))
                    clean_name = full_description[3:] if len(full_description) > 3 else full_description
                    
                    enriched_image['documentTypeName'] = clean_name
                    enriched_image['documentTypeId'] = doc_type_info.get('id', doc_type_id)
                    enriched_image['documentTypeFullDescription'] = full_description
                else:
                    # Fallback to existing description with same cleaning
                    fallback_desc = image.get('descr', 'Unknown Document Type')
                    clean_name = fallback_desc[3:] if len(fallback_desc) > 3 else fallback_desc
                    enriched_image['documentTypeName'] = clean_name
                    enriched_image['documentTypeId'] = doc_type_id
                    enriched_image['documentTypeFullDescription'] = fallback_desc
                    
                enriched_images.append(enriched_image)
                
            return enriched_images
            
        except Exception:
            # If document type enrichment fails, return basic images
            return images
    
    def get_image_pdf(self, image_id: str, company_id: Optional[str] = None) -> bytes:
        """
        Retrieve the image as PDF binary data.
        
        Args:
            image_id: The ID of the image (from image listings)
            company_id: Override Company ID for this request (optional)
            
        Returns:
            Raw PDF binary data
            
        Examples:
            >>> pdf_data = client.get_image_pdf("dta.bol.7.0.5000003")
            >>> with open("invoice.pdf", "wb") as f:
            ...     f.write(pdf_data)
        """
        headers = {"Accept": "application/pdf"}
        response = self.get(f"/images/{image_id}", company_id=company_id, headers=headers)
        return response.content
    
    def save_image_pdf(self, image_id: str, filepath: str, company_id: Optional[str] = None) -> str:
        """
        Download and save an image as PDF file.
        
        Args:
            image_id: The ID of the image
            filepath: Where to save the file (.pdf extension will be added if missing)
            company_id: Override Company ID for this request (optional)
            
        Returns:
            The actual filepath where the file was saved
            
        Examples:
            >>> client.save_image_pdf("dta.bol.7.0.5000003", "invoice")
            'invoice.pdf'
            
            >>> client.save_image_pdf("dta.bol.7.0.5000003", "docs/invoice")
            'docs/invoice.pdf'
        """
        # Get the PDF data
        pdf_data = self.get_image_pdf(image_id, company_id)
        
        # Add .pdf extension if not present
        if not filepath.endswith(".pdf"):
            filepath = filepath + ".pdf"
            
        # Save the file
        with open(filepath, "wb") as f:
            f.write(pdf_data)
            
        return filepath
    
    def get_image_for_web(self, image_id: str, company_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get image data formatted for web response.
        
        Returns the PDF binary data along with proper HTTP headers for browser download.
        Perfect for web backends serving to browsers.
        
        Args:
            image_id: The ID of the image
            company_id: Override Company ID for this request (optional)
            
        Returns:
            Dictionary with 'data', 'headers', and 'filename' for web frameworks
            
        Examples:
            # Flask
            >>> result = client.get_image_for_web("dta.bol.7.0.5000003")
            >>> return Response(result['data'], headers=result['headers'])
            
            # FastAPI  
            >>> result = client.get_image_for_web("dta.bol.7.0.5000003")
            >>> return Response(result['data'], media_type="application/pdf", 
            ...                headers={"Content-Disposition": result['headers']['Content-Disposition']})
            
            # Django
            >>> result = client.get_image_for_web("dta.bol.7.0.5000003")
            >>> response = HttpResponse(result['data'], content_type='application/pdf')
            >>> response['Content-Disposition'] = result['headers']['Content-Disposition']
        """
        # Get the PDF data
        pdf_data = self.get_image_pdf(image_id, company_id)
        
        # Generate a clean filename from the image ID
        # Extract meaningful parts from ID like "dta.bol.7.0.5000003"
        parts = image_id.split('.')
        if len(parts) >= 3:
            # Try to create filename like "5000003_doc7.pdf"
            record_id = parts[-1] if parts[-1] else "document"
            doc_type = parts[-2] if len(parts) > 1 else "doc"
            filename = f"{record_id}_doc{doc_type}.pdf"
        else:
            filename = f"{image_id.replace('.', '_')}.pdf"
        
        # Return web-ready response data
        return {
            'data': pdf_data,
            'headers': {
                'Content-Type': 'application/pdf',
                'Content-Disposition': f'attachment; filename="{filename}"',
                'Content-Length': str(len(pdf_data)),
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Pragma': 'no-cache',
                'Expires': '0'
            },
            'filename': filename,
            'size': len(pdf_data)
        }
    
    def get_available_doctypes(self, row_type: str, row_id: str, movement_id: Optional[str] = None, 
                             company_id: Optional[str] = None, use_cache: bool = True) -> Dict[str, Any]:
        """
        Get available document types for a specific record type and ID.
        
        Args:
            row_type: Type of record (use RowTypes constants)
            row_id: ID of the specific record
            movement_id: ID of the movement associated with the row (optional)
            company_id: Override Company ID for this request (optional)
            use_cache: Whether to use cached results (default: True)
            
        Returns:
            List of DocumentType objects available for the specified record
            
        Examples:
            >>> order_doctypes = client.get_available_doctypes(RowTypes.ORDER, "12345")
            >>> location_doctypes = client.get_available_doctypes(RowTypes.LOCATION, "67890", company_id="TMS2")
            >>> movement_doctypes = client.get_available_doctypes(RowTypes.ORDER, "12345", movement_id="MOV123")
        """
        # Create cache key including row_id since doctypes might vary by specific record
        cache_key = f"{row_type}_{row_id}_{movement_id or 'none'}_{company_id or 'default'}"
        
        # Return cached result if available and cache is enabled
        if use_cache and cache_key in self._doctype_cache:
            return self._doctype_cache[cache_key]
        
        # Build query parameters
        params = {}
        if movement_id:
            params['movementId'] = movement_id
        
        # Fetch from API using correct endpoint structure
        doctypes = self.get_json(f"/images/{row_type}/{row_id}/documentTypes", 
                               company_id=company_id, params=params)
        
        # Cache the result
        if use_cache:
            self._doctype_cache[cache_key] = doctypes
            
        return doctypes
    
    def get_comments(self, parent_row_type: str, parent_row_id: Union[str, int], 
                     company_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve comments for a given parent row type and row ID.
        
        Retrieves a list of comments associated with a specific record (driver, settlement, etc.).
        The endpoint supports various parent row types such as Driver (D) and Settlement (M).
        
        Args:
            parent_row_type: The comment record's parent row type. Use RowTypes constants:
                - RowTypes.DRIVER for drivers (D)
                - RowTypes.SETTLEMENT for settlements (M)
                - Other row types as needed
            parent_row_id: The comment record's parent row ID (e.g., driver ID, settlement ID)
            company_id: Optional override for Company ID header (defaults to TMS or TMS2 based on env/config)
        
        Returns:
            List of RowComments objects. Each comment includes:
            - Basic comment fields (id, comments, entered_date, entered_user_id, etc.)
            - commentTypeDescr: Description of the comment type
            - enteredByUser: User details for the user who entered the comment
        
        Examples:
            >>> # Get comments for a driver
            >>> driver_comments = client.get_comments(RowTypes.DRIVER, "BJM01")
            >>> for comment in driver_comments:
            ...     print(f"{comment['enteredByUser']['name']}: {comment['comments']}")
            
            >>> # Get comments for a settlement
            >>> settlement_comments = client.get_comments(RowTypes.SETTLEMENT, "zz1ivr5ucal12v8CFAATS3", company_id="TMS2")
            >>> for comment in settlement_comments:
            ...     print(f"{comment['commentTypeDescr']['descr']}: {comment['comments']}")
        """
        parent_row_id_str = str(parent_row_id)
        endpoint = f"/comments/{parent_row_type}/{parent_row_id_str}"
        results = self.get_json(endpoint, company_id=company_id)
        return results if isinstance(results, list) else []
    
    def get_driver_comments(self, driver_id: Union[str, int], company_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Convenience method to get comments for a driver.
        
        Args:
            driver_id: The driver ID
            company_id: Optional override for Company ID header
        
        Returns:
            List of RowComments objects for the specified driver
        
        Examples:
            >>> driver_comments = client.get_driver_comments("BJM01")
            >>> settlement_comments = client.get_driver_comments("BJM01", company_id="TMS2")
        """
        return self.get_comments(RowTypes.DRIVER, driver_id, company_id=company_id)
    
    def get_settlement_comments(self, settlement_id: Union[str, int], company_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Convenience method to get comments for a settlement.
        
        Args:
            settlement_id: The settlement ID
            company_id: Optional override for Company ID header
        
        Returns:
            List of RowComments objects for the specified settlement
        
        Examples:
            >>> settlement_comments = client.get_settlement_comments("zz1ivr5ucal12v8CFAATS3", company_id="TMS2")
        """
        return self.get_comments(RowTypes.SETTLEMENT, settlement_id, company_id=company_id)
    
    def create_comment(self, parent_row_type: str, parent_row_id: Union[str, int], 
                      comment_type_id: str, comments: str, company_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new comment for a given parent row type and row ID.
        
        Creates a comment record using the PUT /comments/create endpoint. The payload
        is kept minimal with only the required fields.
        
        Args:
            parent_row_type: The parent row type. Use RowTypes constants:
                - RowTypes.DRIVER for drivers (D)
                - RowTypes.SETTLEMENT for settlements (M)
                - Other row types as needed
            parent_row_id: The parent row ID (e.g., driver ID, settlement ID)
            comment_type_id: The comment type ID (e.g., "AP" for AP NOTES)
            comments: The comment text to create
            company_id: Optional override for Company ID header
        
        Returns:
            The created RowComments object from the API response
        
        Examples:
            >>> # Create a settlement comment
            >>> comment = client.create_comment(
            ...     RowTypes.SETTLEMENT, 
            ...     "zz1ivr5ucal12v8CFAATS3",
            ...     "AP",
            ...     "Payment processed successfully",
            ...     company_id="TMS2"
            ... )
            >>> print(f"Created comment ID: {comment['id']}")
            
            >>> # Create a driver comment
            >>> comment = client.create_comment(
            ...     RowTypes.DRIVER,
            ...     "BJM01",
            ...     "GEN",
            ...     "Driver called in sick"
            ... )
        """
        parent_row_id_str = str(parent_row_id)
        
        # Minimal payload - only required fields
        payload = {
            "__type": "comments",
            "parent_row_type": parent_row_type,
            "parent_row_id": parent_row_id_str,
            "comment_type_id": comment_type_id,
            "comments": comments
        }
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        response = self.put(
            "/comments/create",
            json=payload,
            headers=headers,
            company_id=company_id
        )
        return response.json()
    
    def create_driver_comment(self, driver_id: Union[str, int], comment_type_id: str, 
                              comments: str, company_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Convenience method to create a comment for a driver.
        
        Args:
            driver_id: The driver ID
            comment_type_id: The comment type ID (e.g., "AP", "GEN")
            comments: The comment text to create
            company_id: Optional override for Company ID header
        
        Returns:
            The created RowComments object
        
        Examples:
            >>> comment = client.create_driver_comment("BJM01", "GEN", "Driver called in sick")
            >>> print(f"Created comment: {comment['id']}")
        """
        return self.create_comment(RowTypes.DRIVER, driver_id, comment_type_id, comments, company_id=company_id)
    
    def create_settlement_comment(self, settlement_id: Union[str, int], comment_type_id: str,
                                  comments: str, company_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Convenience method to create a comment for a settlement.
        
        Args:
            settlement_id: The settlement ID
            comment_type_id: The comment type ID (e.g., "AP", "GEN")
            comments: The comment text to create
            company_id: Optional override for Company ID header
        
        Returns:
            The created RowComments object
        
        Examples:
            >>> comment = client.create_settlement_comment(
            ...     "zz1ivr5ucal12v8CFAATS3",
            ...     "AP",
            ...     "Payment processed successfully",
            ...     company_id="TMS2"
            ... )
            >>> print(f"Created comment: {comment['id']}")
        """
        return self.create_comment(RowTypes.SETTLEMENT, settlement_id, comment_type_id, comments, company_id=company_id)
    
    def delete_comment(self, comment_id: Union[str, int], company_id: Optional[str] = None) -> bool:
        """
        Delete a comment by its ID.
        
        Deletes a comment record using the DELETE /comments/{id} endpoint.
        
        Args:
            comment_id: The ID of the comment to delete
            company_id: Optional override for Company ID header
        
        Returns:
            True if deletion was successful, False otherwise
        
        Examples:
            >>> # Delete a comment
            >>> success = client.delete_comment("zz1jdvsrs3i0icoAATSAPP", company_id="TMS2")
            >>> if success:
            ...     print("Comment deleted successfully")
            
            >>> # Get comments first, then delete one
            >>> comments = client.get_settlement_comments("zz1j0agbbp50rfkCFAATS2", company_id="TMS2")
            >>> if comments:
            ...     client.delete_comment(comments[0]['id'], company_id="TMS2")
        """
        comment_id_str = str(comment_id)
        endpoint = f"/comments/{comment_id_str}"
        
        # Set Accept header to text/plain as per API docs
        headers = {
            "Accept": "text/plain"
        }
        
        try:
            response = self.delete(endpoint, company_id=company_id, headers=headers)
            # DELETE typically returns 200 or 204 on success
            # Response is text/plain according to docs
            return response.status_code in (200, 204)
        except Exception as e:
            # If we get an exception, deletion likely failed
            raise Exception(f"Failed to delete comment {comment_id_str}: {e}")
    
    def get_available_charge_codes(self, use_cache: bool = True, cache_hours: int = 24, 
                                  company_id: Optional[str] = None) -> List[Dict]:
        """
        Get available charge codes with simple caching.
        
        Args:
            use_cache: Use cached data if available and valid (default: True) 
            cache_hours: Hours before cache expires (default: 24)
            company_id: Override Company ID for this request (optional)
            
        Returns:
            List of charge code objects
            
        Examples:
            >>> charge_codes = client.get_available_charge_codes()
            >>> charge_codes = client.get_available_charge_codes(use_cache=False)  # force fresh
        """
        company = company_id or os.getenv('TMS_COMPANY_ID', 'TMS')
        
        # Check cache
        if use_cache and company in self._charge_codes_cache:
            cache_data = self._charge_codes_cache[company]
            cache_time = datetime.fromisoformat(cache_data['timestamp'])
            if datetime.now() < cache_time + timedelta(hours=cache_hours):
                return cache_data['codes']
        
        # Fetch from API
        charge_codes = self.get_json("/otherCharges/codes", company_id=company_id)
        codes_list = charge_codes if isinstance(charge_codes, list) else []
        
        # Cache result
        self._charge_codes_cache[company] = {
            'codes': codes_list,
            'timestamp': datetime.now().isoformat()
        }
        
        return codes_list
    
    def refresh_charge_codes_cache(self, company_id: Optional[str] = None) -> bool:
        """Force refresh charge codes from API."""
        try:
            self.get_available_charge_codes(use_cache=False, company_id=company_id)
            return True
        except Exception:
            return False
    
    def upload_image_to_history(self, row_type: str, row_id: str, document_type_id: str, 
                               image_file: Union[str, bytes, Any], movement_id: Optional[str] = None, 
                               company_id: Optional[str] = None) -> str:
        """
        Upload an image to the TMS object history (staging area).
        
        Note: This uploads images to the object history/staging area. To move images from 
        history to the main imaging area, you need access to the "Import to Imaging" 
        service in McLeod TMS.
        
        Args:
            row_type: Type of record (use RowTypes constants: O, M, C, L, P, D, T, E, U)
            row_id: ID of the record to associate the image with
            document_type_id: ID of the document type
            image_file: File-like object, file path string, or binary data to upload
            movement_id: ID of the movement associated with the row (optional)
            company_id: Override Company ID for this request (optional)
            
        Returns:
            String containing batch ID for the staged upload
            
        Examples:
            >>> # Upload from file path
            >>> batch_id = client.upload_image_to_history(RowTypes.ORDER, "12345", "7", "/path/to/image.jpg")
            
            >>> # Upload from open file
            >>> with open("invoice.pdf", "rb") as f:
            ...     batch_id = client.upload_image_to_history(RowTypes.ORDER, "12345", "7", f)
            
            >>> # Upload with movement ID
            >>> batch_id = client.upload_image_to_history(RowTypes.ORDER, "12345", "7", "image.png", 
            ...                                          movement_id="MOV123")
            
            >>> # Upload binary data directly
            >>> with open("doc.pdf", "rb") as f:
            ...     data = f.read()
            >>> batch_id = client.upload_image_to_history(RowTypes.ORDER, "12345", "7", data)
        """
        # Build endpoint URL
        endpoint = f"/images/{row_type}/{row_id}/{document_type_id}"
        
        # Build query parameters
        params = {}
        if movement_id:
            params['movementId'] = movement_id
        
        # Prepare binary data for upload (raw data, not multipart)
        if isinstance(image_file, str):
            # File path string - read the file
            with open(image_file, 'rb') as f:
                data = f.read()
        elif hasattr(image_file, 'read'):
            # File-like object - read the content
            data = image_file.read()
        else:
            # Assume it's already binary data
            data = image_file
        
        # API expects raw binary data in request body with proper Content-Type header
        # Determine content type based on file content magic bytes
        content_type = 'application/pdf'  # Default to PDF
        if data.startswith(b'%PDF'):
            content_type = 'application/pdf'
        elif data.startswith(b'\xFF\xD8\xFF'):
            content_type = 'image/jpeg'
        elif data.startswith(b'\x89PNG'):
            content_type = 'image/png'
        elif data.startswith(b'GIF8'):
            content_type = 'image/gif'
        elif data.startswith(b'BM'):
            content_type = 'image/bmp'
        elif data[:4] in [b'II*\x00', b'MM\x00*']:
            content_type = 'image/tiff'
        
        # Send raw binary data in request body with proper Content-Type header
        headers = {'Content-Type': content_type}
        response = self.post(endpoint, company_id=company_id, params=params, data=data, headers=headers)
        
        # Return the response as text (batch ID for staged upload)
        return response.text
    
    def update_load(self, order_json: Dict[str, Any], company_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Update a load with the provided order JSON.
        
        This sends the complete order JSON to the PUT /orders/update endpoint.
        Useful for modifying reference numbers, stops, charges, or any other order data.
        
        Args:
            order_json: Complete RowOrders JSON object with modifications
            company_id: Override Company ID for this request (optional)
            
        Returns:
            Updated RowOrders object from the API
            
        Raises:
            Exception: If the update fails
            
        Examples:
            >>> # Get current order
            >>> order = client.get_load_json("5225506")
            >>> 
            >>> # Modify reference numbers
            >>> order['reference_number'] = "NEW-REF-123"
            >>> order['customer_reference_number'] = "CUST-REF-456"
            >>> 
            >>> # Update the order
            >>> updated = client.update_load(order)
            >>> print(f"Updated order {updated['id']}")
            
            >>> # Modify and update in different company
            >>> order = client.get_load_json("5225506", company_id="TMS2")
            >>> order['reference_number'] = "NEW-REF-123"
            >>> updated = client.update_load(order, company_id="TMS2")
        """
        headers = {
            "Content-Type": "application/json", 
            "Accept": "application/json"
        }
        
        response = self.put("/orders/update", json=order_json, headers=headers, company_id=company_id)
        return response.json()

    def add_charge(self, order_id: str, charge_id: str, description: str, amount: float,
                   units: float = 1.0, calc_method: str = "F", company_id: Optional[str] = None) -> bool:
        """
        Add a charge to an order using the working pattern from successful implementation.
        
        This follows the proven approach: load full current order, add minimal charge structure,
        send complete order back to API.
        
        Args:
            order_id: ID of the order to add charge to
            charge_id: Charge code (e.g., 'LUM', 'DTU', 'MISC')
            description: Charge description (e.g., 'LUMPER', 'DETENTION')
            amount: Charge amount
            units: Units/quantity (default: 1.0)
            calc_method: Calculation method - 'F' for flat, 'P' for percent (default: 'F')
            company_id: Override Company ID for this request (optional)
            
        Returns:
            True if charge added successfully, False otherwise
            
        Examples:
            >>> # Add a lumper charge
            >>> client.add_charge("5000015", "LUM", "LUMPER", 75.00)
            
            >>> # Add detention charge
            >>> client.add_charge("5000015", "DTU", "DETENTION", 50.00, units=2.0)
            
            >>> # Add misc charge with percent calculation
            >>> client.add_charge("5000015", "MISC", "FUEL SURCHARGE", 25.00, calc_method="P")
        """
        try:
            # Step 1: Validate charge code exists
            available_codes = self.get_available_charge_codes(company_id=company_id)
            valid_charge_ids = [code.get('id') for code in available_codes if code.get('id')]
            
            if charge_id not in valid_charge_ids:
                raise Exception(f"Invalid charge code '{charge_id}'.")
            
            # Step 2: Get the complete current order (this is critical!)
            current_order = self.get_load_json(order_id, company_id=company_id)
            
            # Step 3: Create minimal charge structure (only essential fields)
            new_charge = {
                "__type": "other_charge",
                "__name": "otherCharges",
                "charge_id": charge_id,
                "descr": description,
                "amount": float(amount),
                "units": float(units),
                "rate": float(amount),  # For flat charges, rate = amount
                "calc_method": calc_method
            }
            
            # Step 4: Add new charge to existing charges (no duplicate checking for now)
            existing_charges = current_order.get("otherCharges", [])
            all_charges = existing_charges + [new_charge]
            
            # Step 5: Update the complete order with new charges
            current_order["otherCharges"] = all_charges
            
            # Step 6: Send the FULL order back to the API
            headers = {
                "Content-Type": "application/json", 
                "Accept": "application/json"
            }
            
            response = self.put("/orders/update", json=current_order, headers=headers, company_id=company_id)
            
            if response.status_code == 200:
                return True
            else:
                # Let the calling code handle the error details
                return False
                
        except Exception as e:
            # Re-raise with context for debugging
            raise Exception(f"Failed to add charge to order {order_id}: {e}")

    def search_deductions(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Search pending deductions using flexible table.field criteria.

        This calls the ``/deductions/search`` endpoint and allows passing any
        combination of prefixed fields supported by the API (e.g.,
        ``drs_pending_deduct.movement_id``, ``drs_pending_deduct.ready_to_pay_flag``,
        ``movement.loaded``, ``payee.id``).

        Args:
            filters: Mapping of query keys to values. Keys should include the
                proper table/field prefix as required by the API
                (for example: {"drs_pending_deduct.movement_id": "1180935"}).
                Supported prefixes:
                - drs_pending_deduct: Use `drs_pending_deduct` or no prefix
                - movement: Use `movement` prefix
                - payee: Use `payee` prefix
            company_id: Optional override for Company ID header.
            order_by: Optional order by expression. Multiple columns may be
                provided as a comma-delimited string per API docs.
                Format: prefix.field+direction, prefix.field+direction
                Default: drs_pending_deduct.transaction_date+DESC
            record_length: Optional page size.
            record_offset: Optional page offset (ignored if auto_paginate is True).
            auto_paginate: When True, automatically fetches all pages by incrementing
                record_offset until no more results are returned.

        Returns:
            List of RowDrsPendingDeduct objects returned by the search.

        Examples:
            >>> # Search deductions by movement ID
            >>> client.search_deductions({"drs_pending_deduct.movement_id": "1180935"})
            
            >>> # Search deductions ready to pay for loaded movements
            >>> client.search_deductions({
            ...     "drs_pending_deduct.ready_to_pay_flag": "Y",
            ...     "movement.loaded": "L"
            ... })
            
            >>> # Search with custom sorting
            >>> client.search_deductions(
            ...     {"drs_pending_deduct.payee_id": "*"},
            ...     order_by="drs_pending_deduct.transaction_date+DESC"
            ... )
            
            >>> # Search with auto-pagination to get ALL results
            >>> all_deductions = client.search_deductions(
            ...     {"drs_pending_deduct.payee_id": "*"},
            ...     auto_paginate=True
            ... )
        """
        # Auto-pagination using offset-based pagination
        if auto_paginate:
            all_rows: List[Dict[str, Any]] = []
            page_size = int(record_length) if record_length is not None else 100
            max_pages = 1000  # Safety limit (100,000 records max)
            offset = 0
            
            for page_num in range(1, max_pages + 1):
                page_results = self.search_deductions(
                    filters=filters,
                    company_id=company_id,
                    order_by=order_by,
                    record_length=page_size,
                    record_offset=offset,
                    auto_paginate=False,  # Prevent recursion
                )
                
                if not page_results or len(page_results) == 0:
                    break
                
                all_rows.extend(page_results)
                
                # If we got fewer results than requested, we're done
                if len(page_results) < page_size:
                    break
                
                offset += page_size
            
            return all_rows
        
        # Single-page request (no auto-pagination)
        params: Dict[str, Any] = dict(filters or {})

        # Sorting and pagination
        if order_by:
            params["orderBy"] = order_by
        if record_length is not None:
            params["recordLength"] = int(record_length)
        if record_offset is not None:
            params["recordOffset"] = int(record_offset)

        results = self.get_json("/deductions/search", company_id=company_id, params=params)
        return results if isinstance(results, list) else []

    def search_deductions_history(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Search deduction history (processed/paid deductions) using flexible table.field criteria.

        This calls the ``/deductions/history`` endpoint and allows passing any
        combination of prefixed fields supported by the API. Unlike pending deductions,
        history deductions have been processed and include payment information like
        check_date, check_number, and process_status.

        ⚠️ **IMPORTANT**: This endpoint requires Basic Authentication (username/password)
        and does NOT accept API key authentication. This is a server-side limitation
        of the McLeod TMS API. If you initialize the client with an API key, this
        function will raise a clear error message explaining the requirement.

        Args:
            filters: Mapping of query keys to values. Keys should include the
                proper table/field prefix as required by the API
                (for example: {"drs_deduct_hist.movement_id": "1180935"}).
                Supported prefixes:
                - drs_deduct_hist: Use `drs_deduct_hist` or no prefix
                - movement: Use `movement` prefix
                - payee: Use `payee` prefix
            company_id: Optional override for Company ID header.
            order_by: Optional order by expression. Multiple columns may be
                provided as a comma-delimited string per API docs.
                Format: prefix.field+direction, prefix.field+direction
                Default: drs_deduct_hist.transaction_date+DESC
            record_length: Optional page size.
            record_offset: Optional page offset (ignored if auto_paginate is True).
            auto_paginate: When True, automatically fetches all pages by incrementing
                record_offset until no more results are returned.

        Returns:
            List of RowDrsDeductHist objects returned by the search.

        Raises:
            Exception: If authentication fails with API key, provides a helpful error
                message explaining that Basic Auth is required.

        Examples:
            >>> # Search deduction history by movement ID (requires username/password)
            >>> client = TMSClient("username", "password")  # Not api_key!
            >>> client.search_deductions_history({"drs_deduct_hist.movement_id": "1180935"})
            
            >>> # Search by payee and transaction date
            >>> client.search_deductions_history({
            ...     "drs_deduct_hist.payee_id": "SHERTUCA",
            ...     "drs_deduct_hist.transaction_date": ">=t-30"
            ... })
            
            >>> # Search with custom sorting
            >>> client.search_deductions_history(
            ...     {"drs_deduct_hist.payee_id": "SHERTUCA"},
            ...     order_by="drs_deduct_hist.transaction_date+DESC"
            ... )
        """
        # Auto-pagination using offset-based pagination
        if auto_paginate:
            all_rows: List[Dict[str, Any]] = []
            page_size = int(record_length) if record_length is not None else 100
            max_pages = 1000  # Safety limit (100,000 records max)
            offset = 0
            
            for page_num in range(1, max_pages + 1):
                page_results = self.search_deductions_history(
                    filters=filters,
                    company_id=company_id,
                    order_by=order_by,
                    record_length=page_size,
                    record_offset=offset,
                    auto_paginate=False,  # Prevent recursion
                )
                
                if not page_results or len(page_results) == 0:
                    break
                
                all_rows.extend(page_results)
                
                # If we got fewer results than requested, we're done
                if len(page_results) < page_size:
                    break
                
                offset += page_size
            
            return all_rows
        
        # Single-page request (no auto-pagination)
        params: Dict[str, Any] = dict(filters or {})

        # Sorting and pagination
        if order_by:
            params["orderBy"] = order_by
        if record_length is not None:
            params["recordLength"] = int(record_length)
        if record_offset is not None:
            params["recordOffset"] = int(record_offset)

        # Note: The endpoint is /deductions/history (not /deductions/history/search)
        # IMPORTANT: This endpoint may require Basic Auth instead of API key
        # If API key auth fails, we'll catch and provide a helpful error
        try:
            results = self.get_json("/deductions/history", company_id=company_id, params=params)
            return results if isinstance(results, list) else []
        except Exception as e:
            error_msg = str(e)
            # Check if it's a 401 auth error and we're using API key
            if "401" in error_msg and self.api_key:
                raise Exception(
                    f"The /deductions/history endpoint requires Basic Authentication (username/password), "
                    f"not API key authentication. Please initialize TMSClient with username and password "
                    f"instead of api_key to use this endpoint. Original error: {error_msg}"
                )
            # Re-raise other errors as-is
            raise

    def search_deductions_by_movement(
        self,
        movement_id: Union[str, int],
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        include_history: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Search pending deductions by movement ID, with optional fallback to history.

        This is a convenience method that searches for pending deductions
        associated with a specific movement ID. If no pending deductions are found
        and `include_history=True`, it will also search deduction history.

        Args:
            movement_id: The movement ID to search for (e.g., "1180935" or 1180935)
            company_id: Optional override for Company ID header.
            order_by: Optional order by expression.
                Default: drs_pending_deduct.transaction_date+DESC
            include_history: If True and no pending deductions found, also search
                deduction history for processed/paid deductions.

        Returns:
            List of deduction objects (RowDrsPendingDeduct or RowDrsDeductHist) for
            the specified movement. If history is included, the list may contain
            both pending and history deductions.

        Examples:
            >>> # Get deductions for a movement (pending only)
            >>> deductions = client.search_deductions_by_movement("1180935", include_history=False)
            >>> for d in deductions:
            ...     print(f"Deduction: {d.get('id')} - ${d.get('amount', 0)}")
            
            >>> # Get deductions including history (fallback if no pending)
            >>> deductions = client.search_deductions_by_movement("1180935", include_history=True)
            
            >>> # Get deductions from TMS2
            >>> deductions = client.search_deductions_by_movement(1180935, company_id="TMS2")
        """
        # First try pending deductions
        pending = self.search_deductions(
            filters={"drs_pending_deduct.movement_id": str(movement_id)},
            company_id=company_id,
            order_by=order_by,
        )
        
        # If we found pending deductions, return them
        if pending:
            return pending
        
        # If no pending and history is requested, try history
        if include_history:
            history = self.search_deductions_history(
                filters={"drs_deduct_hist.movement_id": str(movement_id)},
                company_id=company_id,
                order_by=order_by,
            )
            return history
        
        return []

    def search_settlement_history(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Search settlement history using flexible table.field criteria.

        This endpoint returns settlements that have been paid/processed, including
        payment details like check_number, pay_date, and total_pay.

        Args:
            filters: Dictionary of filter criteria. Supports the following prefixes:
                - drs_settle_hist: Use `drs_settle_hist` or no prefix (e.g., movement_id, payee_id, pay_date)
                - movement: Use `movement` prefix
                - payee: Use `payee` prefix
            company_id: Optional override for Company ID header.
            order_by: Optional order by expression. Multiple columns may be
                provided as a comma-delimited string.
                Format: prefix.field+direction, prefix.field+direction
                Default: drs_settle_hist.transfer_date+DESC
            record_length: Optional page size.
            record_offset: Optional page offset (ignored if auto_paginate is True).
            auto_paginate: When True, automatically fetches all pages.

        Returns:
            List of drs_settle_hist objects with nested movement, payee, and
            pending_deductions (historical deductions) data.

        Examples:
            >>> # Check if a movement has been paid
            >>> history = client.search_settlement_history(
            ...     {"drs_settle_hist.movement_id": "1234721"},
            ...     company_id="TMS2"
            ... )
            >>> if history:
            ...     record = history[0]
            ...     print(f"Paid on: {record['pay_date']}")
            ...     print(f"Check #: {record['check_number']}")
            ...     print(f"Total: ${record['total_pay']}")
            
            >>> # Search by payee
            >>> history = client.search_settlement_history(
            ...     {"drs_settle_hist.payee_id": "JSDHMACA"},
            ...     company_id="TMS2"
            ... )
            
            >>> # Search recent payments (last 7 days)
            >>> history = client.search_settlement_history(
            ...     {"drs_settle_hist.pay_date": ">=t-7", "movement.loaded": "L"},
            ...     company_id="TMS2"
            ... )
        """
        # Auto-pagination
        if auto_paginate:
            all_rows: List[Dict[str, Any]] = []
            page_size = int(record_length) if record_length is not None else 100
            max_pages = 1000
            offset = 0
            
            for _ in range(max_pages):
                page_results = self.search_settlement_history(
                    filters=filters,
                    company_id=company_id,
                    order_by=order_by,
                    record_length=page_size,
                    record_offset=offset,
                    auto_paginate=False,
                )
                
                if not page_results:
                    break
                
                all_rows.extend(page_results)
                
                if len(page_results) < page_size:
                    break
                
                offset += page_size
            
            return all_rows
        
        # Single-page request
        params: Dict[str, Any] = dict(filters or {})

        if order_by:
            params["orderBy"] = order_by
        if record_length is not None:
            params["recordLength"] = int(record_length)
        if record_offset is not None:
            params["recordOffset"] = int(record_offset)

        results = self.get_json("/settlements/history/search", company_id=company_id, params=params)
        return results if isinstance(results, list) else []

    def is_movement_paid(
        self,
        movement_id: Union[str, int],
        company_id: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Check if a movement has been paid by looking up settlement history.

        This is the cleanest way to confirm payment status for a movement.
        Returns the settlement history record if paid, None if not yet paid.

        Args:
            movement_id: The movement ID to check (e.g., "1234721" or 1234721)
            company_id: Optional override for Company ID header.

        Returns:
            If paid: Dictionary with payment details including:
                - pay_date: When the payment was made
                - check_number: The check/wire reference number
                - total_pay: Total amount paid
                - is_void: Whether the payment was voided
                - payee_id: The carrier/payee ID
                - movement: Nested movement details
                - payee: Nested payee details
                - pending_deductions: Historical deductions for this settlement
            If not paid: None

        Examples:
            >>> # Check if movement 1234721 has been paid
            >>> payment = client.is_movement_paid("1234721", company_id="TMS2")
            >>> if payment:
            ...     print(f"✓ PAID on {payment['pay_date']}")
            ...     print(f"  Check #: {payment['check_number']}")
            ...     print(f"  Amount: ${payment['total_pay']}")
            ... else:
            ...     print("✗ Not yet paid")
            
            >>> # Use in conditional logic
            >>> if client.is_movement_paid(movement_id):
            ...     print("Movement has been settled")
            ... else:
            ...     print("Movement is still pending payment")
        """
        history = self.search_settlement_history(
            filters={"drs_settle_hist.movement_id": str(movement_id)},
            company_id=company_id,
        )
        
        if history:
            # Return the first (and typically only) record
            record = history[0]
            # Check if voided
            if record.get("is_void"):
                return None
            return record
        
        return None

    def close(self) -> None:
        """Close the session."""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Example usage
if __name__ == "__main__":
    # Create a client instance
    # In production, you should get these from secure storage or environment variables
    
    # Option 1: Username/password authentication
    try:
        with TMSClient("your_username", "your_password") as client:
            # Example API call - adjust endpoint based on actual API
            # response = client.get('/some/endpoint')
            print("TMS Client initialized successfully!")
            print(f"Using Basic Auth for user: {client.username}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Option 2: API key authentication
    try:
        with TMSClient(api_key="your-api-key") as client:
            # Example API call
            # response = client.get('/some/endpoint')
            print("TMS Client initialized successfully with API key!")
    except Exception as e:
        print(f"Error: {e}")
