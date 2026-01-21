# McLeod API Documentation - /ediStops/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getStop&role=-1&service=EdiStopService

---

go back to [EdiStopService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStopService&role=-1)

# GET /ediStops/{id}

Retrieves a stop and the associated reference numbers and stop notes.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the stop for which to return reference numbers |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowEdiStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStop&role=-1) _of type: application/xml application/json_

a list of RowEdiStop objects   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the stop status, found in the `stop.status` field.
  * `__typeDescr` This value represents the description of the stop type, found in the `stop.stop_type` field.
  * `__loadUnloadDescr` This value represents the description of the load/unload value, found in the `stop.driver_load_unload` field.
  * `__zoneDescr` This value represents the description of the zone, found in the `stop.zone_id` field.
  * `__directions` This value represents the stop location's directions.
  * `__loadingInstructions` This value represents the stop location's loading instructions.
  * `__unloadingInstructions` This value represents the stop location's unloading instructions.

Child Elements: 
  * `[RowReferenceNumber](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowReferenceNumber)` These elements represent the reference numbers associated with the stop. Each element contains a `__name` attribute with the value `referenceNumbers`.
  * `[RowStopNote](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStopNote)` These elements represent the stop notes associated with the stop. Each element contains a `__name` attribute with the value `stopNotes`.

## Request Details

**Endpoint:** `GET /ediStops/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediStops/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
