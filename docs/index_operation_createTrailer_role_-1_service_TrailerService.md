# McLeod API Documentation - /trailers/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createTrailer&role=-1&service=TrailerService

---

go back to [TrailerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&role=-1)

# PUT /trailers/create

Creates a new RowTrailer record for the given data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
trailer | he data to use when creating the new trailer |  body _of type: application/xml application/json_ |  |  [RowTrailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTrailer&role=-1)  
  
* * *

## Result

[RowTrailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTrailer&role=-1) _of type: application/xml application/json_

the created RowTrailer object   
  
Additional attributes: 

  * `__fleetDescr` This value represents the description of the fleet, found in the `trailer.trailer_group` field.
  * `__trailerTypeDescr` This value represents the description of the trailer type, found in the `trailer.trailer_type` field.
  * `__currentMovementId` This value represents the ID of the trailer's current movement.

## Request Details

**Endpoint:** `PUT /trailers/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowTrailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTrailer&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /trailers/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
