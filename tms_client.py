import os
import base64
import requests
from typing import Optional, Dict, Any
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
            raise ValueError("TMS_BASE_URL must be provided either as parameter or environment variable")
            
        # Remove trailing slash if present
        self.base_url = self.base_url.rstrip('/')
        
        # Create base64 encoded basic auth header
        credentials = f"{username}:{password}"
        self.basic_auth = base64.b64encode(credentials.encode()).decode()
        
        # Initialize session
        self.session = requests.Session()
        
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
