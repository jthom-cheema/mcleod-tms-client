# McLeod API Documentation - /carrierDispatch/addPendingLock/{movementId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=addPendingLock&role=-1&service=CarrierDispatchService

---

go back to [CarrierDispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&role=-1)

# POST /carrierDispatch/addPendingLock/{movementId}

Adds a pending lock on the movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | ID of the movement to be locked |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
notificationType | an int value representing the type of notification requested by the user NOTIFICATION TYPES: 1 - Don't request lock 2 - Request lock with no notification 3 - Request lock with email notification 4 - Request lock with rapid alert notification |  query  | 2 |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response containing the success or failure message of the pending lock request @see PanelPendingLockPrompt

## Request Details

**Endpoint:** `POST /carrierDispatch/addPendingLock/{movementId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierDispatch/addPendingLock/{movementId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
