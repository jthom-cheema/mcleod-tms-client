# McLeod API Documentation - /billing/miscBilling/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createMiscBill&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# PUT /billing/miscBilling/create

Creates a miscellaneous bill. At least one detail records must be included.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
bill | the RowMiscBill object; include child RowMiscBillDetail records as children of this object with the `__name` attribute set to `miscBillDetails` |  body _of type: application/xml application/json_ |  |  [RowMiscBill](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMiscBill&role=-1)  
  
* * *

## Result

[RowMiscBill](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMiscBill&role=-1)

the created RowMiscBill object

## Request Details

**Endpoint:** `PUT /billing/miscBilling/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Request Body

- **Type:** [RowMiscBill](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMiscBill&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /billing/miscBilling/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Content-Type: application/xml
```
