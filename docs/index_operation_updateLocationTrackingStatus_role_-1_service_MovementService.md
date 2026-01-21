# McLeod API Documentation - /movements/{id}/updateLocationTrackingStatus

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateLocationTrackingStatus&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# POST /movements/{id}/updateLocationTrackingStatus

Updates the Brokerage Tracking Status based on if the user's device has location services enabled

Roles that can access this endpoint are [ Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the movement |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
enabled | Indicates if the app's location services are available |  query  |  |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a String indicating if the operation was successful

## Request Details

**Endpoint:** `POST /movements/{id}/updateLocationTrackingStatus`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /movements/{id}/updateLocationTrackingStatus HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
