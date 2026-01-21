# McLeod API Documentation - /drivers/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createDriver&role=-1&service=DriverService

---

go back to [DriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&role=-1)

# PUT /drivers/create

Creates a new RowDriver record for the given Driver data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
driver | the data to use when creating the new driver |  body _of type: application/xml application/json_ |  |  [RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver&role=-1)  
  
* * *

## Result

[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver&role=-1) _of type: application/xml application/json_

the created RowDriver record   
  

  * `__returnHomeFlagDescr` This value represents the description of the return home flag, found in the `driver.return_home_flag` field.
  * `__sexDescr` This value represents the description of the driver's sex, found in the `driver.sex` field.
  * `__teamStatusDescr` This value represents the description of the driver's team status, found in the `driver.team_status` field.
  * `__typeOfDescr` This value represents the description of the driver type, found in the `driver.type_of` field.

Child Elements: 
  * `[RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation)` This element represent the location associated with the driver's home location, by the `driver.home_location_id` field. The element contains a `__name` attribute with the value `homeLocation`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the fleet manager user associated with the driver by the `driver.fleet_manager` field. The element contains a `__name` attribute with the value `fleetManager`.
  * `[RowDriverLane](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverLane)` These elements represent the lane exclusions associated with the driver. The element contains a `__name` attribute with the value `lanes`. 

## Request Details

**Endpoint:** `PUT /drivers/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /drivers/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
