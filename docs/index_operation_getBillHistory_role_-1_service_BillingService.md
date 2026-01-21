# McLeod API Documentation - /billing/history/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getBillHistory&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# GET /billing/history/{id}

Retrieves details for the requested historical freight billing record.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the historical billing record to be retrieved |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowBillingHistory](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowBillingHistory&role=-1) _of type: application/xml application/json_

a RowBillingHistory record   
  
Additional attributes: 

  * `__revenuTypeDescr` the description of the revenue code, found in the `revenue_id` field.
  * `__rateTypeDescr` the hard coded description of the rate type, found in the `rate_type` field. 
  * `__billTypeDescr` the hard coded description of the bill type, found in the `bill_type` field. 
  * `__paymentMethodDescr` the hard coded description of the payment method, found in the `payment_method` field. 

Child Elements: 
  * `[RowOtherChargeBill](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherChargeBill)` the other charges associated with the bill; each containing a `__name` attribute equal to `otherCharges`
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` the entered by user associated with the `entered_user_id` field; contains a `__name` attribute equal to `enteredUser`
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` the billing user associated with the `billing_user_id` field; contains a `__name` attribute equal to `billingUser`
  * [RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer) the customer associated with the `customer_id` field; contains a `__name` attribute equal to `customer`

## Request Details

**Endpoint:** `GET /billing/history/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /billing/history/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
