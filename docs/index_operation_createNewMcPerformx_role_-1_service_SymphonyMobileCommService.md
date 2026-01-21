# McLeod API Documentation - /symphonymcmessages/performance

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createNewMcPerformx&role=-1&service=SymphonyMobileCommService

---

go back to [SymphonyMobileCommService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&role=-1)

# POST /symphonymcmessages/performance

Creates a new Performance data

Roles that can access this endpoint are [ Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
rowMcPerformx |  |  body _of type: application/xml application/json_ |  |  [RowMcPerformx](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcPerformx&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

response object indicating the success or failure of adding the performance data

## Request Details

**Endpoint:** `POST /symphonymcmessages/performance`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowMcPerformx](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcPerformx&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
POST /symphonymcmessages/performance HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
