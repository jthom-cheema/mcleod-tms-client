# McLeod API Documentation - /ediOrder/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getRowEdiOrder&role=-1&service=EdiOrderService

---

go back to [EdiOrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&role=-1)

# GET /ediOrder/{id}

Retrieves a RowEdiOrder object for the given load tender ID.

Roles that can access this endpoint are [ Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the load tender to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowEdiOrder](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiOrder&role=-1) _of type: application/xml application/json_

the requested RowEdiOrder record   
  
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
  * `[RowOtherCharge](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherCharge)` These elements represent the other charges associated with the tender. Each element contains a `__name` attribute with the value `otherCharges`.
  * `[RowEdiMapError](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiMapError)` These elements represent the map errors associated with the tender. Each element contains a `__name` attribute with the value `ediMapErrors`.
  * `[RowEdiMapError](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiMapError)` These elements represent the reply map errors associated with the tender. Each element contains a `__name` attribute with the value `replyEdiMapErrors`.
  * `[RowEdiBatchHistory](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBatchHistory)` These elements represent the batch history records associated with the tender. Each element contains a `__name` attribute with the value `batchHistoryRecords`.

## Request Details

**Endpoint:** `GET /ediOrder/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediOrder/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
