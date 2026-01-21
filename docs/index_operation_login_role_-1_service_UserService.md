# McLeod API Documentation - /users/login

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=login&role=-1&service=UserService

---

go back to [UserService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&role=-1)  
  
# POST /users/login

Logs the user in and returns a token that may be used on subsequent requests for access.

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
user-agent | the "User-Agent" HTTP header |  header  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
accept | the "Accept" HTTP header (only text/plain or application/json are valid) |  header  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain application/json_

a response indicating success or failure and if success, the access token

## Request Details

**Endpoint:** `POST /users/login`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain application/json
  - Default: application/xml (if not specified)

### Example Request

```http
POST /users/login HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
