# McLeod API Documentation - /carrierDriverMessages/sendMessage

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=sendMessage&role=-1&service=CarrierDriverMessageService

---

go back to [CarrierDriverMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&role=-1)

# POST /carrierDriverMessages/sendMessage

Sends the composed message and updates certain records (carrier_driver, order_post_hist, and movement) based on the supplied query parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
messageType | whether to send a Text message (0), Email (1), or update the records only (2) |  query  | 0 |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
driverName | recipient of the message |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
contact | recipient of the message |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
phoneNumber | phone number of the recipient |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
emailAddress | email address of the recipient |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
message | the message to be sent |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
orderId | ID of the order that the driver was assigned when the text message was sent |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
movementId | ID of the movement that the driver was assigned when the text message was sent |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

response object indicating the success or failure of sending the message

## Request Details

**Endpoint:** `POST /carrierDriverMessages/sendMessage`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierDriverMessages/sendMessage HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
