# McLeod API Documentation - /carrierDriverMessages/{id}/thumbnail

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getThumbnail&role=-1&service=CarrierDriverMessageService

---

go back to [CarrierDriverMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&role=-1)

# GET /carrierDriverMessages/{id}/thumbnail

Retrieves a PNG thumbnail of the attachment stored with a message, if it exists.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the mmsMedia ID, included in the path |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
size | the size of the largest dimension; for example, if you have a 200x100 pixel image and you passed in 50 for this parameter, the thumbnail would be 50x25 |  query  |  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf image/jpeg image/gif image/tiff image/png image/bmp application/octet-stream_

a response object with a PNG thumbnail body

## Request Details

**Endpoint:** `GET /carrierDriverMessages/{id}/thumbnail`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf image/jpeg image/gif image/tiff image/png image/bmp application/octet-stream
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierDriverMessages/{id}/thumbnail HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
