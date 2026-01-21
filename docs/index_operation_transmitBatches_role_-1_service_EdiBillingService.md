# McLeod API Documentation - /ediBilling/transmitBatches

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=transmitBatches&role=-1&service=EdiBillingService

---

go back to [EdiBillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&role=-1)

# POST /ediBilling/transmitBatches

Submits a transmission request for the specified EDI Billing batches for a specified profile ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
profileId | the ID of the EDI Billing profile record |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
batchInfo | a repeating parameter that identifies 1 or more EDI Billing batches to be transmitted. Each batch is defined by a batch number and a customer ID, in the format of `batch:customerId`.   
  
For example, `/ediBilling/transmitBatches?profileId=someProfileId&batchInfo=161:SOMECUST&batchInfo=162:SOMECUST` would transmit batches 161 and 162 for customer ID 'SOMECUST', for the partner defined by the profile having 'someProfileId'.   
  
Transmitting batch 0 (zero) will cause a new batch (or batches) to be created and transmitted. |  query  |  |  [EdiBatch](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.edi.EdiBatch&role=-1) (repeating)   
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a Response indicating the result of the transmission request

## Request Details

**Endpoint:** `POST /ediBilling/transmitBatches`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /ediBilling/transmitBatches HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
