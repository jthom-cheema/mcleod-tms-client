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

# Initialize client with username/password (loads from .env if available)
with TMSClient("username", "password") as client:
    
    # Get JSON data
    locations = client.get_json("/locations")
    orders = client.get_json("/orders", params={'status': 'active'})
    
    # Search customers
    customers = client.search_customers("ACME")
    
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

# Initialize client with API key
with TMSClient(api_key="your-api-key") as client:
    orders = client.get_json("/orders")
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
- `TMS_USERNAME`: Username for authentication (optional if using API key)
- `TMS_PASSWORD`: Password for authentication (optional if using API key)
- `TMS_API_KEY`: API key for authentication (optional if using username/password)

If no `.env` file exists, you can also pass credentials directly:
```python
# Username/password
client = TMSClient("username", "password", base_url="https://your-domain.com")

# API key
client = TMSClient(api_key="your-api-key", base_url="https://your-domain.com")
```

## Movement Search

The client provides flexible movement search with change tracking:

```python
from tms_client import TMSClient
from datetime import datetime

with TMSClient("username", "password") as client:
    # Basic search with table.field filters
    movements = client.search_movements({
        "destination.state": "AL",
        "destination.stop_type": "SO",
        "movement.status": "P"
    })
    
    # Search with change tracking (string or datetime)
    recent = client.search_movements(
        {"destination.driver_load_unload": "DRP"},
        changed_after_date="20251012000000-0700",
        changed_after_type="Add"
    )
    
    # Using datetime object (naive datetimes default to -0700)
    updated = client.search_movements(
        {"origin.location_id": "WARE*"},
        changed_after_date=datetime(2025, 10, 12, 0, 0, 0),
        changed_after_type="Update",
        order_by="movement.id DESC",
        record_length=100,
        record_offset=0
    )
```

**Supported Filter Prefixes**: `movement` (or no prefix), `origin`, `destination`, `driver`, `driver2`, `tractor`, `trailer`, `trailer2`, `trailer3`

## Image Upload

The client provides functionality to upload images to McLeod TMS object history:

```python
from tms_client import TMSClient, RowTypes

with TMSClient("username", "password") as client:
    # Upload from file path
    batch_id = client.upload_image_to_history(
        row_type=RowTypes.ORDER,
        row_id="12345", 
        document_type_id="7",  # Use get_available_doctypes() to find valid IDs
        image_file="/path/to/invoice.pdf"
    )
    
    # Upload from file object
    with open("receipt.jpg", "rb") as f:
        batch_id = client.upload_image_to_history(
            row_type=RowTypes.ORDER,
            row_id="12345",
            document_type_id="5", 
            image_file=f
        )
    
    # Upload with movement ID
    batch_id = client.upload_image_to_history(
        row_type=RowTypes.ORDER,
        row_id="12345",
        document_type_id="1",
        image_file="proof_of_delivery.pdf",
        movement_id="456789"
    )
    
    # Get available document types
    doctypes = client.get_available_doctypes(RowTypes.ORDER, "12345")
    for doctype in doctypes:
        print(f"ID: {doctype['id']} - {doctype['description']}")
```

**Important Note**: `upload_image_to_history()` uploads images to the object history/staging area. To move images from history to the main imaging area where they appear in loads, you need access to the "Import to Imaging" service in McLeod TMS. Contact McLeod support to enable this service.

## Charge Management

The client provides functionality to manage charges on orders with automatic validation:

```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
    # Get available charge codes (cached for 24 hours)
    charge_codes = client.get_available_charge_codes()
    print(f"Available codes: {len(charge_codes)}")
    
    # Add charges to an order (validates charge codes automatically)
    try:
        # Basic lumper charge
        success = client.add_charge("12345", "LUM", "LUMPER", 75.00)
        
        # Detention charge with units
        success = client.add_charge("12345", "DTU", "DETENTION", 50.00, units=2.0)
        
        # Fuel surcharge with percentage calculation
        success = client.add_charge("12345", "FSC", "FUEL SURCHARGE", 10.00, calc_method="P")
        
    except Exception as e:
        print(f"Failed to add charge: {e}")
    
    # Force refresh charge codes cache
    client.refresh_charge_codes_cache()
    
    # Get charge codes for different company
    tms2_codes = client.get_available_charge_codes(company_id="TMS2")
```

**Charge Code Validation**: The `add_charge()` function automatically validates charge codes against the API. Invalid codes will raise an exception with a helpful error message.

## Search Functions

The client provides search functionality for customers, users, and locations:

### Customer Search

```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
    # Search customers by name
    customers = client.search_customers("ACME")
    
    # Search customers by ID
    customers = client.search_customers("12345")
    
    # Get all customers (empty query)
    all_customers = client.search_customers("")
    
    # Search in different company
    tms2_customers = client.search_customers("ACME", company_id="TMS2")
    
    # Process results
    for customer in customers:
        print(f"Customer: {customer.get('name')} (ID: {customer.get('id')})")
```

### User Search

```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
    # Search by user ID
    users = client.search_users("cfaa-jthom")
    
    # Search by name
    users = client.search_users("Jack Thompson")
    
    # Search by email
    users = client.search_users("jthompson@teamcheema.com")
    
    # Search with partial ID
    users = client.search_users("cfaa")  # Returns all users starting with "cfaa"
    
    # Process results
    for user in users:
        print(f"User: {user.get('name')} ({user.get('id')})")
        print(f"Email: {user.get('email_address')}")
```

### Location Search

```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
    # Search by location code
    locations = client.search_locations("NYC01")
    
    # Search by location name
    locations = client.search_locations("New York")
    
    # Search in different company
    locations = client.search_locations("LAX", company_id="TMS2")
    
    # Process results
    for location in locations:
        print(f"Location: {location.get('name')} (Code: {location.get('id')})")
```

### Carrier Search

```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
    # Search by carrier ID
    carriers = client.search_carriers("CONSVAWA")
    
    # Search by carrier name
    carriers = client.search_carriers("Swift")
    
    # Search in different company
    carriers = client.search_carriers("CONSVAWA", company_id="TMS2")
    
    # Process results
    for carrier in carriers:
        print(f"Carrier: {carrier.get('name')} (ID: {carrier.get('id')})")
        print(f"MC#: {carrier.get('mc_number')} | DOT#: {carrier.get('dot_number')}")
```

### Freight Billing History Search

```python
from tms_client import TMSClient
from datetime import datetime, timedelta

with TMSClient("username", "password") as client:
    # Search by relative date (yesterday)
    bills = client.search_billing_history("t-1")
    
    # Search last 100 days
    bills = client.search_billing_history("t-100")
    
    # Search with comparison operator
    bills = client.search_billing_history(">=t-100")
    
    # Search using datetime object
    seven_days_ago = datetime.now() - timedelta(days=7)
    bills = client.search_billing_history(seven_days_ago)
    
    # Search using string date
    bills = client.search_billing_history("20230401000000-0700")
    
    # Include user and customer details
    bills = client.search_billing_history(
        "t-1",
        include_users=True,
        include_customer=True
    )
    
    # Auto-paginate to get all results (API returns max 100 per call)
    # Uses cursor-based pagination since offset pagination isn't supported
    all_bills = client.search_billing_history("t-1", auto_paginate=True)
    print(f"Got {len(all_bills)} total bills")
    
    # Search with additional filters (summary bills with BOL pattern)
    bills = client.search_billing_history(
        ">=t-100",
        is_summary_bill="Y",
        blnum="12345*",
        ship_date=">=t-100"
    )
    
    # Process results
    for bill in bills:
        print(f"Invoice: {bill.get('invoice_no_string')}")
        print(f"Bill Date: {bill.get('bill_date')}")
        print(f"Customer: {bill.get('customer_id')}")
        print(f"Total: ${bill.get('total_charges_n', 0)}")
```

**Billing History Search Notes**:
- **Pagination**: The API returns a maximum of 100 results per call and does not support offset-based pagination (`recordOffset` is ignored). Use `auto_paginate=True` to automatically fetch all results using cursor-based pagination with the `id` field. 
- Supports relative date formats: `"t-1"` (yesterday), `"t-100"` (last 100 days)
- Supports comparison operators: `">=t-100"` (greater than or equal to)
- Supports datetime objects and formatted date strings
- Can filter by any `billing_history` table fields as keyword arguments
- Use `include_users=True` and `include_customer=True` to get related records

### Miscellaneous Billing History Search

```python
from tms_client import TMSClient
from datetime import datetime, timedelta

with TMSClient("username", "password") as client:
    # Search using datetime (last 7 days)
    seven_days_ago = datetime.now() - timedelta(days=7)
    bills = client.search_misc_billing_history(seven_days_ago)
    
    # Search using string date
    bills = client.search_misc_billing_history("20230401000000-0700")
    
    # Include user and customer details
    bills = client.search_misc_billing_history(
        bill_date_after=seven_days_ago,
        include_user=True,
        include_customer=True
    )
    
    # Process results
    for bill in bills:
        print(f"Invoice: {bill.get('invoice_no_string')}")
        print(f"Bill Date: {bill.get('bill_date')}")
        print(f"Customer: {bill.get('customer_id')}")
        print(f"Total: ${bill.get('total_charges_n')}")
```

**Search Notes**: All search functions return a list of matching objects. They support partial matching and empty queries may return all records (depending on API configuration).