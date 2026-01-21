# McLeod API Documentation - /carrierDriverMessages/{id}/resend

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=resendMessage&role=-1&service=CarrierDriverMessageService

---

go back to [CarrierDriverMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&role=-1)

# POST /carrierDriverMessages/{id}/resend

Resends the driver text message with the specified ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the record to be resent |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

response object indicating the success or failure of sending the message

## Request Details

**Endpoint:** `POST /carrierDriverMessages/{id}/resend`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /carrierDriverMessages/{id}/resend HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
