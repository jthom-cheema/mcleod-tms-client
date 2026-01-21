# McLeod API Documentation - /serviceFailures/{id}/approve

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=approve&role=-1&service=ServiceFailureService

---

go back to [ServiceFailureService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&role=-1)

# POST /serviceFailures/{id}/approve

Approves a service failure specified by the supplied ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the RowServiceFail record to be approved |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)

a response containing the success or failure message for the request

## Request Details

**Endpoint:** `POST /serviceFailures/{id}/approve`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
POST /serviceFailures/{id}/approve HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
