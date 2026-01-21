# McLeod API Documentation - /mileage/distanceToNext

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDistanceToNextStop&role=-1&service=MileageService

---

go back to [MileageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MileageService&role=-1)

# GET /mileage/distanceToNext

This method returns the distance from the current position, in latitude/longitude, to the given stop.

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
latitude | the latitude of the current position |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
longitude | the longitude of the current position |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
stopId | the ID of the stop for which to get distance to |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1) _of type: application/xml application/json_

a string value representing the distance from the current position to the given stop

## Request Details

**Endpoint:** `GET /mileage/distanceToNext`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /mileage/distanceToNext HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
