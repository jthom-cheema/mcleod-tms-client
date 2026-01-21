# McLeod API Documentation - /carrierSelectionRating/findCarrierRates/{orderId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=findCarrierRates&role=-1&service=CarrierSelectionRatingService

---

go back to [CarrierSelectionRatingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierSelectionRatingService&role=-1)

# POST /carrierSelectionRating/findCarrierRates/{orderId}

Initiates the carrier rating lookup for partial and LTL orders

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
orderId | ID of the order to initiate carrier rate lookup from rating engine |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowBillingFreightGroup](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowBillingFreightGroup&role=-1) > _of type: application/xml application/json_

Carrier rates and revenue details for specified order

## Request Details

**Endpoint:** `POST /carrierSelectionRating/findCarrierRates/{orderId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierSelectionRating/findCarrierRates/{orderId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
