# McLeod API Documentation - /locations/userSavedSearch

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=userSavedSearch&role=-1&service=LocationService

---

go back to [LocationService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&role=-1)

# GET /locations/userSavedSearch

Retrieves a List of RowLocation objects based on an existing saved search.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
userId | string indicating the current user |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
createUserId | string indicating the user who created the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
screenClassName | string indicating the class of the screen that is related to the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
searchName | string indicating the name of the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation&role=-1) > _of type: application/xml application/json_

a list of RowLocation objects

## Request Details

**Endpoint:** `GET /locations/userSavedSearch`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /locations/userSavedSearch HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
