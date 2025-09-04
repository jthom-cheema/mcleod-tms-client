"""Type stubs for tms_client module."""

from typing import Optional, Dict, Any, Union, List
import requests
from pathlib import Path

class RowTypes:
    """Constants for TMS row types used in various API endpoints."""
    ORDER: str
    MOVEMENT: str
    CUSTOMER: str
    LOCATION: str
    PAYEE: str
    DRIVER: str
    TRACTOR: str
    TRAILER: str
    USER: str

class TMSClient:
    """
    McLeod TMS API client with HTTP Basic Authentication.
    
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
    """
    
    username: str
    password: str
    base_url: str
    basic_auth: str
    session: requests.Session
    
    def __init__(
        self, 
        username: str, 
        password: str, 
        base_url: Optional[str] = None
    ) -> None:
        """
        Initialize the TMS client.
        
        Args:
            username: Username for authentication
            password: Password for authentication  
            base_url: Base URL for the TMS API (defaults to env var TMS_BASE_URL)
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
