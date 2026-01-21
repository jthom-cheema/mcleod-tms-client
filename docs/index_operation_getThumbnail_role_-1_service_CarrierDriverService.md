# McLeod API Documentation - /carrierDriver/mobileMessage/{id}/thumbnail

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getThumbnail&role=-1&service=CarrierDriverService

---

go back to [CarrierDriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&role=-1)

# GET /carrierDriver/mobileMessage/{id}/thumbnail

Roles that can access this endpoint are [ Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
size |  |  query  |  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf image/jpeg image/gif image/tiff image/png image/bmp application/octet-stream_

## Request Details

**Endpoint:** `GET /carrierDriver/mobileMessage/{id}/thumbnail`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf image/jpeg image/gif image/tiff image/png image/bmp application/octet-stream
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierDriver/mobileMessage/{id}/thumbnail HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
