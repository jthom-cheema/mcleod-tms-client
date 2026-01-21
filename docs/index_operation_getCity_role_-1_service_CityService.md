# McLeod API Documentation - /cities/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCity&role=-1&service=CityService

---

go back to [CityService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CityService&role=-1)

# GET /cities/{id}

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id |  |  path  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
  
* * *

## Result

[RowCity](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCity&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `GET /cities/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /cities/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
