# McLeod API Documentation - /carrierDispatch/unlock/{movementId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=unlock&role=-1&service=CarrierDispatchService

---

go back to [CarrierDispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&role=-1)

# POST /carrierDispatch/unlock/{movementId}

This will attempt to unlock a locked move. An exception will be thrown if the move is not locked, the locked user is different than the one making the unlock request, or the requesting user does not have permission to unlock a movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | ID of the movement to be unlocked |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response containing the success or failure message of the unlock request

## Request Details

**Endpoint:** `POST /carrierDispatch/unlock/{movementId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierDispatch/unlock/{movementId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
