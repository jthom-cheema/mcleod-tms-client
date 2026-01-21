# McLeod API Documentation - /carrierOffers/offerTerms

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getOfferTerms&role=-1&service=CarrierOfferService

---

go back to [CarrierOfferService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&role=-1)

# GET /carrierOffers/offerTerms

Returns the order offer terms set in mobile service control. Currently, this only returns limited fields.

The endpoint has no roles. 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMobileService](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMobileService&role=-1) > _of type: application/xml_

A MobileService record

## Request Details

**Endpoint:** `GET /carrierOffers/offerTerms`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierOffers/offerTerms HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
