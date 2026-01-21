# McLeod API Documentation - /geocode

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getPosition&role=-1&service=GeocodeService

---

go back to [GeocodeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=GeocodeService&role=-1)

# GET /geocode

Gets the GPS position of an address.

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
addr1 | the first line of the address |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
addr2 | the second line of the address |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
city | the city name (required) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
state | the state code (required) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
zip | the zip (required) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Position](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.general.Position&role=-1) _of type: application/xml application/json_

a Position object if the lookup was successful, null if not

## Request Details

**Endpoint:** `GET /geocode`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /geocode HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
