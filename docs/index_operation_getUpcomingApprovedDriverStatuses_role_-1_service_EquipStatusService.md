# McLeod API Documentation - /equipStatus/approvedDriverStatuses

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getUpcomingApprovedDriverStatuses&role=-1&service=EquipStatusService

---

go back to [EquipStatusService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipStatusService&role=-1)

# GET /equipStatus/approvedDriverStatuses

Searches the database for approved driver status records that are upcoming or in progress and have the provided event code type.   
  

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
event_codes | a comma-delimited string used as a query parameter to determine which type of events are to be returned. A null value will return all approved, upcoming or in progress data for a given driver.   
  
Examples:   
  
The call `/equipstatus/approvedDriverStatuses?event_codes=TO` would find approved time off (TO) driver status events for the current driver that are in the future or currently in progress, based on evaluation of current date/time against the record's provided start and end time frame.   
  
The call `/equipstatus/approvedDriverStatuses?event_codes=TO,BR` would find find the data from the first example, but would also find approved bereavement leave (BR) as long as those record are also driver events for the future or are currently in progress.   
  
The call `/equipstatus/approvedDriverStatuses` would find find all approved records that are upcoming or in progress for a given driver.   
  
|  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
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

**Endpoint:** `GET /equipStatus/approvedDriverStatuses`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /equipStatus/approvedDriverStatuses HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
