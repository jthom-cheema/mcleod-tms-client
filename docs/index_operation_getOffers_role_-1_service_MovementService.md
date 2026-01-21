# McLeod API Documentation - /movements/offers

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getOffers&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# GET /movements/offers

Retrieves a List of RowMovement objects that represent the top five available movements for a driver.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
driverId | ID of the driver for which to return offers |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1) > _of type: application/xml application/json_

a list of RowMovement objects   
  
Additional attributes: 

  * `__findNearDistance` This value represents the find near distance.
  * `__proratedRevenue` This value represents the prorated revenue of the load.
  * `__sessionId` This value represents the session id.
  * `__callInPhoneNumber` This value represents the phone number used to call in to request the load.
  * `__estimatedPay` This value represents the estimated pay for the load.
  * `__hasOverrideDistance` This flag indicates when the movement was included despite the driver's empty mileage preference.

## Request Details

**Endpoint:** `GET /movements/offers`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /movements/offers HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
