# McLeod API Documentation - /locationRatings/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getLocationRating&role=-1&service=LocationRatingService

---

go back to [LocationRatingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationRatingService&role=-1)

# GET /locationRatings/{id}

Retrieves the Location Rating for the specified ID

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID for the Location Rating to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowLocationRating](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocationRating&role=-1) _of type: application/xml application/json_

the RowLocationRating object associated with the specified ID   
  
Child Elements: 

  * `[RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation)` This element represents the location being rated. The element contains a `__name` attribute with the value `location`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the user performing the rating. The element contains a `__name` attribute with the value `enteredByUser`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represents the driver record associated with the user performing the rating. The element contains a `__name` attribute with the value `driver`.
  * `[RowLocationRatingQuestion](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocationRatingQuestion)` This element represents a question being posed on the rating. The element contains a `__name` attribute with the value `locationRatingQuestion`.
  * `[RowLocationRatingAnswer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocationRatingAnswer)` This element represents the answer to its enclosing question element. The element contains a `__name` attribute with the value `locationRatingAnswer`.

## Request Details

**Endpoint:** `GET /locationRatings/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /locationRatings/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
