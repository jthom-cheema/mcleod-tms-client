# McLeod API Documentation - /drivers

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCurrentMovement&role=-1&service=DriverService

---

go back to [DriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&role=-1)

#  /drivers

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id |  |  body _of type:_ |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeStops |  |  body _of type:_ |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
includeLocationRatings |  |  body _of type:_ |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1)

## Request Details

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Request Body

- **Type:** [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)

### Example Request

```http
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
