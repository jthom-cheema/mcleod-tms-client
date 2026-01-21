# McLeod API Documentation - /carrierDispatch/assign/{movementId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=assignCarrier&role=-1&service=CarrierDispatchService

---

go back to [CarrierDispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&role=-1)

# POST /carrierDispatch/assign/{movementId}

This method allows assignment of a carrier to a movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | ID of the movement to be updated |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierId | ID of the carrier to be assigned |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
reason | string reason for unassigning the previously assigned carrier |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response containing the success or failure of the assignment request

## Request Details

**Endpoint:** `POST /carrierDispatch/assign/{movementId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierDispatch/assign/{movementId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
