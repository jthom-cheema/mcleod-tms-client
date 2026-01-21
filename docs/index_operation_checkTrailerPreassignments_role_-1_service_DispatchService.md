# McLeod API Documentation - /dispatch/checkTrailerPreassignments/{trailerId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=checkTrailerPreassignments&role=-1&service=DispatchService

---

go back to [DispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DispatchService&role=-1)

# GET /dispatch/checkTrailerPreassignments/{trailerId}

Checks to see if the trailer has existing preassignments other than the current movement being checked for dispatch.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
trailerId | ID of the trailer for which to check for preassignments |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
excludedMovementId | ID of the movement the trailer is being assigned to so it can be excluded in the preassignment check |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response containing Status.OK (200) of the trailer has no preassignments or Status.CONFLICT (409) if there are existing preassignments

## Request Details

**Endpoint:** `GET /dispatch/checkTrailerPreassignments/{trailerId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
GET /dispatch/checkTrailerPreassignments/{trailerId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
