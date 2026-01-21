# McLeod API Documentation - /brandings/{id}/{fieldName}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getBlob&role=-1&service=BrandingService

---

go back to [BrandingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BrandingService&role=-1)

# GET /brandings/{id}/{fieldName}

Retrieves an image stored with the branding, if it exists.

Roles that can access this endpoint are [ Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the mobile_branding ID |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
fieldName | the name of the field containing the image |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf image/jpeg image/gif image/tiff image/png image/bmp image/svg+xml application/octet-stream_

a response object with the attachment as a byte[] in the payload

## Request Details

**Endpoint:** `GET /brandings/{id}/{fieldName}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf image/jpeg image/gif image/tiff image/png image/bmp image/svg+xml application/octet-stream
  - Default: application/xml (if not specified)

### Example Request

```http
GET /brandings/{id}/{fieldName} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
