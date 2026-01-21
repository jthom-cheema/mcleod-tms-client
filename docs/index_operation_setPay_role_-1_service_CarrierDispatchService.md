# McLeod API Documentation - /carrierDispatch/setPay/{movementId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=setPay&role=-1&service=CarrierDispatchService

---

go back to [CarrierDispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&role=-1)

# POST /carrierDispatch/setPay/{movementId}

Sets the carrier pay for a given movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | ID of the movement to update |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
overrideMaxPay | decimal amount by which to override the existing max pay |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
method | pay method |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
units | pay units |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
rate | per unit rate |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
carrierPay | decimal amount to set as the carrier pay |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
overrideTargetPay | decimal amount by which to override the existing max pay |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response object containing a success/failure message

## Request Details

**Endpoint:** `POST /carrierDispatch/setPay/{movementId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierDispatch/setPay/{movementId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
