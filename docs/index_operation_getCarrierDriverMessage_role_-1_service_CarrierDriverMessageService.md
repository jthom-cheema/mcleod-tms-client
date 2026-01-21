# McLeod API Documentation - /carrierDriverMessages/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCarrierDriverMessage&role=-1&service=CarrierDriverMessageService

---

go back to [CarrierDriverMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&role=-1)

# GET /carrierDriverMessages/{id}

Retrieves the driver text message based on the specified ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the record to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowCarrierDriverMessage](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierDriverMessage&role=-1) _of type: application/xml application/json_

the requested RowCarrierDriverMessage object   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the status, found in the `carrier_driver_message.status` field.
  * `__directionDescr` This value represents the description of the direction, found in the `carrier_driver_message.direction` field.
  * `__vendorDescr` This value represents the description of the vendor, found in the `carrier_driver_message.vendor_id` field.

Child Elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the user associated with the driver text message, by the `carrier_driver_message.user_id` field. The element contains a `__name` attribute with the value `user`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represents the asset driver user associated with the driver text message, by the `carrier_driver_message.asset_driver_id` field. The element contains a `__name` attribute with the value `assetDriver`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` This element represents the carrier user associated with the driver text message, by the `carrier_driver_message.carrier_id` field. The element contains a `__name` attribute with the value `carrier`.
  * `[RowCarrierDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierDriver)` This element represents the carrier driver user associated with the driver text message, by the `carrier_driver_message.driver_id` field. The element contains a `__name` attribute with the value `carrierDriver`.
  * `[RowMmsMedia](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMmsMedia)` This element represents the media associated with the driver text message. The element contains a `__name` attribute with the value `mmsMedia`.

## Request Details

**Endpoint:** `GET /carrierDriverMessages/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierDriverMessages/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
