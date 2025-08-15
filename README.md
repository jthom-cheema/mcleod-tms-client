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
TMS_LICENSING_AGENT=YOUR_LICENSING_AGENT
```

## Usage

```python
from tms_client import TMSClient

# Basic usage
with TMSClient("your_username", "your_password") as client:
    # Make API calls
    response = client.get("/some/endpoint")
    data = client.get_json("/another/endpoint")
```

## Configuration

The client uses these environment variables:
- `TMS_BASE_URL`: Base URL for the TMS API
- `TMS_COMPANY_ID`: Company ID header value  
- `TMS_LICENSING_AGENT`: Licensing agent header value

If no `.env` file exists, you can also pass the base URL directly:
```python
client = TMSClient("username", "password", base_url="https://your-domain.com")
```
