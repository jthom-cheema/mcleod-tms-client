# McLeod API Documentation - /users/loginWithPIN

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=loginWithPIN&role=-1&service=UserService

---

go back to [UserService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&role=-1)

# POST /users/loginWithPIN

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
pin |  |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1) _of type: application/xml_

## Request Details

**Endpoint:** `POST /users/loginWithPIN`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml
  - Default: application/xml (if not specified)

### Example Request

```http
POST /users/loginWithPIN HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
