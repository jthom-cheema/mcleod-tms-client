# McLeod API Documentation - /trailers/{id}/preassignments

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getPreassignments&role=-1&service=TrailerService

---

go back to [TrailerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&role=-1)

# GET /trailers/{id}/preassignments

Retrieves preassignments for the trailer with the specified ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the trailer for which to return preassignments |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [Preassignment](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.dsp.Preassignment&role=-1) > _of type: application/xml application/json_

a list of rows

## Request Details

**Endpoint:** `GET /trailers/{id}/preassignments`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /trailers/{id}/preassignments HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
