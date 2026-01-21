# McLeod API Documentation - /dispatch/reconsign/{movementId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=reconsign&role=-1&service=DispatchService

---

go back to [DispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DispatchService&role=-1)

# POST /dispatch/reconsign/{movementId}

Reconsigns the order for the given movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
newConsigneeStop | a stop object representing the new consignee stop |  body _of type: application/xml application/json_ |  |  [RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop&role=-1)  
movementId | ID of the move for which to reconsign the order |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
overrideXferToFueltax | whether to allow reconsignment if transfer to fuel tax has already been done |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
overrideXferToSettlements | whether to allow reconsignment if transfer to settlements has already been done |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response object containing an HTTP response code and string representing success or failure of the web service call

## Request Details

**Endpoint:** `POST /dispatch/reconsign/{movementId}`

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
POST /dispatch/reconsign/{movementId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
