# McLeod API Documentation - /sysadmin/getServerTimeMillis

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getServerTimestamp&role=-1&service=SysAdminService

---

go back to [SysAdminService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SysAdminService&role=-1)

# GET /sysadmin/getServerTimeMillis

This method returns the server time in milliseconds.

Roles that can access this endpoint are [ Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a timestamp value representing the server time in milliseconds.

## Request Details

**Endpoint:** `GET /sysadmin/getServerTimeMillis`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
GET /sysadmin/getServerTimeMillis HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
