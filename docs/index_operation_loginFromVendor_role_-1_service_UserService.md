# McLeod API Documentation - /users/loginFromVendor

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=loginFromVendor&role=-1&service=UserService

---

go back to [UserService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&role=-1)

# POST /users/loginFromVendor

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

## Request Details

**Endpoint:** `POST /users/loginFromVendor`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /users/loginFromVendor HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
