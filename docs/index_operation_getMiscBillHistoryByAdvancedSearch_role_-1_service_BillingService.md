# McLeod API Documentation - /billing/miscBilling/history

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getMiscBillHistoryByAdvancedSearch&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# GET /billing/miscBilling/history

Retrieves a list of historical miscellaneous bills matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the `misc_bill_hist` table   
  
For example, `/billing/miscBilling/history?ready_to_process=Yℴ_id=12345*&bill_date=>=t-100` would find bills ready for processing having a order ID that starts with '12345' that was billed in the last 100 days. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
includeUser |  |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
includeCustomer | whether to include customer details with each invoice |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMiscBillHist](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMiscBillHist&role=-1) > _of type: application/xml application/json_

a list of RowMiscBillHistory records for all historical bills   
  
Additional attributes: 

  * `__billTypeDescr` the description of the bill type, found in the `bill_type` field.
  * `__arCycleCodeDescr` the description of the AR cycle code, found in the `ar_cycle_code_id` field.
  * `__twSegCodeDescr` the description of the segment allocation code, found in the `tw_seg_code` field.

Child elements: 
  * `[RowMiscBillDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMiscBillDetail)` the miscellaneous billing detail records associated with the bill; each containing a a `__name` attribute equal to `miscBillDetails 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` the billing user associated with the bill; contains a `__name` attribute equal to `billingUser`. *Note this is only returned if the `includeUsers` Query Parameter is passed as true.
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` the customer associated with the bill; contains a `__name` attribute equal to `customer`. *Note this is only returned if the `includeCustomer` Query Parameter is passed as true.
`

## Request Details

**Endpoint:** `GET /billing/miscBilling/history`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /billing/miscBilling/history HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
