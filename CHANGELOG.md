# Changelog

Update history for the McLeod TMS Client. Each entry includes what was added, where to find examples, and pointers for future development.

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

## [2025-12-18] Deductions Search & History

### Added
- **`search_deductions()`** - Search pending deductions via `/deductions/search`
- **`search_deductions_history()`** - Search processed deductions via `/deductions/history`
- **`search_deductions_by_movement()`** - Convenience method with auto-fallback to history

### Known Issues
- **`/deductions/history` requires Basic Auth** - API key authentication is rejected with 401. Must use username/password.
- **Server-side filtering limited** - The `/deductions/history` endpoint ignores `movement_id` filter; client-side filtering is used.

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

