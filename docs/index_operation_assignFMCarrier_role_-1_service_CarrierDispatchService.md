# McLeod API Documentation - /carrierDispatch/bookload/{movementId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=assignFMCarrier&role=-1&service=CarrierDispatchService

---

go back to [CarrierDispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&role=-1)

# POST /carrierDispatch/bookload/{movementId}

This method allows assignment of a carrier to a movement for freight matching.

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | (Required) ID of the movement to be updated |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierId | (Required if no vendor supplied mcNumber parameter) ID of the carrier to be assigned   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
mcNumber | (Required if no vendor supplied carrierId parameter) MC number of the carrier to be assigned   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierPhone | (Optional) Carrier phone number   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverName | (Optional) Override driver name   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverPhone | (Optional) Override driver phone number   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverEmail | (Optional) Override driver email   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierTractor | (Optional) Tractor number   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierTrailer | (Optional) Trailer number   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
rateConfirmationEmail | (Optional) Email recipient of the rate confirmation   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
rateAmount | (Optional) Vendor pay rate guidance   
**There is no default value** |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
dispatcherEmail | (Optional) Dispatcher email address   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
emptyTractorCity | (Optional) Empty tractor city location   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
emptyTractorState | (Optional) Empty tractor state location   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
emptyTractorZip | (Optional) Empty tractor zip location   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
emptyTractorDateTime | (Optional) Empty tractor date/time   
**There is no default value** |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

A response containing the success or failure of the assignment request   
  
Either a carrierId or a mcNumber parameter must be supplied. Both can be supplied but both cannot be omitted   
Exactly one carrier record must exist in the PowerBroker system for the given carrierId and/or mcNumber parameters.   
If multiple carrier records exist, based on the supplied carrierId and/or mcNumber parameters, a non 200 status code will be returned along with a response message stating that multiple carriers exists.   
If pay rate guidance is invalid, a non 200 status code will be returned along with a response message.   

## Request Details

**Endpoint:** `POST /carrierDispatch/bookload/{movementId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierDispatch/bookload/{movementId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
