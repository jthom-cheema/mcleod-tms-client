# McLeod API Documentation - /images/{rowType}/{rowId}/{documentTypeId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=addImage&role=-1&service=ImagingService

---

go back to [ImagingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ImagingService&role=-1)

# POST /images/{rowType}/{rowId}/{documentTypeId}

Stores the uploaded image into imaging. Some providers may simply stage the uploaded image and later pick it up with a batch process whereas others may immediately store it, making it ready for immediate retrieval.

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
rowType | the type of object to which the image is associated 

  * `O` \- Order
  * `M` \- Movement
  * `C` \- Customer
  * `L` \- Location
  * `P` \- Payee
  * `D` \- Driver
  * `T` \- Tractor
  * `E` \- Trailer
  * `U` \- User

|  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
rowId | the ID of the type (most likely the primary key of the row) |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
documentTypeId | the document type ID; this value must be one of the values returned in the [GET /{rowType}/{rowId}/documentTypes](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ImagingService&operation=getImageTypes) method |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
movementId | the ID of the movement associated with the row (optional) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
image | a single image sent in the body of the request |  body _of type: image/jpeg image/gif image/tiff image/png image/bmp application/pdf_ |  |  [InputStream](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.io.InputStream&role=-1)  
  
* * *

## Result

[String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)

a String containing the batch ID (if staged for later batch pickup) or the ID of the record stored in the database.

## Request Details

**Endpoint:** `POST /images/{rowType}/{rowId}/{documentTypeId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Request Body

- **Type:** [InputStream](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.io.InputStream&role=-1)
- **Content-Type:** image/jpeg image/gif image/tiff image/png image/bmp application/pdf

### Example Request

```http
POST /images/{rowType}/{rowId}/{documentTypeId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Content-Type: image/jpeg
```
