# McLeod API Documentation - /movements/{id}/declineOffer

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=declineOffer&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# POST /movements/{id}/declineOffer

Declines the movement offered to the driver.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the movement |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverId | ID of the driver who declined the offer |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
sessionId | ID of the session for the offer |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1) _of type: application/xml application/json_

a RowMovement object representing the next available movement   
  
Additional attributes: 

  * `__findNearDistance` This value represents the find near distance.
  * `__sessionId` This value represents the session id.
  * `__callInPhoneNumber` This value represents the phone number used to call in to request the load.
  * `__proratedRevenue` This value represents the prorated revenue of the load.
  * `__estimatedPay` This value represents the estimated pay for the load.

## Request Details

**Endpoint:** `POST /movements/{id}/declineOffer`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
POST /movements/{id}/declineOffer HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
