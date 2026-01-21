# McLeod API Documentation - /ediBilling/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateBill&role=-1&service=EdiBillingService

---

go back to [EdiBillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&role=-1)

# PUT /ediBilling/update

Updates a RowEdiBilling record for the given billing data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
bill | the data to use when updating the existing EDI Billing record |  body _of type: application/xml application/json_ |  |  [RowEdiBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBilling&role=-1)  
  
* * *

## Result

[RowEdiBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBilling&role=-1) _of type: application/xml application/json_

the updated RowEdiBilling object   
  
Additional attributes: 

  * `__directionDescr` This value represents the bill's direction, found in the `edi_billing.direction` field.
  * `__errorDescr` This value represents the error description, found in the `edi_billing.error` field.
  * `__readyToSendDescr` This value represents the ready to send description, found in the `edi_billing.ready_to_send` field.
  * `__equipmentTypeDescr` This value represents the description of the equipment type, found in the `edi_billing.equipment_type_id` field.
  * `__shipmentMatchingDescr` This value represents the shipment matching method description, found in the `edi_billing.ship_match_type` field.

Child Elements: 
  * `[RowEdiBillingProfile](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBillingProfile)` This element represents the EDI Billing Profile associated with the invoice. The element contains a `__name` attribute with the value `profile`.
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represents the customer associated with the bill, by the `edi_billing.customer_id` field. The element contains a `__name` attribute with the value `customer`.
  * `[RowEdiStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStop)` These elements represent the stops associated with the invoice. Each element contains a `__name` attribute with the value `stops`.
  * `[RowOtherCharge](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherCharge)` These elements represent the other charges associated with the invoice. Each element contains a `__name` attribute with the value `otherCharges`.
  * `[RowEdiMapError](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiMapError)` These elements represent the map errors associated with the invoice. Each element contains a `__name` attribute with the value `ediMapErrors`.
  * `[RowEdiBatchHistory](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBatchHistory)` These elements represent the batch history records associated with the invoice. Each element contains a `__name` attribute with the value `batchHistoryRecords`.

## Request Details

**Endpoint:** `PUT /ediBilling/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowEdiBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBilling&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /ediBilling/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
