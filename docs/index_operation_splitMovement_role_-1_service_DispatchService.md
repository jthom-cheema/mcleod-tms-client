# McLeod API Documentation - /dispatch/split/{splitBeforeStopId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=splitMovement&role=-1&service=DispatchService

---

go back to [DispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DispatchService&role=-1)

# POST /dispatch/split/{splitBeforeStopId}

Splits the given movement, given the specified stop and equipment information.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
splitBeforeStopId | ID of the stop before which to place the split point |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
splitStop | RowStop object containing the stop details for the split point |  body _of type: application/xml application/json_ |  |  [RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop&role=-1)  
tractorId | ID of the tractor |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driver1Id | ID of the first driver |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driver2Id | ID of the second driver |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
emptyToCorrectMovementId | ID of the empty movement to be corrected |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response object containing an HTTP response code and string representing success or failure of the web service call

## Request Details

**Endpoint:** `POST /dispatch/split/{splitBeforeStopId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
POST /dispatch/split/{splitBeforeStopId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
