# McLeod API Documentation - /alerts/messages/confirm

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=markAlertsConfirmed&role=-1&service=AlertService

---

go back to [AlertService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&role=-1)

# POST /alerts/messages/confirm

Marks all rapid alerts as confirmed.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
value | boolean value used to update the is_confirmed value for the given alert message |  query  | true |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
alertId | specifies the rapid alert type ID |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

Response object with Success or Failure status and status string to display to the user

## Request Details

**Endpoint:** `POST /alerts/messages/confirm`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /alerts/messages/confirm HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
