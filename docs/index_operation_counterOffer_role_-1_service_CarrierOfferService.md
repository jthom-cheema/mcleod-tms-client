# McLeod API Documentation - /carrierOffers/{id}/counter

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=counterOffer&role=-1&service=CarrierOfferService

---

go back to [CarrierOfferService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&role=-1)

# POST /carrierOffers/{id}/counter

Submits new counter offer for the given RowCarrierOffer.

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the record associated with the new offer amount |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
newAmount | amount of the carrier counter offer |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
  
* * *

## Result

[String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1) _of type: text/plain_

A String message to be displayed to the user with success/failure of submission.

## Request Details

**Endpoint:** `POST /carrierOffers/{id}/counter`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierOffers/{id}/counter HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
