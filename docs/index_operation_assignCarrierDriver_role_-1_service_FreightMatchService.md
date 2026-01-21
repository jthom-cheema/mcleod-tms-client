# McLeod API Documentation - /freightmatch/{movementId}/assignCarrierDriver

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=assignCarrierDriver&role=-1&service=FreightMatchService

---

go back to [FreightMatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=FreightMatchService&role=-1)

# POST /freightmatch/{movementId}/assignCarrierDriver

Update the driver name, mobile phone number and email address on a load

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | (Required) ID of the movement for the arrive/depart event |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
eventDateTime | (Required) Date and time of the assignment |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
driverName | (Required) Driver's name |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverPhone | (Required) Driver's mobile phone number |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverEmail | (Optional) Driver's email address |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

## Request Details

**Endpoint:** `POST /freightmatch/{movementId}/assignCarrierDriver`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /freightmatch/{movementId}/assignCarrierDriver HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
