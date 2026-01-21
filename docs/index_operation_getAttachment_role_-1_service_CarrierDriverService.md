# McLeod API Documentation - /carrierDriver/mobileMessage/{id}/attachment

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getAttachment&role=-1&service=CarrierDriverService

---

go back to [CarrierDriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&role=-1)

# GET /carrierDriver/mobileMessage/{id}/attachment

Retrieves an attachment stored with an order history record, if it exists.

Roles that can access this endpoint are [ Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the order history id, included in the path |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf image/jpeg image/gif image/tiff image/png image/bmp application/octet-stream_

a Response object with the attachment as a byte array in the body

## Request Details

**Endpoint:** `GET /carrierDriver/mobileMessage/{id}/attachment`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf image/jpeg image/gif image/tiff image/png image/bmp application/octet-stream
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierDriver/mobileMessage/{id}/attachment HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
