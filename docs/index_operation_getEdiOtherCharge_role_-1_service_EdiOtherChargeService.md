# McLeod API Documentation - /ediOtherCharges/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEdiOtherCharge&role=-1&service=EdiOtherChargeService

---

go back to [EdiOtherChargeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOtherChargeService&role=-1)

# GET /ediOtherCharges/{id}

Retrieves an EdiOtherCharge based on the ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the EDI other charge to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowOtherChargeEdi](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherChargeEdi&role=-1) _of type: application/xml application/json_

an EdiOtherCharge object   
  
Additional attributes: 

  * `__calcMethodDescr` This value represents the description of the rate methods, found in the `other_charge_edi.calc_method` field.

Child Elements: 
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represent the customer associated with the other charge, by the `other_charge_edi.customer_id` field. The element contains a `__name` attribute with the value `customer`.

## Request Details

**Endpoint:** `GET /ediOtherCharges/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediOtherCharges/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
