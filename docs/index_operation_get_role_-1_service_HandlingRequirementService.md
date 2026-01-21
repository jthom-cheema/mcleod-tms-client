# McLeod API Documentation - /handling_requirement/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=get&role=-1&service=HandlingRequirementService

---

go back to [HandlingRequirementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=HandlingRequirementService&role=-1)

# GET /handling_requirement/{id}

Retrieves the handling requirement record identified by the given ID value.

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the handling requirement record in the database |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowHandlingRequirement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowHandlingRequirement&role=-1) _of type: application/xml application/json_

the handling requirement record

## Request Details

**Endpoint:** `GET /handling_requirement/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /handling_requirement/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
