# McLeod API Documentation - /links

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getMyLinks&role=-1&service=LinkService

---

go back to [LinkService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LinkService&role=-1)

# GET /links

Retrieves a list of mobile link records appropriate for the current user.

The endpoint has no roles. 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMobileLink](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowMobileLink&role=-1) > _of type: application/xml application/json_

a list of mobile link records

## Request Details

**Endpoint:** `GET /links`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /links HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
