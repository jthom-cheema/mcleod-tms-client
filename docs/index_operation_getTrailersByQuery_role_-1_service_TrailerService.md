# McLeod API Documentation - /trailers

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getTrailersByQuery&role=-1&service=TrailerService

---

go back to [TrailerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&role=-1)

# GET /trailers

Retrieves a List of Trailers with a full or partial match to the given value.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
q | string for which to search for trailers by name or ID |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowTrailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTrailer&role=-1) > _of type: application/xml application/json_

a list of Trailer objects

## Request Details

**Endpoint:** `GET /trailers`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /trailers HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
