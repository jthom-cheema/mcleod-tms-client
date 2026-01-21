# McLeod API Documentation - /billing/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateBill&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# PUT /billing/update

Updates a RowBilling record for the given data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
rowBilling | the data use to update the given RowBilling record |  body _of type: application/xml application/json_ |  |  [RowBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowBilling&role=-1)  
includeUsers | include user details with the returned RowBilling record |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
includeCustomer | include Customer details with the returned RowBilling record |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[RowBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowBilling&role=-1) _of type: application/xml application/json_

a RowBilling record representing the updated values   
  
Additional attributes: 

  * `__revenuTypeDescr` the description of the revenue code, found in the `revenue_id` field.
  * `__rateTypeDescr` the hard coded description of the rate type, found in the `rate_type` field. 
  * `__billTypeDescr` the hard coded description of the bill type, found in the `bill_type` field. 
  * `__paymentMethodDescr` the hard coded description of the payment method, found in the `payment_method` field. 

Child Elements: 
  * `[RowOtherChargeBill](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherChargeBill)` the other charges associated with the bill; each containing a `__name` attribute equal to `otherCharges`
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` the entered by user associated with the `entered_user_id` field; contains a `__name` attribute equal to `enteredUser` (included only when the `includeUsers` query parameter is true)
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` the billing user associated with the `billing_user_id` field; contains a `__name` attribute equal to `billingUser` (included only when the `includeUsers` query parameter is true)
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` the customer associated with the `customer_id` field; contains a `__name` attribute equal to `customer` (included only when the `includeCustomer` query parameter is true)

## Request Details

**Endpoint:** `PUT /billing/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowBilling&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /billing/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
