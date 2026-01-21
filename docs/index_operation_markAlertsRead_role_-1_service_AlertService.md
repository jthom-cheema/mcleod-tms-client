# McLeod API Documentation - /alerts/messages/read

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=markAlertsRead&role=-1&service=AlertService

---

go back to [AlertService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&role=-1)

# POST /alerts/messages/read

Marks all messages as read, for the given user. The User ID is not passed as a parameter, but rather is determined by the Device ID in the request header.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
value | the boolean value for which to update the "is_confirmed" value for alert messages |  query  | true |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
alertId | specifies the rapid alert type ID |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

the boolean value for which to update the "is_confirmed" value for the alert message

## Request Details

**Endpoint:** `POST /alerts/messages/read`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /alerts/messages/read HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
