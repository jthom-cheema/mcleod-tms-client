# McLeod API Documentation - /carrierOffers/{id}/legalTerms

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getLegalTerms&role=-1&service=CarrierOfferService

---

go back to [CarrierOfferService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&role=-1)

# GET /carrierOffers/{id}/legalTerms

Returns the legal terms pdf set in mobile service control.

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf_

Response object containing a pdf of the Order Offer Legal Terms.

## Request Details

**Endpoint:** `GET /carrierOffers/{id}/legalTerms`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierOffers/{id}/legalTerms HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
