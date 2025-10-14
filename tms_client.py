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
    
    This client uses HTTP Basic Authentication and maintains a stateful session for making API calls.
    Avoids token accumulation by using basic auth for all requests.
    
    Examples:
        Basic usage:
        >>> with TMSClient("username", "password") as client:
        ...     locations = client.get_json("/locations/new")
        ...     orders = client.get_json("/orders", params={'status': 'active'})
        
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
    
    def __init__(self, username: str, password: str, base_url: Optional[str] = None):
        """
        Initialize the TMS client.
        
        Args:
            username: Username for authentication
            password: Password for authentication  
            base_url: Base URL for the TMS API (defaults to env var TMS_BASE_URL)
        """
        self.username = username
        self.password = password
        self.base_url = base_url or os.getenv('TMS_BASE_URL')
        
        if not self.base_url:
            raise ValueError(
                "TMS_BASE_URL must be provided. Options:\n"
                "1. Pass as parameter: TMSClient(username, password, base_url='https://your-domain.com')\n"
                "2. Set environment variable: TMS_BASE_URL=https://your-domain.com\n"
                "3. Create .env file with: TMS_BASE_URL=https://your-domain.com"
            )
            
        # Remove trailing slash if present
        self.base_url = self.base_url.rstrip('/')
        
        # Create base64 encoded basic auth header
        credentials = f"{username}:{password}"
        self.basic_auth = base64.b64encode(credentials.encode()).decode()
        
        # Initialize session
        self.session = requests.Session()
        
        # Cache for doctypes to avoid repeated API calls
        self._doctype_cache: Dict[str, Dict[str, Any]] = {}
        
        # Cache for charge codes (in memory)
        self._charge_codes_cache: Dict[str, Dict[str, Any]] = {}
        
        # Set default headers including basic auth
        self.session.headers.update({
            'User-Agent': 'TMS-Python-Client/1.0',
            'Accept': 'application/json',
            'Authorization': f'Basic {self.basic_auth}',
            'X-com.mcleodsoftware.CompanyID': os.getenv('TMS_COMPANY_ID', 'TMS')
        })
        
        print(f"TMS Client initialized with Basic Auth for user: {username}")
    
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
    username = "your_username"
    password = "your_password"
    
    try:
        with TMSClient(username, password) as client:
            # Example API call - adjust endpoint based on actual API
            # response = client.get('/some/endpoint')
            print("TMS Client initialized successfully!")
            print(f"Using Basic Auth for user: {client.username}")
            
    except Exception as e:
        print(f"Error: {e}")
