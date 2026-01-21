# McLeod API Documentation - /motorAccidents

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getMotorAccidents&role=-1&service=MotorAccidentService

---

go back to [MotorAccidentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&role=-1)

# GET /motorAccidents

Retrieves a List of motor accident records matching the given request parameters or with an match of the given value to the driver ID or report number.

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the `motoraccident` table   
  
For example, `/motorAccidents?driver_type=C&state=AL&accident_date=>=t-100` would find accidents for company drivers in the state of Alabama within the last 100 days. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
q | string for which to search for motor accidents by driver ID or report number |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMotorAccident](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMotorAccident&role=-1) > _of type: application/xml application/json_

a list of `[RowMotorAccident](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowMotorAccident)` objects

## Request Details

**Endpoint:** `GET /motorAccidents`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /motorAccidents HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
