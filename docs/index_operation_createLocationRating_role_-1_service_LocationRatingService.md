# McLeod API Documentation - /locationRatings/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createLocationRating&role=-1&service=LocationRatingService

---

go back to [LocationRatingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationRatingService&role=-1)

# PUT /locationRatings/create

Creates a new Location Rating record for the given data.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
locationRating | the data to use when creating the new Location Rating |  body _of type: application/xml application/json_ |  |  [RowLocationRating](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocationRating&role=-1)  
  
* * *

## Result

[RowLocationRating](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocationRating&role=-1) _of type: application/xml application/json_

the created RowLocationRating object   
  
Child Elements: 

  * `[RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation)` This element represents the location being rated. The element contains a `__name` attribute with the value `location`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the user performing the rating. The element contains a `__name` attribute with the value `enteredByUser`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represents the driver record associated with the user performing the rating. The element contains a `__name` attribute with the value `driver`.
  * `[RowLocationRatingQuestion](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocationRatingQuestion)` This element represents a question being posed on the rating. The element contains a `__name` attribute with the value `locationRatingQuestion`. **Please note that locationRatingQuestion records are read only and cannot be saved via this API.**
  * `[RowLocationRatingAnswer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocationRatingAnswer)` This element represents the answer to its enclosing question element. The element contains a `__name` attribute with the value `locationRatingAnswer`. **Please note that locationRatingAnswer elements that do not include a numeric answer attribute from 1-5 will not be saved.**

## Request Details

**Endpoint:** `PUT /locationRatings/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowLocationRating](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocationRating&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /locationRatings/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
