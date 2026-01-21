# McLeod API Documentation - /cities/findNearestCity

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=findNearestCity&role=-1&service=CityService

---

go back to [CityService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CityService&role=-1)

# GET /cities/findNearestCity

Finds the nearest RowCity given a latitude and longitude. This method queries all records from the city table that are within a pretend fence around the latitude and longitude.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
latitude | the latitude of the point which we want to find nearest city |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
longitude | the longitude of the point which we want to find nearest city |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
fence | the number of degrees from the latitude/longitude to which we will limit the city search. fence values > 2 (App: 120 miles) are not allowed. |  query  | .25 |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowCity](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCity&role=-1) _of type: application/xml application/json_

the RowCity object for the nearest city using GreatCircleMath   
  
For example, `/cities/findNearestCity?latitude=42.434700&longitude=83.984700?fence=.25 would find a single city that is closest to the provided latitude and longitude within .25 degrees. **Note:** Omitting the fence parameter will default to .25 (App: 15 miles).   
  
`

## Request Details

**Endpoint:** `GET /cities/findNearestCity`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /cities/findNearestCity HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
