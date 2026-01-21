# McLeod API Documentation - /vitalSigns/image

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getAssetImage&role=-1&service=VitalSignsService

---

go back to [VitalSignsService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=VitalSignsService&role=-1)

# GET /vitalSigns/image

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id |  |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
imageName |  |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: image/jpeg image/gif image/tiff image/png image/bmp application/octet-stream_

## Request Details

**Endpoint:** `GET /vitalSigns/image`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** image/jpeg image/gif image/tiff image/png image/bmp application/octet-stream
  - Default: application/xml (if not specified)

### Example Request

```http
GET /vitalSigns/image HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: image/jpeg
```
