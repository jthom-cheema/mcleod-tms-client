# Changelog

Update history for the McLeod TMS Client. Each entry includes what was added, where to find examples, and pointers for future development.

---

## [2026-02-09] Customer Lane Rates

### Added
- **`get_customer_lane_rates()`** - Retrieve all lanes and their most recent rates for one or more customers

### What It Does

Consolidates rate headers (`rate` table) and lane details (`orig_dest_rate` table) into a single list where each lane appears once with its most recent rate information. Accepts a single customer code or a list of customer codes - when multiple customers are provided, lanes are unified across all customers.

### Usage

```python
from tms_client import TMSClient

with TMSClient() as client:
    # Single customer
    lanes = client.get_customer_lane_rates("HOMEATGA")
    
    # Multiple customers - unified list
    lanes = client.get_customer_lane_rates(["HOMEATGA", "KRUSTTWA", "LOWEWINC"])
    
    # Get only active (non-expired) lanes
    active_lanes = client.get_customer_lane_rates("HOMEATGA", include_expired=False)
    
    # Process results
    for lane in lanes:
        print(f"{lane['lane_key']}: ${lane['rate']} ({lane['customer_id']})")
        print(f"  Effective: {lane['effective_date']}")
        print(f"  Expires: {lane['expiration_date'] or 'Open-ended'}")
        print(f"  Status: {'EXPIRED' if lane['is_expired'] else 'ACTIVE'}")
        if len(lane['customers']) > 1:
            print(f"  Also on: {lane['customers']}")
```

### Returned Fields
| Field | Description |
|-------|-------------|
| `lane_key` | Unique identifier: `origin (code) -> dest (code)` |
| `customer_id` | Customer code this rate belongs to |
| `customers` | List of all customers with rates on this lane |
| `origin_city`, `origin_state`, `origin_value`, `origin_code` | Origin location details |
| `dest_city`, `dest_state`, `dest_value`, `dest_code` | Destination location details |
| `rate` | Most recent rate amount (float) |
| `rate_type` | F=Flat, M=Per Mile, etc. |
| `rate_id` | Reference to rate header |
| `effective_date` | When rate became effective (YYYYMMDD) |
| `expiration_date` | When rate expires/expired (YYYYMMDD or None) |
| `is_expired` | Boolean - is the rate currently expired? |
| `bill_distance` | Lane miles (if available) |
| `times_used` | How many times this lane rate was used |
| `description` | Rate description/notes |
| `rate_count` | How many rate entries exist for this lane |

### Key Implementation Notes
- Accepts single customer code (str) or list of codes (List[str])
- Uses `TableRowService` to query `rate` and `orig_dest_rate` tables
- For lanes with multiple rate entries, selects the most recent by effective_date
- Expiration check uses current date comparison
- Results sorted alphabetically by lane_key

### See Also
- `examples.py` → `example_customer_lane_rates()`
- `USAGE.md` → Customer Lane Rates section

---

## [2026-01-21] Payee Pay-To Address

### Added
- **`get_payee()`** - Get a payee record by ID with full pay-to address fields
- **`get_payee_pay_to_address()`** - Convenience method to extract just pay-to address info

### What It Does

**`get_payee()`**: Retrieves a full RowPayee record using `GET /payees/{id}`. Returns all payee fields including the pay-to (check) address fields used for carrier payments. Optionally includes related contacts and comments.

**`get_payee_pay_to_address()`**: Extracts just the pay-to address fields from a payee record. Useful when you only need the address where checks/payments should be sent (which may be a factoring company).

### Key Pay-To Fields
- `check_name` - Pay-to name (may be factoring company)
- `check_address` / `check_address2` - Pay-to address lines
- `check_city` / `check_st` / `check_zip` - Pay-to city, state, ZIP

### Usage

```python
from tms_client import TMSClient

with TMSClient() as client:
    # Get full payee record
    payee = client.get_payee("SUNNTRCA")
    if payee:
        print(f"Carrier: {payee.get('name')}")
        print(f"Pay-To: {payee.get('check_name')}")
        print(f"Address: {payee.get('check_address')}")
        print(f"City/St/Zip: {payee.get('check_city')}, {payee.get('check_st')} {payee.get('check_zip')}")
    
    # Get payee with contacts
    payee = client.get_payee("SUNNTRCA", include_contacts=True)
    
    # Convenience method for just pay-to address
    pay_to = client.get_payee_pay_to_address("SUNNTRCA")
    if pay_to:
        print(f"Make check to: {pay_to['name']}")
        print(f"Mail to: {pay_to['address1']}, {pay_to['city']}, {pay_to['state']} {pay_to['zip_code']}")
```

### See Also
- `examples.py` → `example_payee_pay_to_address()`
- API Docs: `docs/index_operation_getPayee_role_-1_service_PayeeService.md`

---

## [2026-01-XX] Billing Record Updates

### Added
- **`search_billing()`** - Search unposted billing records by various criteria
- **`get_billing()`** - Get a single unposted billing record by ID
- **`update_billing()`** - Update `ready_to_process` (Ready to Bill checkbox), `billing_user_id` (Billing User field), and/or `additional_notes` (Additional Notes field)

### What It Does

**`search_billing()`**: Searches the unposted billing table (bills that haven't been posted to history yet). Supports flexible filtering by any billing table fields such as `order_id`, `ready_to_process`, `billing_user_id`, `blnum`, `customer_id`, etc. Includes auto-pagination support to retrieve all results when there may be more than 100 records.

**`get_billing()`**: Retrieves a single unposted billing record by its ID. Useful for getting full details of a specific bill before updating it.

**`update_billing()`**: Updates the "Ready to Bill" checkbox (`ready_to_process`), the "Billing User" field (`billing_user_id`), and/or the "Additional Notes" field (`additional_notes` / `addlnotes1`) on unposted billing records. The `ready_to_process` field accepts both boolean values (True/False) and string values ("Y"/"N"), automatically converting to the correct format. The `additional_notes` field supports up to 200 characters. All other billing fields are preserved during the update.

### Usage

**Search unposted bills:**
```python
from tms_client import TMSClient

with TMSClient() as client:
    # Search by order ID
    bills = client.search_billing(order_id="5225404", company_id="TMS")
    
    # Search bills ready to process
    ready_bills = client.search_billing(ready_to_process="Y", company_id="TMS2")
    
    # Search by billing user
    user_bills = client.search_billing(
        billing_user_id="cfaa-dsopr",
        company_id="TMS"
    )
    
    # Search with multiple filters and auto-pagination
    all_bills = client.search_billing(
        ready_to_process="N",
        ship_date=">=t-30",
        company_id="TMS2",
        auto_paginate=True
    )
```

**Get a single billing record:**
```python
bill = client.get_billing(
    "zz1jas4t3sq180gCFAATS2",
    company_id="TMS",
    include_users=True,
    include_customer=True
)
print(f"Ready to process: {bill.get('ready_to_process')}")
print(f"Billing user: {bill.get('billing_user_id')}")
```

**Update billing records:**
```python
# Mark bill as ready to process
updated = client.update_billing(
    "zz1jas4t3sq180gCFAATS2",
    ready_to_process=True,
    company_id="TMS"
)

# Update billing user
updated = client.update_billing(
    "zz1jas4t3sq180gCFAATS2",
    billing_user_id="cfaa-dsopr",
    company_id="TMS2"
)

# Update additional notes
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

# Uncheck ready to bill using string
updated = client.update_billing(
    "zz1jas4t3sq180gCFAATS2",
    ready_to_process="N",
    company_id="TMS"
)
```

### Key Implementation Notes
- Uses `GET /billing` for searching unposted bills
- Uses `GET /billing/{id}` for retrieving a single bill
- Uses `PUT /billing/update` (BillingService) for updates
- `ready_to_process` accepts both boolean (True/False) and string ("Y"/"N") values
- `billing_user_id` must be a valid user ID (max 10 characters, references users.id)
- `additional_notes` maps to the `addlnotes1` field (VARCHAR(200), max 200 characters)
- All other billing fields are preserved when updating
- Supports auto-pagination for retrieving all results when there may be >100 records

---

## [2026-01-XX] Settlement Transaction Date Updates

### Added
- **`update_settlement_transaction_dates()`** - Update `transaction_date` on all deductions and earnings attached to a settlement
- **Enhanced `update_settlement_ok2pay_date()`** - Now automatically updates transaction dates on deductions and earnings to match the OK to pay date

### What It Does

**`update_settlement_transaction_dates()`**: Updates the `transaction_date` field on all pending deductions (`drs_pending_deduct`) and earnings (`driver_extra_pay`) associated with a settlement. You can provide either a `settlement_id` or `movement_id` to identify the settlement. The transaction date is updated to match the settlement's OK to pay date.

**Enhanced `update_settlement_ok2pay_date()`**: When updating the OK to Pay Date on a settlement, this function now automatically finds and updates all associated deductions and earnings to match the new OK to pay date. This ensures consistency across all settlement-related records. The function is fully backward compatible - existing code will continue to work and automatically benefit from this enhancement.

### Usage

**Update transaction dates explicitly:**
```python
from tms_client import TMSClient
from datetime import datetime

with TMSClient() as client:
    # Update using movement_id
    result = client.update_settlement_transaction_dates(
        movement_id="1195486",
        transaction_date="2026-01-15",
        company_id="TMS2"
    )
    print(f"Updated {result['deductions_count']} deductions and {result['earnings_count']} earnings")
    
    # Update using settlement_id and datetime
    result = client.update_settlement_transaction_dates(
        settlement_id="zz1abc123def",
        transaction_date=datetime(2026, 1, 15),
        company_id="TMS2"
    )
```

**Automatic updates via OK to pay date (recommended):**
```python
from tms_client import TMSClient
from datetime import datetime

with TMSClient() as client:
    # First, find the settlement ID
    settlements = client.search_settlements({'movement.id': '1195486'}, company_id='TMS2')
    settlement_id = settlements[0]['id']
    
    # Update OK to pay date - deductions and earnings automatically updated too!
    updated = client.update_settlement_ok2pay_date(
        settlement_id,
        "01/10/2026",
        company_id="TMS2"
    )
    
    # Access settlement fields (backward compatible)
    print(f"Settlement ID: {updated.get('id')}")
    print(f"OK to Pay Date: {updated.get('ok2pay_date')}")
    
    # Access new update information
    print(f"Deductions updated: {updated.get('deductions_count', 0)}")
    print(f"Earnings updated: {updated.get('earnings_count', 0)}")
```

### Accepted Date Formats
| Format | Example |
|--------|---------|
| `datetime` object | `datetime(2026, 1, 10)` |
| `MM/DD/YYYY` | `"01/10/2026"` |
| `YYYY-MM-DD` | `"2026-01-10"` |
| `YYYYMMDD` | `"20260110"` |
| API format | `"20260110000000-0800"` |

### Key Implementation Notes
- Uses `PUT /settlement/update` for settlement updates
- Uses `PUT /drs_pending_deduct/update` (TableRowService) for deduction updates
- Uses `PUT /driver_extra_pay/update` (TableRowService) for earnings updates
- Defaults to PST timezone (-0800) for naive datetimes to match McLeod's timezone
- Transaction dates are formatted as `YYYYMMDDHHMMSS±ZZZZ` (full datetime with timezone)
- `update_settlement_ok2pay_date()` returns the settlement object with additional fields: `deductions_updated`, `earnings_updated`, `deductions_count`, `earnings_count`
- Fully backward compatible - existing code using `update_settlement_ok2pay_date()` automatically benefits from deduction/earnings updates

---

## [2025-01-XX] Comment Management

### Added
- **`get_comments()`** - Retrieve comments for any parent row type (driver, settlement, etc.)
- **`get_driver_comments()`** - Convenience method to get comments for a driver
- **`get_settlement_comments()`** - Convenience method to get comments for a settlement
- **`create_comment()`** - Create a new comment for any parent row type
- **`create_driver_comment()`** - Convenience method to create a comment for a driver
- **`create_settlement_comment()`** - Convenience method to create a comment for a settlement
- **`delete_comment()`** - Delete a comment by its ID
- **`RowTypes.SETTLEMENT`** - Constant for settlement row type ("M")

### What It Does
**Retrieval**: Retrieves comments associated with various record types using the `GET /comments/{parentRowType}/{parentRowId}` endpoint. Comments include details about who entered them, when they were entered, comment type descriptions, and full user information for the person who created the comment.

**Creation**: Creates new comment records using the `PUT /comments/create` endpoint. Uses minimal payload with only required fields (`__type`, `parent_row_type`, `parent_row_id`, `comment_type_id`, `comments`). The API automatically populates other fields like `entered_date`, `entered_user_id`, and nested objects.

**Deletion**: Deletes comment records using the `DELETE /comments/{id}` endpoint. Requires `Accept: text/plain` header as specified in API documentation. Returns `True` on successful deletion (200/204 status codes).

### Usage
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
    
    # Create comments
    comment = client.create_comment(
        RowTypes.SETTLEMENT,
        "zz1ivr5ucal12v8CFAATS3",
        "AP",
        "Payment processed successfully",
        company_id="TMS2"
    )
    
    # Convenience methods for creating
    driver_comment = client.create_driver_comment("BJM01", "GEN", "Driver called in sick")
    settlement_comment = client.create_settlement_comment(
        "zz1j0agbbp50rfkCFAATS2",
        "AP",
        "test comment",
        company_id="TMS2"
    )
    
    # Delete comments
    success = client.delete_comment("zz1je0gung90o24CFAATS2", company_id="TMS2")
    if success:
        print("Comment deleted successfully")
    
    # Get comments first, then delete one
    comments = client.get_settlement_comments("zz1jbl5m6vq11soCFAATS3", company_id="TMS2")
    if comments:
        client.delete_comment(comments[0]['id'], company_id="TMS2")
```

### Known Parent Row Types
| Type | Code | Constant | Description |
|------|------|----------|-------------|
| Driver | `D` | `RowTypes.DRIVER` | Driver comments |
| Settlement | `M` | `RowTypes.SETTLEMENT` | Settlement/Movement comments |
| *More types to be discovered* | | | |

### Response Structure
Each comment includes:
- **Basic fields**: `id`, `comments`, `entered_date`, `entered_user_id`, `comment_type_id`, `parent_row_id`, `parent_row_type`
- **`commentTypeDescr`**: Nested object with comment type description (`id`, `descr`, `is_active`)
- **`enteredByUser`**: Nested user object with full user details (`id`, `name`, `email_address`, etc.)

### Files Changed
- `tms_client.py` - Added `get_comments()`, `get_driver_comments()`, `get_settlement_comments()`, `create_comment()`, `create_driver_comment()`, `create_settlement_comment()`, `delete_comment()` methods
- `tms_client.pyi` - Added type stubs
- `RowTypes` class - Added `SETTLEMENT` constant
- `README.md` - Added documentation section
- `USAGE.md` - Added usage examples
- `examples.py` - Added example functions
- `tests/test_get_comments.py` - Added test file

### Key Implementation Notes
- **Delete Endpoint**: Requires `Accept: text/plain` header (different from other endpoints that use `application/json`)
- **Delete Response**: Returns `text/plain` response indicating success or failure
- **Delete Status Codes**: Returns `True` for 200 or 204 status codes

### Related Functions
- `RowTypes` constants - Use for consistent row type values

### Future Development
- Discover and document additional parent row types (Order, Customer, Location, etc.)
- Consider adding convenience methods for other common row types as they're discovered

---

## [2025-12-31] Settlement & Deduction Status Updates

### Added
- **`update_settlement_status()`** - Update the `ready_to_pay_flag` for all settlements AND deductions on a movement
- **`update_deduction_status()`** - Update the `ready_to_pay_flag` for a single deduction

### What It Does
Uses `PUT /settlement/update` and `PUT /drs_pending_deduct/update` endpoints to change the process status of pending settlements and their associated deductions. This is the same as changing the status in the McLeod UI.

### Usage
```python
# Put a movement's settlements AND deductions on hold
result = client.update_settlement_status("1195486", "N", company_id="TMS2")
print(f"Updated {len(result['settlements'])} settlement(s)")
print(f"Updated {len(result['deductions'])} deduction(s)")

# Mark ready to process (pay)
result = client.update_settlement_status("1195486", "Y", company_id="TMS2")

# Update a single deduction
updated = client.update_deduction_status("zz1j7hpdj951c0gCFAATS3", "N", company_id="TMS2")
```

### Valid Status Values
| Value | Status | Description |
|-------|--------|-------------|
| `Y` | Process | Ready to pay |
| `N` | Hold | Not ready to pay |
| `V` | Void | Voided |

### How It Works
**`update_settlement_status()`**:
1. Searches for settlements using `movement.id` filter
2. Updates each settlement via `PUT /settlement/update`
3. Searches for deductions using `drs_pending_deduct.movement_id` filter
4. Updates each deduction via `PUT /drs_pending_deduct/update`
5. Returns `{"settlements": [...], "deductions": [...]}`

**`update_deduction_status()`**:
1. Sends minimal PUT payload to `/drs_pending_deduct/update`
2. Returns updated deduction object

### Key Implementation Notes
- **Minimal Payload**: Only `__type`, `id`, and changed field needed
- **Auth**: Works with API key or Basic auth
- **Deductions**: `update_settlement_status()` automatically updates all associated deductions

### Files Changed
- `tms_client.py` - Added functions
- `tms_client.pyi` - Added type stubs
- `README.md` - Added documentation
- `USAGE.md` - Added examples
- `examples.py` - Added example function

### Related Functions
- `search_settlements()` - Find settlements by filters
- `search_deductions()` - Find deductions by filters
- `get_settlements_on_hold()` - Get settlements with `ready_to_pay_flag="N"`

---

## [2026-01-13] Settlement Payment Confirmation Fix

### Fixed
- **`is_movement_paid()`** now checks **all** settlement history rows for a movement and returns the **most recent non-void** record (previously it only inspected the first record, which could be voided).

---

## [2025-12-19] Settlement History & Payment Confirmation

### Added
- **`search_settlement_history()`** - Search paid/processed settlements via `/settlements/history/search`
- **`is_movement_paid()`** - Simple boolean-style check if a movement has been paid

### What It Does
The `/settlements/history/search` endpoint returns settlements that have been paid, including:
- `pay_date` - When payment was made
- `check_number` - Check/wire reference
- `total_pay` - Total amount paid
- `is_void` - Whether payment was voided
- Nested `movement`, `payee`, and `pending_deductions` (historical) objects

### Usage
```python
# Check if a movement is paid
payment = client.is_movement_paid("1234721", company_id="TMS2")
if payment:
    print(f"PAID on {payment['pay_date']}, Check #{payment['check_number']}")
else:
    print("Not yet paid")

# Search settlement history with filters
history = client.search_settlement_history(
    {"drs_settle_hist.movement_id": "1234721"},
    company_id="TMS2"
)
```

### Files Changed
- `tms_client.py` - Added functions (lines ~2076-2220)
- `tms_client.pyi` - Added type stubs
- `README.md` - Added documentation section
- `USAGE.md` - Added usage examples

### Sample Data
- `samples/settlements/settlement_history_1234721.json` - Full paid settlement record
- `samples/settlements/settlement_history_1230166.json` - Another example

### Key Fields in Response
| Field | Description |
|-------|-------------|
| `pay_date` | Payment date (format: `20251126000000-0800`) |
| `check_number` | Check or wire reference (e.g., `D0031923`) |
| `total_pay` | Total payment amount |
| `order_pay` | Order-level pay amount |
| `is_void` | Boolean - whether voided |
| `payee_id` | Carrier/payee ID |
| `movement_id` | Movement ID |
| `order_id` | Order ID |

---

## [2026-01-14] Deductions History Safety Hardening (Correctness-First)

### Changed
- **`search_deductions_history()` is now defensive by default**:
  - Tries `GET /deductions/history/search` first (if the API supports it), then falls back to `GET /deductions/history`.
  - Applies **strict client-side filtering** for simple equality filters (e.g. `movement_id`) and **discards rows missing linkage fields** when a filter is requested (untrusted rows are dropped).
  - Applies `recordLength` / `recordOffset` **in-memory after filtering** (because server-side paging may be ignored).
  - Adds a **hard safety cap**: if the caller requests a bounded page (`record_length` is set) and the API returns an obviously unbounded dataset (currently `> 1000` rows), the client **returns `[]` and logs a warning**. This prevents catastrophic net pay sums from unrelated rows.
- **`search_deductions_by_movement(..., include_history=True)` is bounded**: history fallback requests now include a conservative `record_length` to avoid accidentally pulling huge history datasets on broken servers.

### Added
- **Client-side safety net** for unfilterable history responses (hard cap + strict filtering + in-memory paging).

### Why this exists
- In some McLeod environments, `/deductions/history` behaves as effectively **unfilterable / unbounded** (ignores filters and paging; linkage fields may be missing). Consuming that response blindly can produce **absurd net pay** results. This change makes the client correctness-first: it either returns verified, scoped rows or returns nothing (with a warning).

---

## [2025-12-18] Deductions Search & History

### Added
- **`search_deductions()`** - Search pending deductions via `/deductions/search`
- **`search_deductions_history()`** - Search processed deductions via `/deductions/history`
- **`search_deductions_by_movement()`** - Convenience method with auto-fallback to history

### Known Issues
- **`/deductions/history` requires Basic Auth** - API key authentication is rejected with 401. Must use username/password.
- **Server-side filtering/paging may be ignored** - In some environments `/deductions/history` ignores filters (movement_id, settlement_id, etc.) and may return huge unbounded lists; `recordLength`/`recordOffset` may be ignored in practice. Treat history responses as untrusted unless proven scoped.

### Files Changed
- `tms_client.py` - Added functions
- `tms_client.pyi` - Added type stubs
- `README.md` - Added Deductions Search section
- `USAGE.md` - Added Deductions examples

### Sample Data
- `samples/deductions/deductions_movement_*.json` - Pending deduction samples
- `samples/deductions/deductions_history_*.json` - History samples

### Filter Prefixes
| Endpoint | Prefixes |
|----------|----------|
| `/deductions/search` | `drs_pending_deduct`, `movement`, `payee` |
| `/deductions/history` | `drs_deduct_hist`, `movement`, `payee` |

---

## [2025-12-12] Settlement Search

### Added
- **`search_settlements()`** - Search pending settlements via `/settlements/search`
- **`get_settlements_on_hold()`** - Convenience method for on-hold settlements

### Files Changed
- `tms_client.py` - Added functions
- `README.md` - Added Settlement Search section

### Filter Prefixes
- `settlement` (or no prefix), `movement`, `payee`

---

## Quick Reference: Payment Status Flow

To determine if a movement has been paid:

```python
# RECOMMENDED: Use is_movement_paid() - cleanest approach
payment = client.is_movement_paid(movement_id, company_id="TMS2")
if payment:
    # PAID - has pay_date, check_number, total_pay
    pass
else:
    # NOT PAID - check pending settlements or deductions
    pass
```

**Data Flow:**
1. Movement created → appears in `/orders/{id}` and `/movements/search`
2. Ready for payment → appears in `/settlements/search` (pending)
3. Deductions added → appears in `/deductions/search` (pending)
4. Payment processed → moves to `/settlements/history/search` and `/deductions/history`
5. `is_movement_paid()` queries step 4 directly

---

## API Endpoint Reference

| Function | Endpoint | Auth |
|----------|----------|------|
| `search_settlements()` | `/settlements/search` | Basic or API Key |
| `update_settlement_status()` | `/settlement/update` + `/drs_pending_deduct/update` | Basic or API Key |
| `update_settlement_ok2pay_date()` | `/settlement/update` | Basic or API Key |
| `update_deduction_status()` | `/drs_pending_deduct/update` | Basic or API Key |
| `search_settlement_history()` | `/settlements/history/search` | Basic or API Key |
| `is_movement_paid()` | `/settlements/history/search` | Basic or API Key |
| `search_deductions()` | `/deductions/search` | Basic or API Key |
| `search_deductions_history()` | `/deductions/history` | **Basic Auth Only** |
| `search_deductions_by_movement()` | Both above | Mixed |

---

## Tips for Future Development

1. **Always test both auth methods** - Some endpoints reject API keys (e.g., `/deductions/history`)
2. **Check sample JSON files** - Located in `samples/` directory, organized by endpoint
3. **Server-side filtering varies** - Some endpoints ignore certain filters; may need client-side filtering
4. **Date format** - McLeod uses `YYYYMMDDHHMMSS-0700` format (e.g., `20251126000000-0800`)
5. **Pagination** - Most endpoints support `recordLength` and `recordOffset`; some use cursor-based pagination

