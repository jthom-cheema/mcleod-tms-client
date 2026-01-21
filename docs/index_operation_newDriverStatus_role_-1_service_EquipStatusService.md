# McLeod API Documentation - /equipStatus/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newDriverStatus&role=-1&service=EquipStatusService

---

go back to [EquipStatusService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipStatusService&role=-1)

# GET /equipStatus/new

Creates a RowDriverStatus object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[RowDriverStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverStatus&role=-1) _of type: application/xml application/json_

a RowDriverStatus record with all appropriate defaults set   
  
Additional attributes: 

  * `__eventCodeDescr` This value represents the description of the event code, found in the `equipstatus.event_code` field.

Child Elements: 
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represents the driver associated with the event, by the `equipstatus.equipment_id` field. The element contains a `__name` attribute with the value `driver`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the entered by user associated with the event, by the `equipstatus.entered_by` field. The element contains a `__name` attribute with the value `enteredByUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the driver manager user associated with the event, by the `equipstatus.driver_mgr_id` field. The element contains a `__name` attribute with the value `driverManagerUser`.

## Request Details

**Endpoint:** `GET /equipStatus/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /equipStatus/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
