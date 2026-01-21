# McLeod API Documentation - /trailers/near

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getTrailersNear&role=-1&service=TrailerService

---

go back to [TrailerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&role=-1)

# GET /trailers/near

Returns {@link List} of Trailer-specific data in the form of ReadOnlyRow records, where the trailer is within 100 miles of the provided latitude and longitude.

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
latitude | Latitude point for provided location |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
longitude | Longitude point for provided location |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
distanceOut | Max distance from provided lat/long for which results will be returned. |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
queryFields | A comma-delimited string of database fields |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [ReadOnlyRow](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.data.ReadOnlyRow&role=-1) > _of type: application/xml application/json_

## Request Details

**Endpoint:** `GET /trailers/near`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /trailers/near HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
