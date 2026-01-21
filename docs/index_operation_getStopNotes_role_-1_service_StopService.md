# McLeod API Documentation - /stops/{id}/stopNotes

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getStopNotes&role=-1&service=StopService

---

go back to [StopService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=StopService&role=-1)

# GET /stops/{id}/stopNotes

Retrieves stop notes for the specified stop ID

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the stop for which to return stop notes |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowStopNote](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStopNote&role=-1) > _of type: application/xml application/json_

a list of StopNote objects

## Request Details

**Endpoint:** `GET /stops/{id}/stopNotes`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /stops/{id}/stopNotes HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
