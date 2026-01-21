# McLeod API Documentation - /images/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getImage&role=-1&service=ImagingService

---

go back to [ImagingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ImagingService&role=-1)

# GET /images/{id}

Retrieves the image for the given ID from Imaging. If no mimetype is supplied, we'll default it as "application/pdf" for PDF since it can handle multi-page TIFFs that imaging often contains. If you send a different type like "image/png" and the image from imaging is a multi-page TIFF, you will most likely get the first page of the TIFF, although that's not guaranteed.

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the image |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
Accept | the mimetype desired from the service call We currently support: 

  * application/pdf - PDF
  * image/tiff - TIFF
  * image/png - PNG
  * image/jpeg - JPG
  * image/gif - GIF
  * image/bmp - BMP

|  header  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf image/tiff image/png image/jpeg image/gif image/bmp_

the actual image from imaging converted as requested

## Request Details

**Endpoint:** `GET /images/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf image/tiff image/png image/jpeg image/gif image/bmp
  - Default: application/xml (if not specified)

### Example Request

```http
GET /images/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
