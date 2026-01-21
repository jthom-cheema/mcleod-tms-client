# McLeod API Documentation - /{table}/{id}/{method}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=executeInstanceMethod&role=-1&service=TableRowService

---

go back to [TableRowService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&role=-1)

# POST /{table}/{id}/{method}

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
table |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
method |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
id |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[Object](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Object&role=-1) _of type: application/xml application/json text/plain_

## Request Details

**Endpoint:** `POST /{table}/{id}/{method}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /{table}/{id}/{method} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
