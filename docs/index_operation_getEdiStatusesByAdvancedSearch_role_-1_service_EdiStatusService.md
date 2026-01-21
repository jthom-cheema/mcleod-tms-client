# McLeod API Documentation - /ediStatus/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEdiStatusesByAdvancedSearch&role=-1&service=EdiStatusService

---

go back to [EdiStatusService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&role=-1)

# GET /ediStatus/search

Searches the database for shipment statuses matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from tables: 

  * `edistatus` \- use `edistatus` or no prefix
  * `customer` \- use `customer` prefix
  * `edistatus_profile` \- use `profile` prefix

For example, `/ediStatus/search?edistatus.partner_id=TESTPARTNER&customer.state_id=AL` would find shipment statuses for partner ID 'TESTPARTNER' where the related customer is located in Alabama.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `edistatus.order_id+ASC,edistatus.direction+DESC,profile.partner_name+ASC,edistatus.customer_id+ASC,edistatus.stop_number+ASC,edistatus.xmit_sequence+ASC,edistatus.status_code+ASC` will be applied. For example, `/ediStatus/search?edistatus.partner_id=TESTPARTNER&orderBy=customer.name+DESC` would return all edi status records for partner ID 'TESTPARTNER' sorted descending by the customer name. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` **Changed After Date:** To return only records that have been changed or added since a specific date and time, you can provide the `changedAfterDate` parameter. Dates are limited to the audit setting and days to keep value in the table properties configuration. For example, `/ediStatus/search?edistatus.partner_id=TESTPARTNER&changedAfterDate=t-1` would return all edi status records for partner ID 'TESTPARTNER' that have been added or updated since the beginning of the previous day. **Change Types:** To further define the types of changes you want to filter, use the `changedAfterType` parameter. This parameter is to be used in conjunction with `changedAfterDate` to give the ability to specify if you want added or updated records. Allowed values: [Add, Update]. Any other value will result in an exception. If the `ChangedAfterType` parameter is not provided, both added and updated records will be returned. If you do not provide a corresponding `ChangedAfterDate` the `ChangedAfterType` parameter will be ignored. For example, `/ediStatus/search?edistatus.partner_id=TESTPARTNER&changedAfterDate=t-1&changedAfterType=Add` would return all edi status records for partner ID 'TESTPARTNER' that have been added since the beginning of the previous day. For example, `/ediStatus/search?edistatus.partner_id=TESTPARTNER&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
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

**Endpoint:** `GET /ediStatus/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediStatus/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
