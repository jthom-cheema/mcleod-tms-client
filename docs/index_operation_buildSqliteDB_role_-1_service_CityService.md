# McLeod API Documentation - /cities/db

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=buildSqliteDB&role=-1&service=CityService

---

go back to [CityService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CityService&role=-1)

# GET /cities/db

The endpoint has no roles. 

## Parameters

_This method has no parameters._

* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/octet-stream_

## Request Details

**Endpoint:** `GET /cities/db`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/octet-stream
  - Default: application/xml (if not specified)

### Example Request

```http
GET /cities/db HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/octet-stream
```
