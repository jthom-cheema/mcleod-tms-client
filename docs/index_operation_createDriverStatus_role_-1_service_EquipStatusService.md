# McLeod API Documentation - /equipStatus/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createDriverStatus&role=-1&service=EquipStatusService

---

go back to [EquipStatusService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipStatusService&role=-1)

# PUT /equipStatus/create

Creates a new RowDriverStatus record for the given data.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
driverStatus | the data to use when creating the new driver status event |  body _of type: application/xml application/json_ |  |  [RowDriverStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverStatus&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/xml application/json_

the created RowDriverStatus object   
  
Additional attributes: 

  * `__eventCodeDescr` This value represents the description of the event code, found in the `equipstatus.event_code` field.

Child Elements: 
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represents the driver associated with the event, by the `equipstatus.equipment_id` field. The element contains a `__name` attribute with the value `driver`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the entered by user associated with the event, by the `equipstatus.entered_by` field. The element contains a `__name` attribute with the value `enteredByUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the driver manager user associated with the event, by the `equipstatus.driver_mgr_id` field. The element contains a `__name` attribute with the value `driverManagerUser`.

## Request Details

**Endpoint:** `PUT /equipStatus/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowDriverStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverStatus&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /equipStatus/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
