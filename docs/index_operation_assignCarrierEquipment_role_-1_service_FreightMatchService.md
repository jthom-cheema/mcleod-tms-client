# McLeod API Documentation - /freightmatch/{movementId}/assignCarrierEquipment

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=assignCarrierEquipment&role=-1&service=FreightMatchService

---

go back to [FreightMatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=FreightMatchService&role=-1)

# POST /freightmatch/{movementId}/assignCarrierEquipment

Update the carrier tractor and carrier trailer on a load

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | (Required) ID of the movement for the arrive/depart event |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
eventDateTime | (Required) Date and time of the assignment |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
carrierTractor | (Required if carrierTrailer is not provided) Carrier tractor |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierTrailer | (Required if carrierTractor is not provided) Carrier trailer |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

## Request Details

**Endpoint:** `POST /freightmatch/{movementId}/assignCarrierEquipment`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /freightmatch/{movementId}/assignCarrierEquipment HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
