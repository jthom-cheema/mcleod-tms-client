# McLeod API Documentation - /billing/cashReceipts

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCashReceipts&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# GET /billing/cashReceipts

Retrieves a List of open items matching the given request parameters, posted through cash receipts.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the `open_item` table   
  
For example, `/billing/cashReceipts?is_split_bill=Yℴ_id=12345*&ship_date=>=t-100` would find split bills having a order ID that starts with '12345' that shipped in the last 100 days. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
includeJournalEntries | whether to include GL Journal detail records with each receipt |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowOpenItem](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOpenItem&role=-1) > _of type: application/xml application/json_

a list of RowOpenItem objects matching the requested parameters   
  
Child elements: 

  * `[RowJournalCash](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowJournalCash)` the GL journal entries associated with the cash receipt (included only when `includeJournalEntries` query parameter is true)

## Request Details

**Endpoint:** `GET /billing/cashReceipts`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /billing/cashReceipts HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
