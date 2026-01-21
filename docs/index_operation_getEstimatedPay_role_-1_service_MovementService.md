# McLeod API Documentation - /movements/{id}/estimatedPay

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEstimatedPay&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# GET /movements/{id}/estimatedPay

Retrieves the estimated pay for the load specified by the ID..

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the movement |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverId | ID of the driver who requested the estimated pay |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Currency](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Currency&role=-1) _of type: text/plain_

a Currency object representing the estimated pay

## Request Details

**Endpoint:** `GET /movements/{id}/estimatedPay`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
GET /movements/{id}/estimatedPay HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
