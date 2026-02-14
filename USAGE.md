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

### Payees / Pay-To Address
```python
# Get full payee record (includes pay-to address for checks/payments)
payee = client.get_payee("SUNNTRCA")
if payee:
    # Main address
    print(f"Carrier: {payee.get('name')}")
    print(f"Address: {payee.get('address1')}, {payee.get('city')}, {payee.get('state')}")
    
    # Pay-to address (where checks go - may be factoring company)
    print(f"Pay-To: {payee.get('check_name')}")
    print(f"Check Address: {payee.get('check_address')}")
    print(f"Check City/St/Zip: {payee.get('check_city')}, {payee.get('check_st')} {payee.get('check_zip')}")

# Get payee with contacts included
payee = client.get_payee("SUNNTRCA", include_contacts=True, include_comments=True)

# Convenience method: just the pay-to address fields
pay_to = client.get_payee_pay_to_address("SUNNTRCA")
if pay_to:
    print(f"Make check payable to: {pay_to['name']}")
    print(f"Mail to: {pay_to['address1']}, {pay_to['city']}, {pay_to['state']} {pay_to['zip_code']}")

# Get payee from different company
tms2_payee = client.get_payee("SUNNTRCA", company_id="TMS2")
```

### Customer Lane Rates
```python
# Get all lanes and their most recent rates for a customer
lanes = client.get_customer_lane_rates("HOMEATGA")
print(f"Found {len(lanes)} unique lanes")

# Multiple customers - unified list, one entry per lane with the most recent rate
lanes = client.get_customer_lane_rates(["HOMEATGA", "KRUSTTWA", "LOWEWINC", "DPETMEMO"])
print(f"Found {len(lanes)} unique lanes across all customers")
# If multiple customers have rates on the same lane, only the most recent is returned

# Get only active (non-expired) lanes
active_lanes = client.get_customer_lane_rates("HOMEATGA", include_expired=False)
print(f"Found {len(active_lanes)} active lanes")

# Process results
for lane in lanes[:5]:  # Show first 5
    print(f"{lane['lane_key']} ({lane['customer_id']})")
    print(f"  Rate: ${lane['rate']} ({lane['rate_type']})")
    print(f"  Effective: {lane['effective_date']}")
    print(f"  Expires: {lane['expiration_date'] or 'Open-ended'}")
    print(f"  Status: {'EXPIRED' if lane['is_expired'] else 'ACTIVE'}")
    # Check if lane appears for multiple customers
    if len(lane['customers']) > 1:
        print(f"  Shared by: {lane['customers']}")

# Filter and analyze
active = [l for l in lanes if not l['is_expired']]
expired = [l for l in lanes if l['is_expired']]
print(f"Active: {len(active)}, Expired: {len(expired)}")

# Find highest rate lanes
by_rate = sorted(lanes, key=lambda x: x['rate'], reverse=True)
print(f"Highest rate lane: {by_rate[0]['lane_key']} @ ${by_rate[0]['rate']}")

# Get lanes from different company
tms2_lanes = client.get_customer_lane_rates("HOMEATGA", company_id="TMS2")
```

**Returned Fields**:
| Field | Description |
|-------|-------------|
| `lane_key` | Unique identifier: `origin (code) -> dest (code)` |
| `customer_id` | Customer code this rate belongs to |
| `customers` | List of all customers with rates on this lane |
| `origin_city`, `origin_state`, `origin_value`, `origin_code` | Origin location |
| `dest_city`, `dest_state`, `dest_value`, `dest_code` | Destination location |
| `rate` | Most recent rate amount (float) |
| `rate_type` | F=Flat, M=Per Mile, etc. |
| `effective_date` | When rate became effective (YYYYMMDD) |
| `expiration_date` | When rate expires/expired (YYYYMMDD or None) |
| `is_expired` | Boolean - is rate currently expired? |
| `bill_distance` | Lane miles if available |
| `rate_count` | How many rate entries exist for this lane |

### Lane Average Revenue
```python
from tms_client import TMSClient
from datetime import datetime, timedelta

with TMSClient() as client:
    # Calculate weighted average revenue for a lane over the last 90 days
    end = datetime.now()
    start = end - timedelta(days=90)
    result = client.get_lane_average_revenue("983", "850", start, end)

    print(f"Weighted Average: ${result['weighted_average']:.2f}")
    print(f"Simple Average:   ${result['simple_average']:.2f}")
    print(f"Load Count:       {result['load_count']} (of {result['total_orders']} in range)")
    print(f"Sampled:          {result['sampled']}")
    print(f"Revenue Range:    ${result['min_revenue']:.2f} - ${result['max_revenue']:.2f}")

    # Using YYYYMMDD date strings
    result = client.get_lane_average_revenue("303", "770", "20250101", "20251231")

    # Fetch ALL orders (no sampling) for maximum accuracy
    result = client.get_lane_average_revenue("983", "850", start, end, max_sample=0)

    # Per-load breakdown
    for load in result['loads'][:5]:
        print(f"  Order {load['order_id']}: ${load['revenue']:.2f} "
              f"(freight=${load['freight_charge']:.2f} + acc=${load['accessorial_total']:.2f}) "
              f"del: {load['delivery_date']}")
```

**How It Works**:
- A **lane** is defined by the first 3 digits of origin and destination zip codes
- Searches delivered orders matching `shipper.zip_code` and `consignee.zip_code` with server-side date filtering on `consignee.sched_arrive_early`
- **Revenue per load** = `freight_charge` + qualifying accessorial charges (AIF, BTF, FSC, FUEL, CFS, FSF, FSP, HAZ, SO, STOP, SFC, TM)
- **Weighted average** = `sum(revenue²) / sum(revenue)` — higher-revenue loads count more
- Loads with a `$0 BTF` charge are excluded (charge not yet populated post-delivery)
- Samples up to 60 orders evenly across the date range by default (`max_sample=60`)
- Fetches full order details using 10 concurrent threads (~5s typical)

**Returned Fields**:
| Field | Description |
|-------|-------------|
| `weighted_average` | Weighted average revenue per load |
| `simple_average` | Simple average for reference |
| `load_count` | Number of loads in calculation |
| `total_orders` | Total orders found in date range |
| `sampled` | Whether results are from a sample |
| `loads` | Per-load detail list |

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

# Update settlement AND deduction status - put on hold
result = client.update_settlement_status("1195486", "N", company_id="TMS2")
print(f"Updated {len(result['settlements'])} settlement(s)")
print(f"Updated {len(result['deductions'])} deduction(s)")

# Mark ready to process (pay)
result = client.update_settlement_status("1195486", "Y", company_id="TMS2")

# Update a single deduction directly
updated = client.update_deduction_status("zz1j7hpdj951c0gCFAATS3", "N", company_id="TMS2")

# Update OK to Pay Date on a settlement (automatically updates deductions/earnings too!)
from datetime import datetime

settlements = client.search_settlements({'movement.id': '1195486'}, company_id='TMS2')
settlement_id = settlements[0]['id']

# Using MM/DD/YYYY format - deductions and earnings automatically updated!
updated = client.update_settlement_ok2pay_date(settlement_id, "01/10/2026", company_id="TMS2")

# Access settlement fields (backward compatible)
print(f"Settlement ID: {updated.get('id')}")
print(f"OK to Pay Date: {updated.get('ok2pay_date')}")

# Access new update information
print(f"Deductions updated: {updated.get('deductions_count', 0)}")
print(f"Earnings updated: {updated.get('earnings_count', 0)}")

# Using datetime object
updated = client.update_settlement_ok2pay_date(settlement_id, datetime(2026, 1, 10), company_id="TMS2")

# Using YYYY-MM-DD format
updated = client.update_settlement_ok2pay_date(settlement_id, "2026-01-10", company_id="TMS2")

# Update transaction dates explicitly (alternative to using ok2pay_date)
result = client.update_settlement_transaction_dates(
    movement_id="1195486",
    transaction_date="2026-01-15",
    company_id="TMS2"
)
print(f"Updated {result['deductions_count']} deductions and {result['earnings_count']} earnings")
```

**Supported Filter Prefixes**: `settlement` (or no prefix), `movement`, `payee`

**Status Values for `update_settlement_status()` and `update_deduction_status()`**:
| Value | Status | Description |
|-------|--------|-------------|
| `Y` | Process | Ready to pay |
| `N` | Hold | Not ready to pay |
| `V` | Void | Voided |

**Accepted Date Formats for `update_settlement_ok2pay_date()` and `update_settlement_transaction_dates()`**:
| Format | Example |
|--------|---------|
| `datetime` object | `datetime(2026, 1, 10)` |
| `MM/DD/YYYY` | `"01/10/2026"` |
| `YYYY-MM-DD` | `"2026-01-10"` |
| `YYYYMMDD` | `"20260110"` |
| API format | `"20260110000000-0800"` |

**Important Notes**:
- `update_settlement_status()` updates both settlements AND all associated deductions for the movement.
- `update_settlement_ok2pay_date()` **automatically** updates transaction dates on all deductions and earnings to match the OK to pay date. This ensures consistency across all settlement records.
- `update_settlement_transaction_dates()` allows you to explicitly update transaction dates on deductions and earnings without changing the OK to pay date.

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

**Note**: The `search_deductions_by_movement()` function includes an `include_history` parameter (default: `True`) that will automatically search deduction history if no pending deductions are found.

### Deduction History
```python
# ⚠️ IMPORTANT: This endpoint requires Basic Auth (username/password), not API key
# If using API key, you'll get a 401 error with a helpful message

# Search deduction history (processed/paid deductions)
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
    print(f"Is Void: {deduction.get('is_void')}")
```

**⚠️ Authentication Requirement**: The `/deductions/history` endpoint requires **Basic Authentication (username/password)** and does not accept API key authentication. This is a server-side limitation. If you use an API key, the function will raise a clear error explaining this requirement.

**Key Differences from Pending Deductions**:
- History deductions have been processed/paid and include payment fields
- History deductions do not include nested `movement` objects
- History uses `drs_deduct_hist` prefix instead of `drs_pending_deduct`

**Supported Filter Prefixes**: `drs_deduct_hist` (or no prefix), `movement`, `payee`

### Settlement History & Payment Confirmation
```python
# Simple payment check - returns the most recent *non-void* record if paid, None if not
# (settlement history can contain multiple records if a payment was voided and re-issued)
payment = client.is_movement_paid("1234721", company_id="TMS2")

if payment:
    print(f"✓ PAID on {payment['pay_date']}")
    print(f"  Check #: {payment['check_number']}")
    print(f"  Amount: ${payment['total_pay']}")
else:
    print("✗ Not yet paid")

# Search settlement history with filters
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
    {"drs_settle_hist.pay_date": ">=t-7"},
    company_id="TMS2"
)

# Process results
for record in history:
    print(f"Movement: {record.get('movement_id')}")
    print(f"Pay Date: {record.get('pay_date')}")
    print(f"Check #: {record.get('check_number')}")
    print(f"Total: ${record.get('total_pay', 0)}")
    print(f"Voided: {record.get('is_void')}")
```

**Key Fields**: `pay_date`, `check_number`, `total_pay`, `is_void`, `movement_id`, `payee_id`

**Supported Filter Prefixes**: `drs_settle_hist` (or no prefix), `movement`, `payee`

### Comments
```python
from tms_client import TMSClient, RowTypes

# Get comments for a driver
driver_comments = client.get_driver_comments("BJM01")

# Get comments for a settlement
settlement_comments = client.get_settlement_comments("zz1ivr5ucal12v8CFAATS3", company_id="TMS2")

# Generic method - works for any row type
comments = client.get_comments(RowTypes.DRIVER, "BJM01")
comments = client.get_comments(RowTypes.SETTLEMENT, "zz1ivr5ucal12v8CFAATS3", company_id="TMS2")

# Process comments
for comment in comments:
    print(f"User: {comment['enteredByUser']['name']}")
    print(f"Comment: {comment['comments']}")
    print(f"Type: {comment['commentTypeDescr']['descr']}")
    print(f"Date: {comment['entered_date']}")
    print("---")
```

**Known Parent Row Types**: `RowTypes.DRIVER` ("D"), `RowTypes.SETTLEMENT` ("M")

**Response Fields**: Each comment includes `id`, `comments`, `entered_date`, `entered_user_id`, `comment_type_id`, `commentTypeDescr` (nested), and `enteredByUser` (nested user object).

**Creating Comments**:
```python
# Create a settlement comment
comment = client.create_settlement_comment(
    "zz1j0agbbp50rfkCFAATS2",
    "AP",
    "Payment processed successfully",
    company_id="TMS2"
)

# Create a driver comment
comment = client.create_driver_comment("BJM01", "GEN", "Driver called in sick")

# Generic method - works for any row type
comment = client.create_comment(
    RowTypes.SETTLEMENT,
    "zz1ivr5ucal12v8CFAATS3",
    "AP",
    "test comment",
    company_id="TMS2"
)

print(f"Created comment ID: {comment['id']}")
```

**Note**: The create methods use minimal payloads. The API automatically populates `entered_date`, `entered_user_id`, and nested objects.

**Deleting Comments**:
```python
# Delete a comment by ID
success = client.delete_comment("zz1je0gung90o24CFAATS2", company_id="TMS2")
if success:
    print("Comment deleted successfully")

# Get comments first, then delete one
comments = client.get_settlement_comments("zz1jbl5m6vq11soCFAATS3", company_id="TMS2")
if comments:
    # Find and delete a specific comment
    for comment in comments:
        if comment.get('comment_type_id') == "ACCESSOR" and comment.get('comments') == "test comment":
            client.delete_comment(comment['id'], company_id="TMS2")
            break
```

**Note**: The `delete_comment()` method requires the `Accept: text/plain` header as specified in the API documentation.

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

### Unposted Billing (Billing Records)
```python
from tms_client import TMSClient

# Search unposted bills by order ID
bills = client.search_billing(order_id="5225404", company_id="TMS")

# Search bills ready to process
ready_bills = client.search_billing(ready_to_process="Y", company_id="TMS2")

# Search by billing user
user_bills = client.search_billing(
    billing_user_id="cfaa-dsopr",
    company_id="TMS"
)

# Search with multiple filters
bills = client.search_billing(
    ready_to_process="N",
    ship_date=">=t-30",
    customer_id="ACME",
    company_id="TMS2"
)

# Auto-paginate to get all results
all_bills = client.search_billing(
    ready_to_process="Y",
    company_id="TMS",
    auto_paginate=True
)

# Get a single billing record
bill = client.get_billing(
    "zz1jas4t3sq180gCFAATS2",
    company_id="TMS",
    include_users=True,
    include_customer=True
)

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

# Process results
for bill in bills:
    print(f"Order: {bill.get('order_id')}")
    print(f"Ready to process: {bill.get('ready_to_process')}")
    print(f"Billing user: {bill.get('billing_user_id')}")
    print(f"BOL: {bill.get('blnum')}")
```

**Supported Filters for `search_billing()`**: Any field from the `billing` table, including:
- `order_id`: Order ID (e.g., "5225404" or "5225404*" for wildcard)
- `ready_to_process`: "Y" or "N"
- `billing_user_id`: User ID (e.g., "cfaa-dsopr")
- `blnum`: Bill of Lading number (supports wildcards like "12345*")
- `customer_id`: Customer ID
- `ship_date`: Relative date (e.g., ">=t-30")
- And many more...

**`ready_to_process` Values for `update_billing()`**:
| Value | Description |
|-------|-------------|
| `True` or `"Y"` | Ready to bill (checkbox checked) |
| `False` or `"N"` | Not ready to bill (checkbox unchecked) |

**`additional_notes` Field**:
- Maps to the `addlnotes1` field in the billing table
- Maximum length: 200 characters
- Can be updated alone or with other fields
- Set to `None` or empty string to clear the field

**Note**: `search_billing()` searches unposted bills (bills that haven't been posted to history yet). Use `search_billing_history()` for bills that have already been posted.

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
RowTypes.SETTLEMENT # "M" - Settlement (same as Movement)
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
