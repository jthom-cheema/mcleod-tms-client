# McLeod API Documentation - /locationRatings/{locationId}/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newLocationRating&role=-1&service=LocationRatingService

---

go back to [LocationRatingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationRatingService&role=-1)

# GET /locationRatings/{locationId}/new

Creates a Location Rating object with all configured defaults set. This DOES NOT create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
locationId | the id of the location being rated |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowLocationRating](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocationRating&role=-1) _of type: application/xml application/json_

a RowLocationRating object with all appropriate defaults set   
  
When the calling user has previously rated the specified location, the RowLocationRating instance that is returned will include the values supplied on the most recent of their previous ratings for the location. The questions included in the RowLocationRating instance will always be those currently marked for display. However, if the most recent review provided an answer to any of those questions, those answers will be included.

## Request Details

**Endpoint:** `GET /locationRatings/{locationId}/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /locationRatings/{locationId}/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
