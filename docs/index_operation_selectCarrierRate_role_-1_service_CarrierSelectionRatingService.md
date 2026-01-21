# McLeod API Documentation - /carrierSelectionRating/selectCarrierRate/{rateId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=selectCarrierRate&role=-1&service=CarrierSelectionRatingService

---

go back to [CarrierSelectionRatingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierSelectionRatingService&role=-1)

# POST /carrierSelectionRating/selectCarrierRate/{rateId}

Applies a specified carrier rate and books the carrier on the order.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
rateId | Billing freight group id (bfg_id value from billing_freight_group table) of the carrier rate that you want to select for the order |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
brokerageStatusCode | Brokerage status Code to assign to the movement once the carrier rate is selected. |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response object containing an HTTP response code and string representing success or failure of the web service call

## Request Details

**Endpoint:** `POST /carrierSelectionRating/selectCarrierRate/{rateId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierSelectionRating/selectCarrierRate/{rateId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
