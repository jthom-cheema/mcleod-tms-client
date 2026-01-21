# McLeod API Documentation - /sysadmin/locks/unlock

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=unlock&role=-1&service=SysAdminService

---

go back to [SysAdminService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SysAdminService&role=-1)

# POST /sysadmin/locks/unlock

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
info |  |  body _of type: application/xml application/json_ |  |  [LockInfo](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.sysadmin.LockInfo&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

## Request Details

**Endpoint:** `POST /sysadmin/locks/unlock`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [LockInfo](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.sysadmin.LockInfo&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
POST /sysadmin/locks/unlock HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
