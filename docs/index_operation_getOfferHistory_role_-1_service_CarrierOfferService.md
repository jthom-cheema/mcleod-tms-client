# McLeod API Documentation - /carrierOffers/history

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getOfferHistory&role=-1&service=CarrierOfferService

---

go back to [CarrierOfferService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&role=-1)

# GET /carrierOffers/history

Retrieves a list of carrier offer history records.

Roles that can access this endpoint are [ Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowCarrierOffer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierOffer&role=-1) > _of type: application/xml application/json_

a list of `[RowCarrierOffer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierOffer)` objects, representing carrier offer history   
  
Child Elements: 

  * `[RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders)` This element represents the order associated with the carrier offer, by the `carrier_offer.order_id` field. The element contains a `__name` attribute with the value `order`.
  * `[RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop)` These elements represent the stops associated with the order. Each element contains a `__name` attribute with the value `stops`.
  * `[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement)` These elements represent the movements associated with the order. Each element contains a `__name` attribute with the value `movement`.

## Request Details

**Endpoint:** `GET /carrierOffers/history`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierOffers/history HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
