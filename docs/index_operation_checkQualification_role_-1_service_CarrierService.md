# McLeod API Documentation - /carriers/checkQualification

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=checkQualification&role=-1&service=CarrierService

---

go back to [CarrierService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&role=-1)

# GET /carriers/checkQualification

Check to see if a carrier is qualified, based on carrier qualifications, to haul a specific load.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
carrier | string for which to search for carrier by ID |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
movement | string for which to search for movements by ID |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1) _of type: text/plain_

true or false

## Request Details

**Endpoint:** `GET /carriers/checkQualification`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carriers/checkQualification HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
