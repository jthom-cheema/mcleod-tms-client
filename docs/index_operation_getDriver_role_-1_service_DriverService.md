# McLeod API Documentation - /drivers/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDriver&role=-1&service=DriverService

---

go back to [DriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&role=-1)

# GET /drivers/{id}

Retrieves the Driver record with the given ID.

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID for the driver to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeComments | if related Comment records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeContacts | if related Contact records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeLanes | if related RowDriverLane records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver&role=-1) _of type: application/xml application/json_

the requested RowDriver record   
  
Additional attributes: 

  * `__returnHomeFlagDescr` This value represents the description of the return home flag, found in the `driver.return_home_flag` field.
  * `__sexDescr` This value represents the description of the driver's sex, found in the `driver.sex` field.
  * `__teamStatusDescr` This value represents the description of the driver's team status, found in the `driver.team_status` field.
  * `__typeOfDescr` This value represents the description of the driver type, found in the `driver.type_of` field.
  * `__currentMovementId` This value represents the ID of the driver's current movement.

Child Elements: 
  * `[RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation)` This element represent the location associated with the driver's home location, by the `driver.home_location_id` field. The element contains a `__name` attribute with the value `homeLocation`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the fleet manager user associated with the driver by the `driver.fleet_manager` field. The element contains a `__name` attribute with the value `fleetManager`.
  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the contacts associated with the driver. The element contains a `__name` attribute with the value `contacts`. *Note this is only returned if the `includeContacts` Query Parameter is passed as true.
  * `[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments)` These elements represent the comments associated with the driver. The element contains a `__name` attribute with the value `comments`. *Note this is only returned if the `includeComments` Query Parameter is passed as true.
  * `[RowDriverLane](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverLane)` These elements represent the lane exclusions associated with the driver. The element contains a `__name` attribute with the value `lanes`. *Note this is only returned if the `includeLanes` Query Parameter is passed as true.

## Request Details

**Endpoint:** `GET /drivers/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /drivers/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
