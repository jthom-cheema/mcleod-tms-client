# McLeod API Documentation - /dispatch/clearStop/{stopId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=clearStop&role=-1&service=DispatchService

---

go back to [DispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DispatchService&role=-1)

# POST /dispatch/clearStop/{stopId}

Clears the stop with the given dates and creates a service failure record if necessary.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
stopId | ID of the stop being cleared |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
arrivalDate | arrival date and time at stop |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
departureDate | departure date and time from stop |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
delayCode | service failure code if one should be created |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
delayComments | service failure comments |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
causedByType | type of user that caused the service failure, if one existed |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverId | driver that caused the service failure, if one existed |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
payeeId | override payee that caused the service failure, if one existed |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
userId | user that caused the service failure, if one existed |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
name | name of person that caused the service failure, if one existed |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
terminalId | terminal where the service failure, if one existed, occurred |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
isReportable | indicates if service failure, if one existed, is reportable to customer |  query  | true |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
faultOfCarrierOrDriver | indicates if service failure, if one existed, is fault of carrier or driver |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
hub | hub/odometer reading of the tractor at this stop |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response object containing an HTTP response code and string representing success or failure of the web service call

## Request Details

**Endpoint:** `POST /dispatch/clearStop/{stopId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /dispatch/clearStop/{stopId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
