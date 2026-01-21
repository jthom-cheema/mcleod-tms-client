# McLeod API Documentation - /images/{rowType}/{rowId}/documentTypes

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getImageTypes&service=ImagingService

---

go back to [ImagingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ImagingService&role=-1)  
  
# GET /images/{rowType}/{rowId}/documentTypes

Gets the list of document types available for the row.

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
movementId | the ID of the movement associated with the row (optional) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [ImageType](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.imaging.ImageType&role=-1) > _of type: application/xml application/json_

a list of DocumentType objects

## Request Details

**Endpoint:** `GET /images/{rowType}/{rowId}/documentTypes`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /images/{rowType}/{rowId}/documentTypes HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
