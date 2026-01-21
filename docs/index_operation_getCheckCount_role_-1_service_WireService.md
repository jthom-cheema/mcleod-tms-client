# McLeod API Documentation - /wires/{vendor}/checkCount

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCheckCount&role=-1&service=WireService

---

go back to [WireService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&role=-1)

# GET /wires/{vendor}/checkCount

Obtains the count of available checks for the vendor.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
vendor | the LME vendor code |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1) _of type: text/plain_

an int of the number of available checks

## Request Details

**Endpoint:** `GET /wires/{vendor}/checkCount`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
GET /wires/{vendor}/checkCount HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
