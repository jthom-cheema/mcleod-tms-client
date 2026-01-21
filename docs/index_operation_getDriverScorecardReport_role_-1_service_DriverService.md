# McLeod API Documentation - /drivers/{id}/scorecardReport

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDriverScorecardReport&role=-1&service=DriverService

---

go back to [DriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&role=-1)

# GET /drivers/{id}/scorecardReport

Produces the driver scorecard report.

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the driver |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
period | which period we should run (not specified means all) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf_

a response object containing the scorecard report in PDF format

## Request Details

**Endpoint:** `GET /drivers/{id}/scorecardReport`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
GET /drivers/{id}/scorecardReport HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
