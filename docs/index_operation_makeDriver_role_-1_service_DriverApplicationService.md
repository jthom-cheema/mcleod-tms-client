# McLeod API Documentation - /driverApplications/makeDriver/{applicationId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=makeDriver&role=-1&service=DriverApplicationService

---

go back to [DriverApplicationService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverApplicationService&role=-1)

# POST /driverApplications/makeDriver/{applicationId}

Create a driver from the given driver application.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
applicationId | application ID of the driver application for which to create the driver |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverId | driver ID to use when creating the driver row, if not supplied and auto gen is active driver table mask will be used |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
cityId | city ID of the city associated with driver. If not supplied city name and zip will be used to look up city, if multiple cities are found the first one will be used. |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver&role=-1) _of type: application/xml application/json_

the created RowDriver or string representing failure of the web service call

## Request Details

**Endpoint:** `POST /driverApplications/makeDriver/{applicationId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
POST /driverApplications/makeDriver/{applicationId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
