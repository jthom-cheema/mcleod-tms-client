# McLeod API Documentation - /stops/{stopId}/referenceNumbers/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=deleteReferenceNumber&role=-1&service=StopService

---

go back to [StopService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=StopService&role=-1)

# DELETE /stops/{stopId}/referenceNumbers/{id}

Deletes a reference number from a stop

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
stopId | Id of the stop to delete the reference number from |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
id | Id of the reference number to delete |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop&role=-1) _of type: application/xml application/json_

stop record containing all reference numbers after the delete

## Request Details

**Endpoint:** `DELETE /stops/{stopId}/referenceNumbers/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
DELETE /stops/{stopId}/referenceNumbers/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
