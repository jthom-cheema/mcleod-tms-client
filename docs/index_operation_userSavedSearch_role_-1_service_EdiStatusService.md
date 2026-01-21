# McLeod API Documentation - /ediStatus/userSavedSearch

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=userSavedSearch&role=-1&service=EdiStatusService

---

go back to [EdiStatusService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&role=-1)

# GET /ediStatus/userSavedSearch

Retrieves a List of RowEdiStatus objects based on an existing saved search.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
userId | string indicating the current user |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
createUserId | string indicating the user who created the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
screenClassName | string indicating the class of the screen that is related to the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
searchName | string indicating the name of the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowEdiStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStatus&role=-1) > _of type: application/xml application/json_

a list of RowEdiStatus objects   
  
Additional attributes: 

  * `__directionDescr` This value represents the status' direction, found in the `edistatus.direction` field.
  * `__errorDescr` This value represents the error description, found in the `edistatus.error` field.
  * `__readyToSendDescr` This value represents the ready to send description, found in the `edistatus.ready_to_send` field.
  * `__eventTypeDescr` This value represents the event type description, found in the `edistatus.event_type` field.
  * `__shipmentMatchingDescr` This value represents the shipment matching method description, found in the `edistatus.ship_match_type` field.
  * `__stopTypeDescr` This value represents the stop type description, found in the `edistatus.curr_stop_type` field.

Child Elements: 
  * `[RowEdiStatusProfile](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStatusProfile)` This element represents the EDI Shipment Status Profile associated with the status. The element contains a `__name` attribute with the value `profile`.

## Request Details

**Endpoint:** `GET /ediStatus/userSavedSearch`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediStatus/userSavedSearch HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
