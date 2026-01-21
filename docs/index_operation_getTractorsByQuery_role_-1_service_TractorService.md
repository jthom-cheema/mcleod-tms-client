# McLeod API Documentation - /tractors

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getTractorsByQuery&role=-1&service=TractorService

---

go back to [TractorService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&role=-1)

# GET /tractors

Retrieves a List of Tractors with a full or partial match to the given value.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
q |  |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor&role=-1) > _of type: application/xml application/json_

a list of Tractor objects

## Request Details

**Endpoint:** `GET /tractors`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /tractors HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
