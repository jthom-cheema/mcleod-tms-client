# McLeod API Documentation - /carrierDriverMessages/previewMessage

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=previewMessage&role=-1&service=CarrierDriverMessageService

---

go back to [CarrierDriverMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&role=-1)

# GET /carrierDriverMessages/previewMessage

Retrieves the composed message.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
orderId | ID of the order that the driver was assigned |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
movementId | ID of the movement that the driver was assigned |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeStopNameAddress | whether to include the name and address of all stops |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeArrivalTimes | whether to include scheduled arrival times |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeContactInformation | whether to include contact information |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeComments | whether to include dispatch and hot comments |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeReferenceNumbers | whether to include BOL and reference numbers |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeDirections | whether to include location directions |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeDirectionsDisclaimer | whether to include directions disclaimer |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeDistanceBetweenStops | whether to include distance between each stop |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeSendersOfficeNumber | whether to include the office phone number of the user sending the message |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeSendersCellNumber | whether to include the cell number of the user sending the message |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeSendersEmail | whether to include the email address of the user sending the message |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeDoNotCallNotice | whether to include Do Not Call notice |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
freeformText |  |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1) _of type: text/plain_

a String message

## Request Details

**Endpoint:** `GET /carrierDriverMessages/previewMessage`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierDriverMessages/previewMessage HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
