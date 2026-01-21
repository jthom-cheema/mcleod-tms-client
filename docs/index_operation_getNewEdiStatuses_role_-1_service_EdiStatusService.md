# McLeod API Documentation - /ediStatus/retrieveRecords/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getNewEdiStatuses&role=-1&service=EdiStatusService

---

go back to [EdiStatusService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&role=-1)

# GET /ediStatus/retrieveRecords/new

Allows a partner to retrieve a List of 'new' EdiBatch objects (those not already sent to or retrieved by the partner).

Roles that can access this endpoint are [ Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
partnerId | string indicating which partner's data should be retrieved |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
altPartnerId | string indicating which partner's data should be retrieved |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
version | string indicating the version of the data to be retrieved |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
transactionSet | string indicating the type of transaction set to be retrieved |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Object](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Object&role=-1) _of type: application/xml application/json_

a list of EdiBatch objects   
  
Additional attributes: 

  * `__eventTypeDescr` This value represents the event type description, found in the `edistatus.event_type` field.
  * `__stopTypeDescr` This value represents the stop type description, found in the `edistatus.curr_stop_type` field.

## Request Details

**Endpoint:** `GET /ediStatus/retrieveRecords/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediStatus/retrieveRecords/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
