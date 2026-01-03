"""Type stubs for tms_client module."""

from typing import Optional, Dict, Any, Union, List
import requests
from pathlib import Path

class RowTypes:
    """Constants for TMS row types used in various API endpoints."""
    ORDER: str
    MOVEMENT: str
    SETTLEMENT: str
    CUSTOMER: str
    LOCATION: str
    PAYEE: str
    DRIVER: str
    TRACTOR: str
    TRAILER: str
    USER: str

class TMSClient:
    """
    McLeod TMS API client with HTTP Basic Authentication or API Key authentication.
    
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
        
        Company switching:
        >>> client.get_json("/orders", company_id="TMS2")
        
        Raw response access:
        >>> response = client.get("/locations/123")
        >>> print(response.status_code)
        >>> data = response.json()
    """
    
    username: Optional[str]
    password: Optional[str]
    base_url: str
    basic_auth: Optional[str]
    api_key: Optional[str]
    api_key_header: Optional[str]
    session: requests.Session
    
    def __init__(
        self, 
        username: Optional[str] = None, 
        password: Optional[str] = None, 
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        api_key_header: str = "Bearer"
    ) -> None:
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
        ...
    
    def get(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> requests.Response:
        """Make a GET request to the API."""
        ...
    
    def post(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> requests.Response:
        """Make a POST request to the API."""
        ...
    
    def put(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> requests.Response:
        """Make a PUT request to the API."""
        ...
    
    def delete(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> requests.Response:
        """Make a DELETE request to the API."""
        ...
    
    def get_json(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Make a GET request and return JSON response.
        
        Args:
            endpoint: API endpoint
            company_id: Override Company ID for this request (optional)
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response
        """
        ...
    
    def get_load_json(
        self,
        order_id: Union[str, int],
        company_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Retrieve the full JSON for an order (load)."""
    
    def post_json(
        self, 
        endpoint: str, 
        data: Optional[Dict[str, Any]] = None,
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
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
        ...

    # Search helpers
    def search_customers(
        self,
        query: str,
        company_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Search for customers by name or ID."""
        ...

    def search_users(
        self,
        query: str,
        company_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Search for users by ID, name, or email address."""
        ...

    def search_locations(
        self,
        query: str,
        company_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Search for locations by code or name."""
        ...

    def search_carriers(
        self,
        query: str,
        company_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Search for carriers by ID or name."""
        ...
    
    def get_carrier_by_code(
        self,
        carrier_code: str,
        company_id: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """Get a carrier profile by its 8-character carrier code."""
        ...
    
    def get_factoring_company(
        self,
        factor_code: str,
        company_id: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """Get factoring company information by factor code using the table row service."""
        ...

    def search_orders(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        changed_after_date: Optional[Union[str, Any]] = None,
        changed_after_type: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """Search orders using flexible table.field criteria."""
        ...

    def search_orders_by_bol(
        self,
        bol_numbers: Union[str, List[str]],
        company_id: Optional[str] = None,
        include_full: bool = False,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
    ) -> List[Dict[str, Any]]: ...

    def search_movements(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        changed_after_date: Optional[Union[str, Any]] = None,
        changed_after_type: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
    ) -> List[Dict[str, Any]]: ...

    def search_settlements(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        changed_after_date: Optional[Union[str, Any]] = None,
        changed_after_type: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """Search settlements using flexible table.field criteria."""
        ...

    def get_settlements_on_hold(
        self,
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """Get settlements that are on hold (not ready to pay)."""
        ...

    def update_deduction_status(
        self,
        deduction_id: str,
        status: str,
        company_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Update ready_to_pay_flag for a single deduction. Status: Y=Process, N=Hold, V=Void."""
        ...

    def update_settlement_status(
        self,
        movement_id: Union[str, int],
        status: str,
        company_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Update ready_to_pay_flag for all settlements AND deductions on a movement. Status: Y=Process, N=Hold, V=Void. Returns dict with 'settlements' and 'deductions' lists."""
        ...

    def search_deductions(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """Search pending deductions using flexible table.field criteria."""
        ...

    def search_deductions_history(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """Search deduction history (processed/paid deductions) using flexible table.field criteria."""
        ...

    def search_deductions_by_movement(
        self,
        movement_id: Union[str, int],
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        include_history: bool = True,
    ) -> List[Dict[str, Any]]:
        """Search pending deductions by movement ID, with optional fallback to history."""
        ...

    def search_settlement_history(
        self,
        filters: Dict[str, Any],
        company_id: Optional[str] = None,
        order_by: Optional[str] = None,
        record_length: Optional[int] = None,
        record_offset: Optional[int] = None,
        auto_paginate: bool = False,
    ) -> List[Dict[str, Any]]:
        """Search settlement history (paid/processed settlements) using flexible table.field criteria."""
        ...

    def is_movement_paid(
        self,
        movement_id: Union[str, int],
        company_id: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Check if a movement has been paid by looking up settlement history.
        
        Returns the settlement history record if paid (with pay_date, check_number, total_pay, etc.),
        or None if not yet paid.
        """
        ...
    
    # Image and document methods
    def get_available_images(
        self, 
        row_type: str, 
        row_id: str, 
        company_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get available images for a specific record type and ID."""
        ...
    
    def get_enriched_images(
        self, 
        row_type: str, 
        row_id: str, 
        company_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get available images with enriched document type information."""
        ...
    
    def get_image_pdf(
        self, 
        image_id: str, 
        company_id: Optional[str] = None
    ) -> bytes:
        """Retrieve the image as PDF binary data."""
        ...
    
    def save_image_pdf(
        self, 
        image_id: str, 
        filepath: str, 
        company_id: Optional[str] = None
    ) -> str:
        """Download and save an image as PDF file."""
        ...
    
    def get_image_for_web(
        self, 
        image_id: str, 
        company_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get image data formatted for web response."""
        ...
    
    def get_available_doctypes(
        self, 
        row_type: str, 
        row_id: str, 
        movement_id: Optional[str] = None,
        company_id: Optional[str] = None, 
        use_cache: bool = True
    ) -> Dict[str, Any]:
        """Get available document types for a specific record type and ID."""
        ...
    
    def get_comments(
        self, 
        parent_row_type: str, 
        parent_row_id: Union[str, int], 
        company_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Retrieve comments for a given parent row type and row ID."""
        ...
    
    def get_driver_comments(
        self, 
        driver_id: Union[str, int], 
        company_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Convenience method to get comments for a driver."""
        ...
    
    def get_settlement_comments(
        self, 
        settlement_id: Union[str, int], 
        company_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Convenience method to get comments for a settlement."""
        ...
    
    def create_comment(
        self, 
        parent_row_type: str, 
        parent_row_id: Union[str, int], 
        comment_type_id: str,
        comments: str,
        company_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new comment for a given parent row type and row ID."""
        ...
    
    def create_driver_comment(
        self, 
        driver_id: Union[str, int], 
        comment_type_id: str,
        comments: str,
        company_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Convenience method to create a comment for a driver."""
        ...
    
    def create_settlement_comment(
        self, 
        settlement_id: Union[str, int], 
        comment_type_id: str,
        comments: str,
        company_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Convenience method to create a comment for a settlement."""
        ...
    
    def delete_comment(
        self, 
        comment_id: Union[str, int], 
        company_id: Optional[str] = None
    ) -> bool:
        """Delete a comment by its ID."""
        ...
    
    def get_available_charge_codes(
        self, 
        use_cache: bool = True, 
        cache_hours: int = 24,
        company_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get available charge codes with simple caching."""
        ...
    
    def refresh_charge_codes_cache(
        self, 
        company_id: Optional[str] = None
    ) -> bool:
        """Force refresh charge codes from API."""
        ...
    
    def upload_image_to_history(
        self, 
        row_type: str, 
        row_id: str, 
        document_type_id: str,
        image_file: Union[str, bytes, Any], 
        movement_id: Optional[str] = None,
        company_id: Optional[str] = None
    ) -> str:
        """Upload an image to the TMS object history (staging area)."""
        ...
    
    def update_load(
        self,
        order_json: Dict[str, Any],
        company_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update a load with the provided order JSON."""
        ...
    
    def add_charge(
        self, 
        order_id: str, 
        charge_id: str, 
        description: str, 
        amount: float,
        units: float = 1.0, 
        calc_method: str = "F", 
        company_id: Optional[str] = None
    ) -> bool:
        """Add a charge to an order."""
        ...
    
    def close(self) -> None:
        """Close the HTTP session."""
        ...
    
    def __enter__(self) -> 'TMSClient': ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
