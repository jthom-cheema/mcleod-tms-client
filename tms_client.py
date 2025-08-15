import os
import base64
import requests
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class TMSClient:
    """
    A client for interacting with the McLeod TMS API.
    
    This client handles authentication using either HTTP Basic Auth or token-based auth,
    and maintains a stateful session for making API calls.
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
        
        # Initialize session
        self.session = requests.Session()
        
        # Set default headers
        self.session.headers.update({
            'User-Agent': 'TMS-Python-Client/1.0',
            'Accept': 'application/json',
            'X-com.mcleodsoftware.CompanyID': os.getenv('TMS_COMPANY_ID', 'TMS'),
            'X-com.mcleodsoftware.LicensingAgent': os.getenv('TMS_LICENSING_AGENT', 'Digital Freight Matching')
        })
        
        # Authentication token (will be set after login)
        self.token: Optional[str] = None
        
        # Authenticate and get token
        self._authenticate()
    
    def _authenticate(self) -> None:
        """
        Authenticate with the TMS API and obtain a token.
        
        This method first tries to get a token using the /users/login endpoint.
        If successful, it sets up the session to use token-based authentication.
        """
        try:
            # Create basic auth header for login
            credentials = f"{self.username}:{self.password}"
            encoded_credentials = base64.b64encode(credentials.encode()).decode()
            basic_auth_header = f"Basic {encoded_credentials}"
            
            # Login to get token
            login_url = f"{self.base_url}/users/login"
            headers = {
                'Authorization': basic_auth_header,
                'Accept': 'text/plain'
            }
            
            response = requests.post(login_url, headers=headers)
            response.raise_for_status()
            
            # Extract token from response
            self.token = response.text.strip()
            
            # Update session headers to use token authentication
            self.session.headers.update({
                'Authorization': f"Bearer {self.token}"
            })
            
            print(f"Successfully authenticated and obtained token")
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Authentication failed: {e}")
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Make an authenticated request to the TMS API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            endpoint: API endpoint (without base URL)
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
    
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a GET request to the API."""
        return self._make_request('GET', endpoint, **kwargs)
    
    def post(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a POST request to the API."""
        return self._make_request('POST', endpoint, **kwargs)
    
    def put(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a PUT request to the API."""
        return self._make_request('PUT', endpoint, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a DELETE request to the API."""
        return self._make_request('DELETE', endpoint, **kwargs)
    
    def get_json(self, endpoint: str, **kwargs) -> Dict[Any, Any]:
        """
        Make a GET request and return JSON response.
        
        Args:
            endpoint: API endpoint
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response
        """
        response = self.get(endpoint, **kwargs)
        return response.json()
    
    def post_json(self, endpoint: str, data: Optional[Dict] = None, **kwargs) -> Dict[Any, Any]:
        """
        Make a POST request with JSON data and return JSON response.
        
        Args:
            endpoint: API endpoint
            data: Data to send as JSON
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response
        """
        if data is not None:
            kwargs['json'] = data
        response = self.post(endpoint, **kwargs)
        return response.json()
    
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
            print(f"Token obtained: {client.token[:20]}..." if client.token else "No token")
            
    except Exception as e:
        print(f"Error: {e}")
