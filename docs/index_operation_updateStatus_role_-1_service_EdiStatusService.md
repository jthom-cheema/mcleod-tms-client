# McLeod API Documentation - /ediStatus/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateStatus&role=-1&service=EdiStatusService

---

go back to [EdiStatusService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&role=-1)

# PUT /ediStatus/update

Updates a RowEdiStatus record for the given status data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
status | the data to use when updating the existing status record |  body _of type: application/xml application/json_ |  |  [RowEdiStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStatus&role=-1)  
  
* * *

## Result

[RowEdiStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStatus&role=-1) _of type: application/xml application/json_

the updated RowEdiStatus object   
  
Additional attributes: 

  * `__directionDescr` This value represents the status' direction, found in the `edistatus.direction` field.
  * `__errorDescr` This value represents the error description, found in the `edistatus.error` field.
  * `__readyToSendDescr` This value represents the ready to send description, found in the `edistatus.ready_to_send` field.
  * `__eventTypeDescr` This value represents the event type description, found in the `edistatus.event_type` field.
  * `__shipmentMatchingDescr` This value represents the shipment matching method description, found in the `edistatus.ship_match_type` field.
  * `__stopTypeDescr` This value represents the stop type description, found in the `edistatus.curr_stop_type` field.

Child Elements: 
  * `[RowEdiStatusProfile](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStatusProfile)` This element represents the EDI Shipment Status Profile associated with the status. The element contains a `__name` attribute with the value `profile`.
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represents the customer associated with the status, by the `edistatus.customer_id` field. The element contains a `__name` attribute with the value `customer`.
  * `[RowEdiMapError](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiMapError)` These elements represent the map errors associated with the status. Each element contains a `__name` attribute with the value `ediMapErrors`.
  * `[RowEdiStatusComment](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStatusComment)` These elements represent the comments associated with the status. Each element contains a `__name` attribute with the value `ediStatusComments`.
  * `[RowEdiOsd](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiOsd)` These elements represent the OS&D records associated with the status. Each element contains a `__name` attribute with the value `ediOsds`.
  * `[RowEdiBatchHistory](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBatchHistory)` These elements represent the batch history records associated with the status. Each element contains a `__name` attribute with the value `batchHistoryRecords`.

## Request Details

**Endpoint:** `PUT /ediStatus/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowEdiStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStatus&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /ediStatus/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
