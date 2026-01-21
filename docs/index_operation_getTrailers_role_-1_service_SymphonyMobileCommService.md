# McLeod API Documentation - /symphonymcmessages/trailers

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getTrailers&role=-1&service=SymphonyMobileCommService

---

go back to [SymphonyMobileCommService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&role=-1)

# GET /symphonymcmessages/trailers

Get all Trailers

Roles that can access this endpoint are [ Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
blocksize | \- maximum returned records default is 100 |  query  |  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
index | \- id of previous last record (blank for first record) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowTrailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTrailer&role=-1) > _of type: application/xml application/json_

response object indicating the success or failure of returning the trailer records

## Request Details

**Endpoint:** `GET /symphonymcmessages/trailers`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /symphonymcmessages/trailers HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
