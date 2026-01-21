# McLeod API Documentation - /ediStops/{id}/referenceNumbers

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getReferenceNumbers&role=-1&service=EdiStopService

---

go back to [EdiStopService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStopService&role=-1)

# GET /ediStops/{id}/referenceNumbers

Retrieves reference numbers for the specified stop ID

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the stop for which to return reference numbers |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowReferenceNumber](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowReferenceNumber&role=-1) > _of type: application/xml application/json_

a list of ReferenceNumber objects

## Request Details

**Endpoint:** `GET /ediStops/{id}/referenceNumbers`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediStops/{id}/referenceNumbers HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
