# McLeod API Documentation - /stops/{id}/referenceNumbers/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newReferenceNumber&role=-1&service=StopService

---

go back to [StopService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=StopService&role=-1)

# GET /stops/{id}/referenceNumbers/new

Creates a reference number object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowReferenceNumber](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowReferenceNumber&role=-1) _of type: application/xml application/json_

a reference number record with all appropriate defaults set

## Request Details

**Endpoint:** `GET /stops/{id}/referenceNumbers/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /stops/{id}/referenceNumbers/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
