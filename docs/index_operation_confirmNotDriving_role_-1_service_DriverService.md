# McLeod API Documentation - /drivers/{id}/confirmNotDriving

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=confirmNotDriving&role=-1&service=DriverService

---

go back to [DriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&role=-1)

# POST /drivers/{id}/confirmNotDriving

Notes that the given driver has confirmed he's not driving while using the application.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the driver's ID |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
date | the timestamp of when the driver confirmed he's not driving |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
latitude | the latitude of where the driver confirmed he's not driving |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
longitude | the longitude of where the driver confirmed he's not driving |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
speed | the speed in mph of the driver when he confirmed he's not driving |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
course | the bearing in degrees with O indicating true north of the driver when he confirmed he's not driving |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
  
* * *

## Result

[int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1) _of type: text/plain_

the number of minutes the app can wait before prompting the user again (currently hardcoded at 10)

## Request Details

**Endpoint:** `POST /drivers/{id}/confirmNotDriving`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /drivers/{id}/confirmNotDriving HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
