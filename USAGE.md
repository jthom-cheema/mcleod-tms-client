# McLeod TMS Client Usage Guide

Quick reference for using the McLeod TMS API client in your projects.

## Installation

```bash
pip install mcleod-tms-client
```

## Basic Setup

```python
from mcleod_tms_client import TMSClient, RowTypes

# Option 1: Username/password authentication (recommended)
with TMSClient("username", "password") as client:
    # Your API calls here
    pass

# Option 2: API key authentication
with TMSClient(api_key="your-api-key") as client:
    # Your API calls here
    pass

# Option 3: Pass URL directly
with TMSClient("username", "password", base_url="https://your-domain.com") as client:
    # Your API calls here
    pass

# Option 4: API key with custom header format
with TMSClient(api_key="your-api-key", api_key_header="ApiKey") as client:
    # Your API calls here
    pass
```

## Environment Variables

Create a `.env` file in your project root:
```
TMS_BASE_URL=https://your-tms-server.com/api
TMS_COMPANY_ID=TMS

# Authentication: Use either username/password OR api_key (not both)
TMS_USERNAME=your_username
TMS_PASSWORD=your_password
# TMS_API_KEY=your-api-key
```

**Note**: When installing this package in other projects, the `.env` file is not included for security reasons. You must configure the URL and credentials using one of the methods above.

**API Key Header Formats**: The `api_key_header` parameter supports:
- `"Bearer"` (default): `Authorization: Bearer <api_key>`
- `"ApiKey"`: `Authorization: ApiKey <api_key>`
- `"X-API-Key"`: Custom header `X-API-Key: <api_key>`

## Common Examples

### Orders
```python
# Get orders
orders = client.get_json("/orders")
specific_order = client.get_load_json(5000003)

# Get orders from different company
orders_tms2 = client.get_json("/orders", company_id="TMS2")

# Search by BOL (header field orders.blnum)
bol_hits = client.search_orders_by_bol("64724484")
bol_full = client.search_orders_by_bol(["64724484", "8631328"], include_full=True)
```

### Customers
```python
# Search customers by name
customers = client.search_customers("ACME")

# Search customers by ID
customers = client.search_customers("12345")

# Get all customers
all_customers = client.search_customers("")

# Search in different company
tms2_customers = client.search_customers("ACME", company_id="TMS2")
```

### Carriers
```python
# Get carrier by 8-character code
carrier = client.get_carrier_by_code("SUNNTRCA")
if carrier:
    print(f"Carrier: {carrier.get('name')} (ID: {carrier.get('id')})")
    drs = carrier.get('drsPayee', {})
    print(f"DOT#: {drs.get('dot_number')} | MC#: {drs.get('icc_number')}")

# Search carriers by ID or name (returns list)
carriers = client.search_carriers("CONSVAWA")

# Search carriers by name
carriers = client.search_carriers("Swift")

# Search in different company
tms2_carrier = client.get_carrier_by_code("SUNNTRCA", company_id="TMS2")
tms2_carriers = client.search_carriers("CONSVAWA", company_id="TMS2")

# Process results
for carrier in carriers:
    print(f"Carrier: {carrier.get('name')} (ID: {carrier.get('id')})")
    print(f"MC#: {carrier.get('mc_number')} | DOT#: {carrier.get('dot_number')}")
```

### Factoring Companies
```python
# Get factoring company by factor code
factor = client.get_factoring_company("APEXFOTX")
if factor:
    print(f"Factor: {factor.get('name')} (ID: {factor.get('id')})")
    print(f"Address: {factor.get('address')}")
    print(f"City: {factor.get('city')}, {factor.get('state')} {factor.get('zip_code')}")
    print(f"Phone: {factor.get('phone_number')}")
    print(f"Email: {factor.get('email')}")

# Get factoring company from different company
tms2_factor = client.get_factoring_company("APEXFOTX", company_id="TMS2")

# Check if factoring company exists
factor = client.get_factoring_company("INVALID")
if not factor:
    print("Factoring company not found")
```

### Movements
```python
from datetime import datetime

# Search movements with flexible filters
movements = client.search_movements({
    "destination.state": "AL",
    "movement.status": "P"
})

# Search with change tracking (datetime or string)
recent = client.search_movements(
    {"destination.stop_type": "SO"},
    changed_after_date="20251012000000-0700",
    changed_after_type="Add"
)

# With datetime object (naive defaults to -0700)
movements = client.search_movements(
    {"origin.location_id": "WARE*"},
    changed_after_date=datetime(2025, 10, 12),
    changed_after_type="Update"
)

# With pagination and sorting
page = client.search_movements(
    {"driver.user": "DPR"},
    order_by="movement.id DESC",
    record_length=100,
    record_offset=0
)
```

### Settlements
```python
from datetime import datetime

# Get settlements on hold (convenience method)
settlements = client.get_settlements_on_hold()

# Search settlements with flexible filters
settlements = client.search_settlements({
    "settlement.ready_to_pay_flag": "n",
    "movement.loaded": "L"
})

# Search by payee and ok to pay date
settlements = client.search_settlements({
    "settlement.payee_id": "*",
    "settlement.ok2pay_date": ">=t-7"
})

# Search with change tracking (datetime or string)
recent = client.search_settlements(
    {"settlement.loaded": "L"},
    changed_after_date="20251012000000-0700",
    changed_after_type="Add"
)

# With datetime object (naive defaults to -0700)
settlements = client.search_settlements(
    {"settlement.ready_to_pay_flag": "n"},
    changed_after_date=datetime(2025, 10, 12),
    changed_after_type="Update"
)

# With pagination and sorting
page = client.search_settlements(
    {"settlement.payee_id": "*"},
    order_by="settlement.ok2pay_date+DESC",
    record_length=100,
    record_offset=0
)

# Get settlements on hold with sorting
sorted_on_hold = client.get_settlements_on_hold(
    order_by="settlement.ok2pay_date+DESC"
)

# Process results
for settlement in settlements:
    print(f"Settlement ID: {settlement.get('id')}")
    print(f"Payee: {settlement.get('payee_id')}")
    print(f"Amount: ${settlement.get('amount', 0)}")
```

**Supported Filter Prefixes**: `settlement` (or no prefix), `movement`, `payee`

### Deductions
```python
# Search deductions by movement ID (convenience method)
deductions = client.search_deductions_by_movement("1180935", company_id="TMS2")

# General search with filters
deductions = client.search_deductions({
    "drs_pending_deduct.movement_id": "1180935"
})

# Search deductions ready to pay for loaded movements
deductions = client.search_deductions({
    "drs_pending_deduct.ready_to_pay_flag": "Y",
    "movement.loaded": "L"
})

# Search with custom sorting
deductions = client.search_deductions(
    {"drs_pending_deduct.payee_id": "SHERTUCA"},
    order_by="drs_pending_deduct.transaction_date+DESC"
)

# Auto-paginate to get all results
all_deductions = client.search_deductions(
    {"drs_pending_deduct.payee_id": "SHERTUCA"},
    auto_paginate=True
)

# Calculate total carrier pay for a movement
deductions = client.search_deductions_by_movement("1180935", company_id="TMS2")
if deductions:
    movement = deductions[0].get('movement', {})
    base_pay = movement.get('override_pay_amt', 0)
    total_deductions = sum(d.get('amount', 0) for d in deductions)
    total_pay = base_pay + total_deductions
    print(f"Base: ${base_pay}, Deductions: ${total_deductions}, Total: ${total_pay}")

# Process results
for deduction in deductions:
    print(f"Deduction ID: {deduction.get('id')}")
    print(f"Payee: {deduction.get('payee_id')}")
    print(f"Amount: ${deduction.get('amount', 0)}")
    print(f"Code: {deduction.get('deduct_code_id')}")
    print(f"Description: {deduction.get('short_desc', 'N/A')}")
```

**Supported Filter Prefixes**: `drs_pending_deduct` (or no prefix), `movement`, `payee`

### Images & Documents
```python
# Get available images for an order
images = client.get_available_images(RowTypes.ORDER, "5000003")

# Get enriched images with document type names
enriched = client.get_enriched_images(RowTypes.ORDER, "5000003")

# Download image as PDF
pdf_data = client.get_image_pdf("dta.bol.7.0.5000003")
with open("invoice.pdf", "wb") as f:
    f.write(pdf_data)

# Or save directly
client.save_image_pdf("dta.bol.7.0.5000003", "invoice")

# Upload image to order history
with open("receipt.pdf", "rb") as f:
    batch_id = client.upload_image_to_history(
        RowTypes.ORDER, "5000003", "7", f
    )
```

### Charges
```python
# Get available charge codes
codes = client.get_available_charge_codes()

# Add charge to order
success = client.add_charge(
    order_id="5000003",
    charge_id="LUM", 
    description="LUMPER",
    amount=75.00
)
```

### Billing History
```python
from datetime import datetime, timedelta

# Search by relative date (yesterday)
bills = client.search_billing_history("t-1")

# Search last 100 days
bills = client.search_billing_history("t-100")

# Search with comparison operator
bills = client.search_billing_history(">=t-100")

# Search using datetime object
seven_days_ago = datetime.now() - timedelta(days=7)
bills = client.search_billing_history(seven_days_ago)

# Search with string date
bills = client.search_billing_history("20230401000000-0700")

# Include user and customer details
bills = client.search_billing_history(
    "t-1",
    include_users=True,
    include_customer=True
)

# Search with additional filters (summary bills with BOL pattern)
bills = client.search_billing_history(
    ">=t-100",
    is_summary_bill="Y",
    blnum="12345*",
    ship_date=">=t-100"
)

# Auto-paginate to get all results (API returns max 100 per call)
# Uses cursor-based pagination with 'id' field since offset pagination isn't supported
all_bills = client.search_billing_history("t-1", auto_paginate=True)
print(f"Got {len(all_bills)} total bills (API limitation: 100 per call without pagination)")

# Process results
for bill in bills:
    print(f"Invoice: {bill.get('invoice_no_string')}")
    print(f"Bill Date: {bill.get('bill_date')}")
    print(f"Customer: {bill.get('customer_id')}")
    print(f"Total: ${bill.get('total_charges_n', 0)}")
```

**Note on Pagination**: The billing history endpoint returns a maximum of 100 results per call and does not support offset-based pagination (`recordOffset` is ignored). To retrieve all results, use `auto_paginate=True`, which uses cursor-based pagination with the `id` field to fetch all pages automatically.

### Miscellaneous Billing History
```python
from datetime import datetime, timedelta

# Search by date (past 7 days)
seven_days_ago = datetime.now() - timedelta(days=7)
bills = client.search_misc_billing_history(seven_days_ago)

# Search with string date
bills = client.search_misc_billing_history("20230401000000-0700")

# Include user and customer details
bills = client.search_misc_billing_history(
    bill_date_after=seven_days_ago,
    include_user=True,
    include_customer=True
)

# Process results
for bill in bills:
    print(f"Invoice: {bill['invoice_no_string']}")
    print(f"Customer: {bill['customer_id']}")
    print(f"Total: ${bill['total_charges_n']}")
```

### Web Framework Integration
```python
# Flask example
@app.route('/download/<image_id>')
def download_image(image_id):
    result = client.get_image_for_web(image_id)
    return Response(result['data'], headers=result['headers'])

# FastAPI example  
@app.get('/download/{image_id}')
def download_image(image_id: str):
    result = client.get_image_for_web(image_id)
    return Response(
        result['data'], 
        media_type="application/pdf",
        headers={"Content-Disposition": result['headers']['Content-Disposition']}
    )
```

## Row Types Constants

Use the `RowTypes` class for consistent row type values:

```python
RowTypes.ORDER      # "O" - Order
RowTypes.MOVEMENT   # "M" - Movement  
RowTypes.CUSTOMER   # "C" - Customer
RowTypes.LOCATION   # "L" - Location
RowTypes.PAYEE      # "P" - Payee
RowTypes.DRIVER     # "D" - Driver
RowTypes.TRACTOR    # "T" - Tractor
RowTypes.TRAILER    # "E" - Trailer
RowTypes.USER       # "U" - User
```

## Error Handling

```python
try:
    with TMSClient("user", "pass") as client:
        data = client.get_load_json(123)
except Exception as e:
    print(f"API Error: {e}")
```
