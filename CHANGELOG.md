# Changelog

Update history for the McLeod TMS Client. Each entry includes what was added, where to find examples, and pointers for future development.

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

