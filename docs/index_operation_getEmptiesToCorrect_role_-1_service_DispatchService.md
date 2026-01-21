# McLeod API Documentation - /dispatch/emptiesToCorrect

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEmptiesToCorrect&role=-1&service=DispatchService

---

go back to [DispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DispatchService&role=-1)

# GET /dispatch/emptiesToCorrect

Determines previous empties for a given tractor, when canceling a movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | ID of the movement being canceled |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
tractorId | ID of the tractor for which to determine previous empties |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1) > _of type: application/xml application/json_

a list of empty movements   
  
Child Elements: 

  * `[RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop)` This element represent the origin stop for the order. The element contains a `__name` attribute with the value `origin`.
  * `[RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop)` This element represent the consignee stop for the order. The element contains a `__name` attribute with the value `destination`.

## Request Details

**Endpoint:** `GET /dispatch/emptiesToCorrect`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /dispatch/emptiesToCorrect HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
