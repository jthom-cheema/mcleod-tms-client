# McLeod API Documentation - /users/current

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCurrentUser&role=-1&service=UserService

---

go back to [UserService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&role=-1)

# GET /users/current

Retrieves the currently logged in user.

Roles that can access this endpoint are [ Logged In, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[Authorizable](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Authorizable&role=-1) _of type: application/xml application/json_

a RowUsers object

## Request Details

**Endpoint:** `GET /users/current`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /users/current HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
