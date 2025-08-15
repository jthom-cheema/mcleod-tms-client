# McLeod TMS Client

Python client for interacting with the McLeod TMS API.

## Setup

1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

2. Create environment configuration:
```bash
# Copy the template and edit with your values
copy env_template .env
# Then edit .env with your actual TMS URL and credentials
```

3. Update `.env` with your actual values:
```
TMS_BASE_URL=https://your-actual-tms-domain.com
TMS_COMPANY_ID=YOUR_COMPANY_ID
```

## Usage

### Basic Examples

```python
from tms_client import TMSClient

# Initialize client (loads from .env)
with TMSClient("username", "password") as client:
    
    # Get JSON data
    locations = client.get_json("/locations")
    orders = client.get_json("/orders", params={'status': 'active'})
    
    # Company switching (TMS vs TMS2)
    tms2_orders = client.get_json("/orders", company_id="TMS2")
    
    # Create new records
    new_location = {
        "name": "ACME Warehouse",
        "address": "123 Main St",
        "city": "Dallas",
        "state": "TX"
    }
    result = client.post_json("/locations", data=new_location)
    
    # Raw response access
    response = client.get("/locations/123")
    if response.status_code == 200:
        data = response.json()
    
    # Custom timeouts and headers
    client.get("/orders", timeout=30, headers={'Custom': 'value'})
```

### Advanced Usage

```python
# Using without context manager
client = TMSClient("username", "password")
try:
    data = client.get_json("/orders")
finally:
    client.close()

# Override base URL
client = TMSClient("user", "pass", base_url="https://custom-domain.com")

# Error handling
try:
    orders = client.get_json("/orders")
except Exception as e:
    print(f"API call failed: {e}")
```

## Configuration

The client uses these environment variables:
- `TMS_BASE_URL`: Base URL for the TMS API
- `TMS_COMPANY_ID`: Company ID header value

If no `.env` file exists, you can also pass the base URL directly:
```python
client = TMSClient("username", "password", base_url="https://your-domain.com")
```
