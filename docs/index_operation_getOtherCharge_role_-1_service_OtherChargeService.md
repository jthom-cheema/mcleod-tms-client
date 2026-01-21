# McLeod API Documentation - /otherCharges/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getOtherCharge&role=-1&service=OtherChargeService

---

go back to [OtherChargeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OtherChargeService&role=-1)

# GET /otherCharges/{id}

Retrieves the Other Charge specified by the ID

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the other charge to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowOtherCharge](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherCharge&role=-1) _of type: application/xml application/json_

the requested OtherCharge object   
  
Additional attributes: 

  * `__calcMethodDescr` This value represents the description of the rate method, found in the `other_charge.calc_method` field.

Child Elements: 
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represents the customer associated with the other charge, by the `other_charge.customer_id` field. The element contains a `__name` attribute with the value `customer`.

## Request Details

**Endpoint:** `GET /otherCharges/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /otherCharges/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
