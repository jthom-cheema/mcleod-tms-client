# McLeod API Documentation - /{table}/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=get&role=-1&service=TableRowService

---

go back to [TableRowService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&role=-1)

# GET /{table}/{id}

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
table |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
id |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[T](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=T&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `GET /{table}/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /{table}/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
