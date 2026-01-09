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

## Settlement Search

The client provides flexible settlement search with change tracking:

```python
from tms_client import TMSClient
from datetime import datetime

with TMSClient("username", "password") as client:
    # Get settlements on hold (convenience method)
    on_hold = client.get_settlements_on_hold()
    
    # Search settlements with filters
    settlements = client.search_settlements({
        "settlement.ready_to_pay_flag": "n",
        "movement.loaded": "L"
    })
    
    # Search by payee and ok to pay date
    recent = client.search_settlements({
        "settlement.payee_id": "*",
        "settlement.ok2pay_date": ">=t-7"
    })
    
    # Search with change tracking (string or datetime)
    updated = client.search_settlements(
        {"settlement.loaded": "L"},
        changed_after_date="20251012000000-0700",
        changed_after_type="Add"
    )
    
    # Using datetime object (naive datetimes default to -0700)
    settlements = client.search_settlements(
        {"settlement.ready_to_pay_flag": "n"},
        changed_after_date=datetime(2025, 10, 12, 0, 0, 0),
        changed_after_type="Update",
        order_by="settlement.ok2pay_date+DESC",
        record_length=100,
        record_offset=0
    )
    
    # Get settlements on hold with sorting
    sorted_on_hold = client.get_settlements_on_hold(
        order_by="settlement.ok2pay_date+DESC"
    )
    
    # Update settlement AND deduction status (put on hold)
    result = client.update_settlement_status("1195486", "N", company_id="TMS2")
    print(f"Updated {len(result['settlements'])} settlements, {len(result['deductions'])} deductions")
    
    # Mark ready to process
    result = client.update_settlement_status("1195486", "Y", company_id="TMS2")
    
    # Update a single deduction
    updated = client.update_deduction_status("zz1j7hpdj951c0gCFAATS3", "N", company_id="TMS2")
    
    # Update OK to Pay Date on a settlement (automatically updates deductions/earnings!)
    settlements = client.search_settlements({'movement.id': '1195486'}, company_id='TMS2')
    updated = client.update_settlement_ok2pay_date(
        settlements[0]['id'],
        "01/10/2026",  # or datetime(2026, 1, 10) or "2026-01-10"
        company_id="TMS2"
    )
    # Access settlement fields (backward compatible)
    print(f"OK to Pay Date: {updated.get('ok2pay_date')}")
    # Access new update information
    print(f"Deductions updated: {updated.get('deductions_count', 0)}")
    print(f"Earnings updated: {updated.get('earnings_count', 0)}")
    
    # Update transaction dates explicitly (alternative)
    result = client.update_settlement_transaction_dates(
        movement_id="1195486",
        transaction_date="2026-01-15",
        company_id="TMS2"
    )
```

**Supported Filter Prefixes**: `settlement` (or no prefix), `movement`, `payee`

**Status Values**: `Y` (Process/Ready), `N` (Hold), `V` (Void)

**Note**: `update_settlement_status()` updates both settlements AND all associated deductions for the movement.

**OK to Pay Date**: Use `update_settlement_ok2pay_date()` to change the OK to pay date. This function **automatically updates transaction dates** on all associated deductions and earnings to match the OK to pay date, ensuring consistency. Accepts `datetime`, `MM/DD/YYYY`, `YYYY-MM-DD`, or API format strings.

**Transaction Dates**: Use `update_settlement_transaction_dates()` to explicitly update transaction dates on deductions and earnings without changing the OK to pay date. Accepts `settlement_id` or `movement_id` and any of the date formats above.

## Deductions Search

The client provides flexible deductions search for pending carrier deductions:

```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
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
    movement = deductions[0].get('movement', {}) if deductions else {}
    base_pay = movement.get('override_pay_amt', 0)
    total_deductions = sum(d.get('amount', 0) for d in deductions)
    total_pay = base_pay + total_deductions
    print(f"Base: ${base_pay}, Deductions: ${total_deductions}, Total: ${total_pay}")
```

**Supported Filter Prefixes**: `drs_pending_deduct` (or no prefix), `movement`, `payee`

**Note**: The `search_deductions_by_movement()` function includes an `include_history` parameter (default: `True`) that will automatically search deduction history if no pending deductions are found. This ensures you get deductions even if they've already been processed/paid.

## Deduction History Search

The client also provides a separate function for searching deduction history (processed/paid deductions):

```python
from tms_client import TMSClient

# IMPORTANT: This endpoint requires Basic Auth (username/password), not API key
with TMSClient("username", "password") as client:
    # Search deduction history by movement ID
    history = client.search_deductions_history({
        "drs_deduct_hist.movement_id": "1180935"
    })
    
    # Search by payee and transaction date
    history = client.search_deductions_history({
        "drs_deduct_hist.payee_id": "SHERTUCA",
        "drs_deduct_hist.transaction_date": ">=t-30"
    })
    
    # History deductions include payment information
    for deduction in history:
        print(f"Amount: ${deduction.get('amount', 0)}")
        print(f"Check Date: {deduction.get('check_date')}")
        print(f"Check Number: {deduction.get('check_number')}")
        print(f"Process Status: {deduction.get('process_status')}")
```

**⚠️ Authentication Requirement**: The `/deductions/history` endpoint on McLeod TMS servers requires **Basic Authentication (username/password)** and does not accept API key authentication, even though `/deductions/search` works with API keys. If you initialize the client with an API key, this function will raise a clear error message explaining the requirement.

**Key Differences from Pending Deductions**:
- History deductions have been processed/paid and include payment fields (`check_date`, `check_number`, `is_void`, `process_status`)
- History deductions do not include nested `movement` objects
- History uses `drs_deduct_hist` prefix instead of `drs_pending_deduct`

**Supported Filter Prefixes**: `drs_deduct_hist` (or no prefix), `movement`, `payee`

## Settlement History & Payment Confirmation

The cleanest way to confirm if a movement has been paid:

```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
    # Simple payment check - returns record if paid, None if not
    payment = client.is_movement_paid("1234721", company_id="TMS2")
    
    if payment:
        print(f"✓ PAID on {payment['pay_date']}")
        print(f"  Check #: {payment['check_number']}")
        print(f"  Amount: ${payment['total_pay']}")
    else:
        print("✗ Not yet paid")
    
    # Search settlement history with flexible filters
    history = client.search_settlement_history(
        {"drs_settle_hist.movement_id": "1234721"},
        company_id="TMS2"
    )
    
    # Search by payee
    history = client.search_settlement_history(
        {"drs_settle_hist.payee_id": "JSDHMACA"},
        company_id="TMS2"
    )
    
    # Search recent payments (last 7 days)
    history = client.search_settlement_history(
        {"drs_settle_hist.pay_date": ">=t-7", "movement.loaded": "L"},
        company_id="TMS2"
    )
```

**Key Fields in Settlement History**:
- `pay_date`: When the payment was made
- `check_number`: Check/wire reference number
- `total_pay`: Total amount paid
- `is_void`: Whether the payment was voided
- `movement`: Nested movement details
- `payee`: Nested payee details
- `pending_deductions`: Historical deductions for this settlement

**Supported Filter Prefixes**: `drs_settle_hist` (or no prefix), `movement`, `payee`

## Comments

The client provides functionality to retrieve comments for various record types:

```python
from tms_client import TMSClient, RowTypes

with TMSClient("username", "password") as client:
    # Generic method - works for any row type
    comments = client.get_comments(RowTypes.DRIVER, "BJM01")
    comments = client.get_comments(RowTypes.SETTLEMENT, "zz1ivr5ucal12v8CFAATS3", company_id="TMS2")
    
    # Convenience methods
    driver_comments = client.get_driver_comments("BJM01")
    settlement_comments = client.get_settlement_comments("zz1ivr5ucal12v8CFAATS3", company_id="TMS2")
    
    # Process comments
    for comment in comments:
        print(f"{comment['enteredByUser']['name']}: {comment['comments']}")
        print(f"Type: {comment['commentTypeDescr']['descr']}")
        print(f"Date: {comment['entered_date']}")
```

**Known Parent Row Types**:
- `RowTypes.DRIVER` ("D") - Driver comments
- `RowTypes.SETTLEMENT` ("M") - Settlement/Movement comments

**Response Structure**: Each comment includes basic fields (`id`, `comments`, `entered_date`, etc.), `commentTypeDescr` (comment type details), and `enteredByUser` (full user details).

**Creating Comments**:
```python
from tms_client import TMSClient, RowTypes

with TMSClient("username", "password") as client:
    # Generic method - works for any row type
    comment = client.create_comment(
        RowTypes.SETTLEMENT,
        "zz1ivr5ucal12v8CFAATS3",
        "AP",
        "Payment processed successfully",
        company_id="TMS2"
    )
    
    # Convenience methods
    driver_comment = client.create_driver_comment("BJM01", "GEN", "Driver called in sick")
    settlement_comment = client.create_settlement_comment(
        "zz1j0agbbp50rfkCFAATS2",
        "AP",
        "test comment",
        company_id="TMS2"
    )
    
    print(f"Created comment ID: {comment['id']}")
```

**Note**: The `create_comment()` methods use a minimal payload with only required fields. The API automatically populates `entered_date`, `entered_user_id`, and nested objects like `commentTypeDescr` and `enteredByUser`.

**Deleting Comments**:
```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
    # Delete a comment by ID
    success = client.delete_comment("zz1je0gung90o24CFAATS2", company_id="TMS2")
    if success:
        print("Comment deleted successfully")
    
    # Get comments first, then delete one
    comments = client.get_settlement_comments("zz1jbl5m6vq11soCFAATS3", company_id="TMS2")
    if comments:
        # Find and delete a specific comment
        for comment in comments:
            if comment.get('comments') == "test comment":
                client.delete_comment(comment['id'], company_id="TMS2")
                break
```

**Note**: The `delete_comment()` method requires the `Accept: text/plain` header as specified in the API documentation.

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
    # Get carrier by 8-character code (recommended for exact matches)
    carrier = client.get_carrier_by_code("SUNNTRCA")
    if carrier:
        print(f"Carrier: {carrier.get('name')} (ID: {carrier.get('id')})")
        drs = carrier.get('drsPayee', {})
        print(f"DOT#: {drs.get('dot_number')} | MC#: {drs.get('icc_number')}")
    
    # Search by carrier ID or name (returns list)
    carriers = client.search_carriers("CONSVAWA")
    
    # Search by carrier name
    carriers = client.search_carriers("Swift")
    
    # Search in different company
    carrier = client.get_carrier_by_code("SUNNTRCA", company_id="TMS2")
    carriers = client.search_carriers("CONSVAWA", company_id="TMS2")
    
    # Process results
    for carrier in carriers:
        print(f"Carrier: {carrier.get('name')} (ID: {carrier.get('id')})")
        print(f"MC#: {carrier.get('mc_number')} | DOT#: {carrier.get('dot_number')}")
```

### Factoring Company Search

```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
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
<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>
run_terminal_cmd

### Unposted Billing Records

Search and update unposted billing records (bills that haven't been posted to history yet):

```python
from tms_client import TMSClient

with TMSClient() as client:
    # Search by order ID
    bills = client.search_billing(order_id="5225404", company_id="TMS")
    
    # Search bills ready to process
    ready_bills = client.search_billing(ready_to_process="Y", company_id="TMS2")
    
    # Get a single billing record
    bill = client.get_billing("zz1jas4t3sq180gCFAATS2", company_id="TMS")
    
    # Update Ready to Bill checkbox
    updated = client.update_billing(
        "zz1jas4t3sq180gCFAATS2",
        ready_to_process=True,  # or False, or "Y", or "N"
        company_id="TMS"
    )
    
    # Update Billing User field
    updated = client.update_billing(
        "zz1jas4t3sq180gCFAATS2",
        billing_user_id="cfaa-dsopr",
        company_id="TMS2"
    )
    
    # Update Additional Notes field
    updated = client.update_billing(
        "zz1jas4t3sq180gCFAATS2",
        additional_notes="Special handling required",
        company_id="TMS"
    )
    
    # Update all three fields at once
    updated = client.update_billing(
        "zz1jas4t3sq180gCFAATS2",
        ready_to_process=True,
        billing_user_id="cfaa-jthom",
        additional_notes="Customer requested rush delivery",
        company_id="TMS"
    )
```

**Supported Filters**: `order_id`, `ready_to_process`, `billing_user_id`, `blnum`, `customer_id`, `ship_date`, and many more from the billing table.

**Update Fields**: `update_billing()` supports updating `ready_to_process` (bool/str), `billing_user_id` (str, max 10 chars), and `additional_notes` (str, max 200 chars).

**Note**: Use `search_billing()` for unposted bills. Use `search_billing_history()` for bills that have already been posted.

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
- **Pagination (enforced)**: The client forces `recordLength=100` by default. Single-page calls are trimmed to 100 rows even if the API returns more, so consumers always receive paginated batches. Use `auto_paginate=True` to fetch all records via cursor (`id > last_id`).
- **API quirks**: Some companies (e.g., TMS2) may ignore `recordLength` and return all rows in one response; the client will log a warning. Auto-pagination still returns the full dataset.
- Supports relative date formats: `"t-1"` (yesterday), `"t-100"` (last 100 days)
- Supports comparison operators: `">=t-100"` (greater than or equal to)
- Supports datetime objects and formatted date strings
- Can filter by any `billing_history` table fields as keyword arguments
- Use `include_users=True` and `include_customer=True` to get related records

**Billing History Examples**:
```python
from tms_client import TMSClient

with TMSClient("username", "password") as client:
    # Single page (enforced 100 max). If API sends more, it is trimmed to 100.
    first_page = client.search_billing_history(bill_date="t-1", company_id="TMS")
    print(f"Page size: {len(first_page)}")  # <= 100

    # All pages (cursor-based). Returns every row.
    all_rows = client.search_billing_history(bill_date="t-1", company_id="TMS", auto_paginate=True)
    print(f"Total rows: {len(all_rows)}")

    # Range query also paginates; auto_paginate gets everything.
    range_first_page = client.search_billing_history(bill_date=">=t-30", company_id="TMS")
    range_all = client.search_billing_history(bill_date=">=t-30", company_id="TMS", auto_paginate=True)
```

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