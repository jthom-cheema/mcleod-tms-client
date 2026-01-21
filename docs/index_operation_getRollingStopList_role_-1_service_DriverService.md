# McLeod API Documentation - /drivers/rollingStops

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getRollingStopList&role=-1&service=DriverService

---

go back to [DriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&role=-1)

# GET /drivers/rollingStops

Retrieves a rolling List of RowStop objects for a driver.   
  
Under typical circumstances, this list will included:  
1: Cleared first stop of the current movement if in transit or  
Cleared last stop of the current movement if delivered.  
2: Next uncleared stop.  
3 - given stopCount: Upcoming first and last stops of the current and preassigned movements.  
  

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
stopCount | The number of stops to be returned in the list. Default value = 5. |  query  | 5 |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop&role=-1) > _of type: application/xml application/json_

A List of RowStop objects

## Request Details

**Endpoint:** `GET /drivers/rollingStops`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /drivers/rollingStops HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
