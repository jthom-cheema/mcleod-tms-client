# McLeod API Documentation - /motorAccidents/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createMotorAccident&role=-1&service=MotorAccidentService

---

go back to [MotorAccidentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&role=-1)

# PUT /motorAccidents/create

Creates a new motor accident record. If successful, returns the new record.

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
accident | a RowMotorAccident record with associated child rows |  body _of type: application/xml application/json_ |  |  [RowMotorAccident](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMotorAccident&role=-1)  
  
* * *

## Result

[RowMotorAccident](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMotorAccident&role=-1) _of type: application/xml application/json_

the successfully created RowMotorAccident record with associated child rows   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the record status, found in the `motoraccident.status` field.
  * `__accidentCodeDescr` This value represents the description of the accident code, found in the `motoraccident.accident_code` field.
  * `__roadConditionDescr` This value represents the description of the road condition, found in the `motoraccident.road_cond` field.
  * `__roadTypeDescr` This value represents the description of the road type, found in the `motoraccident.road_type` field.
  * `__weatherCondDescr` This value represents the description of the weather conditions, found in the `motoraccident.weather_cond` field.
  * `__locationTypeDesc` This value represents the description of the location type, found in the `motoraccident.location_type` field.
  * `__contribFactorDescr` This value represents the description of the contributing factors, found in the `motoraccident.contrib_factor` field.
  * `__trailerConfigDescr` This value represents the description of the trailer configuration, found in the `motoraccident.trailer_config` field.
  * `__unitTypeDescr` This value represents the description of the tractor type, found in the `motoraccident.unit_type` field.

Child Elements: 
  * `[RowAccidentCost](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAccidentCost)` This element represents costs records associated with motor accident. The element contains a `__name` attribute with the value `accidentCost`.
  * `[RowWitness](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowWitness)` This element represents witness records associated with the motor accident. The element contains a `__name` attribute with the value `witness`.
  * `[RowPropertyDamage](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPropertyDamage)` This element represents property damage records associated with the motor accident. The element contains a `__name` attribute with the value `propertyDamage`.
  * `[RowPersonalInjury](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPersonalInjury)` This element represents personal injury records associated with the motor accident. The element contains a `__name` attribute with the value `personalInjury`.
  * `[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments)` This element represents comments associated with the motor accident. The element contains a `__name` attribute with the value `comments`.
  * `[RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor)` This element represent the tractor associated with the motor accident, by the `motoraccident.tractor_id` field. The element contains a `__name` attribute with the value `tractor`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` These element represent the drivers associated with the motor accident, by the `motoraccident.driver_id` field. The element contains a `__name` attribute with the value `driver`.
  * `[RowTrailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTrailer)` These element represent the trailers associated with the motor accident, by the `motoraccident.trailer)id` field. The element contains a `__name` attribute with the value `trailer`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the dispatcher associated with the motor accident, by the `motoraccident.dispatcher` field. The element contains a `__name` attribute with the value `dispatcherUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the driver manager user associated with the motor accident, by the `motoraccident.driver_mgr` field. The element contains a `__name` attribute with the value `driverManagerUser`.

## Request Details

**Endpoint:** `PUT /motorAccidents/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowMotorAccident](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMotorAccident&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /motorAccidents/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
