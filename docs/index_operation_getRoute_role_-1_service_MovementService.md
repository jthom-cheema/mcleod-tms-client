# McLeod API Documentation - /movements/{id}/route

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getRoute&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# GET /movements/{id}/route

Retrieves the step by step route information from the connected mileage software. Based on EntryMovement.showRoute();

Roles that can access this endpoint are [ Users, Drivers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the movement ID for which to get the route |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [LegGroup](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.dsp.LegGroup&role=-1) > _of type: application/xml application/json_

a list of {@link LegGroup} objects

## Request Details

**Endpoint:** `GET /movements/{id}/route`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /movements/{id}/route HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
