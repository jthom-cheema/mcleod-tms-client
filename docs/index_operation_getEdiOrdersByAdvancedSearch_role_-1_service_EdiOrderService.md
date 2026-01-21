# McLeod API Documentation - /ediOrder/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEdiOrdersByAdvancedSearch&role=-1&service=EdiOrderService

---

go back to [EdiOrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&role=-1)

# GET /ediOrder/search

Searches the database for load tenders matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from tables: 

  * `edi_order` \- use `edi_order` or no prefix
  * `stop` \- use `shipper` or `consignee` prefixes as appropriate
  * `customer` \- use `customer` prefix
  * `ediorder_profile` \- use `profile` prefix

For example, `/ediOrder/search?edi_order.commodity_id=FAK&shipper.location_id=WARE*&consignee.state=AL` would find load tenders with commodity ID of 'FAK' shipping from locations starting with 'WARE' to consignees in Alabama.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `edi_order.id+DESC` will be applied. For example, `/ediOrder/search?edi_order.customer_id=*&orderBy=customer.name+DESC` would return all edi order records for all customers sorted descending by the customer name. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/ediOrder/search?edi_order.customer_id=*&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. **Changed After Date:** To return only records that have been changed or added since a specific date and time, you can provide the `changedAfterDate` parameter. Dates are limited to the audit setting and days to keep value in the table properties configuration. For example, `/ediOrder/search?edi_order.edi_order.tender_status=R&changedAfterDate=t-1` would return edi orders records with a tender status of received that have been added or updated since the beginning of the previous day. **Change Types:** To further define the types of changes you want to filter, use the `changedAfterType` parameter. This parameter is to be used in conjunction with `changedAfterDate` to give the ability to specify if you want added or updated records. Allowed values: [Add, Update]. Any other value will result in an exception. If the `ChangedAfterType` parameter is not provided, both added and updated records will be returned. If you do not provide a corresponding `ChangedAfterDate` the `ChangedAfterType` parameter will be ignored. For example, `/ediOrders/search?edi_order.edi_order.tender_status=R&changedAfterDate=t-1&changedAfterType=Add` would return edi orders records with a tender status of received that have been added since the beginning of the previous day. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowEdiOrder](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiOrder&role=-1) > _of type: application/xml application/json_

a list of RowEdiOrder objects   
  
Additional attributes: 

  * `__collectionMethodDescr` This value represents the description of the collection method, found in the `edi_order.collection_method` field.
  * `__rateTypeDescr` This value represents the description of the rate type, found in the `edi_order.rate_type` field.
  * `__directionDescr` This value represents the tender direction, found in the `edi_order.direction` field.
  * `__purposeDescr` This value represents the tender purpose.
  * `__appTypeDescr` This value represents the description of the tender app type.
  * `__errorDescr` This value represents the error description, found in the `edi_order.edi_error` field.
  * `__tenderStatusDescr` This value represents the tender status description, found in the `edi_order.tender_status` field.
  * `__readyToSendDescr` This value represents the reply to sender description.
  * `__replyActionDescr` This value represents the reply action description, found in the `edi_order.reply_action` field.
  * `__requiresReply` This value represents whether a reply is required by associated EDI Order Profile.
  * `__ltxCellColor` This value represents the background color to be used in Load Tender Express.
  * `__ltxMRBColor` This value represents the Must Respond By date color to be used in Load Tender Express.
  * `__ltxTextColor` This value represents the text color to be used in Load Tender Express.

Child Elements: 
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represent the customer associated with the tender, by the `edi_order.customer_id` field. The element contains a `__name` attribute with the value `customer`.
  * `[RowEdiOrderProfile](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiOrderProfile)` This element represent the EDI Order Profile associated with the tender. The element contains a `__name` attribute with the value `profile`.
  * `[RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop)` These elements represent the stops associated with the tender. Each element contains a `__name` attribute with the value `stops`.

## Request Details

**Endpoint:** `GET /ediOrder/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediOrder/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
