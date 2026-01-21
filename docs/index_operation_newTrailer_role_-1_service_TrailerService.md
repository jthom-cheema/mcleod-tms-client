# McLeod API Documentation - /trailers/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newTrailer&role=-1&service=TrailerService

---

go back to [TrailerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&role=-1)

# GET /trailers/new

Creates a trailer object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[RowTrailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTrailer&role=-1) _of type: application/xml application/json_

a trailer record with all appropriate defaults set   
  
Additional attributes: 

  * `__fleetDescr` This value represents the description of the fleet, found in the `trailer.trailer_group` field.
  * `__trailerTypeDescr` This value represents the description of the trailer type, found in the `trailer.trailer_type` field.

## Request Details

**Endpoint:** `GET /trailers/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /trailers/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
