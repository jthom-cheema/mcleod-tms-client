# McLeod API Documentation - /billing/cashReceipts/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createCashReceiptsBatch&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# PUT /billing/cashReceipts/create

Creates a cash receipts batch. The batch header, receipt header and detail rows must all be included. Detail totals must match the check total. All check totals must match the header total.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
batch | a RowCashBatch with child RowCashReceiptHdr and RowCashReceiptDtl records |  body _of type: application/xml application/json_ |  |  [RowCashBatch](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCashBatch&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response with the created batch ID or a failure message

## Request Details

**Endpoint:** `PUT /billing/cashReceipts/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowCashBatch](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCashBatch&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /billing/cashReceipts/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
