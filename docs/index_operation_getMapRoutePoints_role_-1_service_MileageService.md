# McLeod API Documentation - /mileage/mapRoutePoints

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getMapRoutePoints&role=-1&service=MileageService

---

go back to [MileageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MileageService&role=-1)

# GET /mileage/mapRoutePoints

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId |  |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1) > _of type: application/xml application/json_

## Request Details

**Endpoint:** `GET /mileage/mapRoutePoints`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /mileage/mapRoutePoints HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
