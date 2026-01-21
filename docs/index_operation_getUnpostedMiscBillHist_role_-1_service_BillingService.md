# McLeod API Documentation - /billing/miscBilling/history/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getUnpostedMiscBillHist&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# GET /billing/miscBilling/history/{id}

Retrieves details for the requested miscellaneous bill history.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the miscellaneous bill history to be retrieved |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMiscBillHist](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMiscBillHist&role=-1) _of type: application/xml application/json_

a RowMiscBillHist record for the requested miscellaneous bill   
  
Additional attributes: 

  * `__billTypeDescr` the description of the bill type, found in the `bill_type` field
  * `__arCycleCodeDescr` the description of the AR cycle code, found in the `ar_cycle_code_id` field
  * `__twSegCodeDescr` the description of the segment allocation code, found in the `tw_seg_code` field

Child elements: 
  * `[RowMiscBillDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMiscBillDetail)` the miscellaneous billing detail records associated with the bill; each containing a `__name` attribute equal to `miscBillDetails`
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` the billing user associated with the bill; containing a `__name` attribute equal to `billingUser`
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` the customer associated with the bill; containing a `__name` attribute equal to `customer`

## Request Details

**Endpoint:** `GET /billing/miscBilling/history/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /billing/miscBilling/history/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
