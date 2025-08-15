"""Type stubs for tms_client module."""

from typing import Optional, Dict, Any, Union
import requests

class TMSClient:
    """
    McLeod TMS API client with HTTP Basic Authentication.
    
    Supports company switching between TMS and TMS2 databases.
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
        """Initialize TMS client with credentials."""
        ...
    
    def get(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> requests.Response:
        """GET request to TMS API."""
        ...
    
    def post(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> requests.Response:
        """POST request to TMS API."""
        ...
    
    def put(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> requests.Response:
        """PUT request to TMS API."""
        ...
    
    def delete(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> requests.Response:
        """DELETE request to TMS API."""
        ...
    
    def get_json(
        self, 
        endpoint: str, 
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """GET request returning parsed JSON."""
        ...
    
    def post_json(
        self, 
        endpoint: str, 
        data: Optional[Dict[str, Any]] = None,
        company_id: Optional[str] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """POST request with JSON data returning parsed JSON."""
        ...
    
    def close(self) -> None:
        """Close the HTTP session."""
        ...
    
    def __enter__(self) -> 'TMSClient': ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
