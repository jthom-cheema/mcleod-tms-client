# McLeod API Documentation - /contacts/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=deleteContact&role=-1&service=ContactService

---

go back to [ContactService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ContactService&role=-1)

# DELETE /contacts/{id}

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1)

## Request Details

**Endpoint:** `DELETE /contacts/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
DELETE /contacts/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
