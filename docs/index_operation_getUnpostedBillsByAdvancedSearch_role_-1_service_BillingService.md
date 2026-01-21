# McLeod API Documentation - /billing

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getUnpostedBillsByAdvancedSearch&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# GET /billing

Retrieves a list of unposted billing records matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the `billing` table   
  
For example, `/billing?ready_to_process=Y&blnum=12345*&ship_date=>=t-100` would find bills ready to process having a BOL that starts with '12345' that shipped in the last 100 days. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
includeUsers | whether to include user detail records with each invoice |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
includeCustomer | whether to include customer details with each invoice |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowBilling&role=-1) > _of type: application/xml application/json_

a list of RowBilling records   
  
Additional attributes: 

  * `__revenuTypeDescr` the description of the revenue code, found in the `revenue_id` field
  * `__rateTypeDescr` the hard coded description of the rate type, found in the `rate_type` field
  * `__billTypeDescr` the hard coded description of the bill type, found in the `bill_type` field
  * `__paymentMethodDescr` the hard coded description of the payment method, found in the `payment_method` field

Child Elements: 
  * `[RowOtherChargeBill](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherChargeBill)` the other charges associated with the bill; each containing a `__name` attribute equal to `otherCharges`
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` the entered by user associated with the `entered_user_id` field; contains a `__name` attribute equal to `enteredUser` (included only when the `includeUsers` query parameter is true)
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` the billing user associated with the `billing_user_id` field; contains a `__name` attribute equal to `billingUser` (included only when the `includeUsers` query parameter is true)
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` the customer associated with the `customer_id` field; contains a `__name` attribute equal to `customer` (included only when the `includeCustomer` query parameter is true)

## Request Details

**Endpoint:** `GET /billing`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /billing HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
