# McLeod API Documentation - /equipStatus/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDriverStatus&role=-1&service=EquipStatusService

---

go back to [EquipStatusService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipStatusService&role=-1)

# GET /equipStatus/search

Searches the database for driver status events matching the given request parameters.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the `equipstatus` table   
  
For example, `/equipstatus/search?event_code=TO&event_status=A&start_date=>t` would find approved time off (TO) driver status events for the current driver that starts after today. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowDriverStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverStatus&role=-1) > _of type: application/xml application/json_

a list of `[RowDriverStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverStatus)` objects   
  
Additional attributes: 

  * `__eventCodeDescr` This value represents the description of the event code, found in the `equipstatus.event_code` field.

Child Elements: 
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represents the driver associated with the event, by the `equipstatus.equipment_id` field. The element contains a `__name` attribute with the value `driver`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the entered by user associated with the event, by the `equipstatus.entered_by` field. The element contains a `__name` attribute with the value `enteredByUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the driver manager user associated with the event, by the `equipstatus.driver_mgr_id` field. The element contains a `__name` attribute with the value `driverManagerUser`.

## Request Details

**Endpoint:** `GET /equipStatus/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /equipStatus/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
