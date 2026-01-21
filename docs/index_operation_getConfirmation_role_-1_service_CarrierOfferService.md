# McLeod API Documentation - /carrierOffers

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getConfirmation&role=-1&service=CarrierOfferService

---

go back to [CarrierOfferService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&role=-1)

#  /carrierOffers

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
rowCarrierOffer |  |  body _of type:_ |  |  [RowCarrierOffer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierOffer&role=-1)  
  
* * *

## Result

[Report](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.remote.lib.Report&role=-1)

## Request Details

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Request Body

- **Type:** [RowCarrierOffer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierOffer&role=-1)

### Example Request

```http
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
