# McLeod API Documentation - /users/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getUser&role=-1&service=UserService

---

go back to [UserService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&role=-1)

# GET /users/{id}

Retrieves a user based on the specified ID.

Roles that can access this endpoint are [ Users, Drivers, Customers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID for the user to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers&role=-1) _of type: application/xml application/json_

the requested RowUsers object   
  
Child Elements: 

  * `[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments)` These elements represent the comments associated with the user. The element contains a `__name` attribute with the value `comments`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represents the driver associated with the user, if the user is of type driver. The element contains a `__name` attribute with the value `driver`. 

## Request Details

**Endpoint:** `GET /users/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /users/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
