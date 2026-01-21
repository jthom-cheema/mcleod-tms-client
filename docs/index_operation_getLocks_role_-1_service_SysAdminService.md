# McLeod API Documentation - /sysadmin/locks

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getLocks&role=-1&service=SysAdminService

---

go back to [SysAdminService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SysAdminService&role=-1)

# GET /sysadmin/locks

This method gets a list of current application locks.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [LockInfo](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.sysadmin.LockInfo&role=-1) > _of type: application/xml application/json_

a list of LockInfo objects

## Request Details

**Endpoint:** `GET /sysadmin/locks`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /sysadmin/locks HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
