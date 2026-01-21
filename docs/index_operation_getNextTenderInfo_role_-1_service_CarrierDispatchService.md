# McLeod API Documentation - /carrierDispatch/logisticsTender/getNextTenderInfo/{movementId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getNextTenderInfo&role=-1&service=CarrierDispatchService

---

go back to [CarrierDispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&role=-1)

# GET /carrierDispatch/logisticsTender/getNextTenderInfo/{movementId}

This method checks to see if a payee is setup to receive EDI, and if so, return basic info about the tender to be sent.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | ID of the movement for which the tender is needed |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierId | payee ID that will receive the next tender (may not be the payee currently assigned to the movement) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[EdiLogisticsTenderInfo](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.edi.EdiLogisticsTenderInfo&role=-1) _of type: application/xml application/json_

an EdiLogisticsTenderInfo object containing information for the next outbound load tender to be created

## Request Details

**Endpoint:** `GET /carrierDispatch/logisticsTender/getNextTenderInfo/{movementId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierDispatch/logisticsTender/getNextTenderInfo/{movementId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
