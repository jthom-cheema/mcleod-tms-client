# McLeod API Documentation - /{table}/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=update&role=-1&service=TableRowService

---

go back to [TableRowService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&role=-1)

# PUT /{table}/update

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
table |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
row |  |  body _of type: application/xml application/json_ |  |  [T](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=T&role=-1)  
  
* * *

## Result

[T](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=T&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `PUT /{table}/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [T](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=T&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /{table}/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
