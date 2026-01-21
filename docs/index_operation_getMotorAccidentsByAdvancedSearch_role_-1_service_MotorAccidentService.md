# McLeod API Documentation - /motorAccidents/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getMotorAccidentsByAdvancedSearch&role=-1&service=MotorAccidentService

---

go back to [MotorAccidentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&role=-1)

# GET /motorAccidents/search

Returns a list of motor accident records matching the given request parameters.

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the location table using a prefix of `motoraccident` or no prefix.   
  
For example, `/motorAccidents/search?motoraccident.driver_type=C&state=AL&motoraccident.accident_date=>=t-100` would find accidents for company drivers in the state of Alabama within the last 100 days.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `motoraccident.accident_date+DESC` will be applied. For example, `/motoraccident/search?motoraccident.driver_type=C&orderBy=motoraccident.accident_date+DESC` would return all motor accidents for company drivers sorted descending by the accident date. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/motoraccident/search?motoraccident.driver_type=C&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. **Changed After Date:** To return only records that have been changed or added since a specific date and time, you can provide the `changedAfterDate` parameter. Dates are limited to the audit setting and days to keep value in the table properties configuration. For example, `/motoraccident/search?motoraccident.driver_type=C&changedAfterDate=t-1` would return all motor accidents for company drivers that have been added or updated since the beginning of the previous day. **Change Types:** To further define the types of changes you want to filter, use the `changedAfterType` parameter. This parameter is to be used in conjunction with `changedAfterDate` to give the ability to specify if you want added or updated records. Allowed values: [Add, Update]. Any other value will result in an exception. If the `ChangedAfterType` parameter is not provided, both added and updated records will be returned. If you do not provide a corresponding `ChangedAfterDate` the `ChangedAfterType` parameter will be ignored. For example, `/motoraccident/search?motoraccident.driver_type=C&changedAfterDate=t-1&changedAfterType=Add` would return all motor accidents for company drivers that have been added since the beginning of the previous day. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMotorAccident](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMotorAccident&role=-1) > _of type: application/xml application/json_

a list of RowMotorAccident records Additional attributes: 

  * `__statusDescr` This value represents the description of the record status, found in the `motoraccident.status` field.
  * `__accidentCodeDescr` This value represents the description of the accident code, found in the `motoraccident.accident_code` field.
  * `__roadConditionDescr` This value represents the description of the road condition, found in the `motoraccident.road_cond` field.
  * `__roadTypeDescr` This value represents the description of the road type, found in the `motoraccident.road_type` field.
  * `__weatherCondDescr` This value represents the description of the weather conditions, found in the `motoraccident.weather_cond` field.
  * `__locationTypeDesc` This value represents the description of the location type, found in the `motoraccident.location_type` field.
  * `__contribFactorDescr` This value represents the description of the contributing factors, found in the `motoraccident.contrib_factor` field.
  * `__trailerConfigDescr` This value represents the description of the trailer configuration, found in the `motoraccident.trailer_config` field.
  * `__unitTypeDescr` This value represents the description of the tractor type, found in the `motoraccident.unit_type` field.

## Request Details

**Endpoint:** `GET /motorAccidents/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /motorAccidents/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
