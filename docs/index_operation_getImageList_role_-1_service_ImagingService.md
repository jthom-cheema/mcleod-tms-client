# McLeod API Documentation - /images/{rowType}/{rowId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getImageList&role=-1&service=ImagingService

---

go back to [ImagingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ImagingService&role=-1)

# GET /images/{rowType}/{rowId}

Retrieves a list of images available for the given type and ID.

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
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [Image](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.imaging.Image&role=-1) > _of type: application/xml application/json_

a list of images available

## Request Details

**Endpoint:** `GET /images/{rowType}/{rowId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /images/{rowType}/{rowId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
