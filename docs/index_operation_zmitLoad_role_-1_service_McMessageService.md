# McLeod API Documentation - /mcmessages/zmitLoad/{unitId}/{moveId}/{fuelOpt}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=zmitLoad&role=-1&service=McMessageService

---

go back to [McMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&role=-1)

# PUT /mcmessages/zmitLoad/{unitId}/{moveId}/{fuelOpt}

Zmits load information to a unit.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
unitId | ID of the MC Unit for which to send the load information macro |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
moveId | ID of the movement to be zmitted |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
fuelOpt | whether fuel optimization information should be included in zmitted macro |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)

a success/failure String to be displayed to the user

## Request Details

**Endpoint:** `PUT /mcmessages/zmitLoad/{unitId}/{moveId}/{fuelOpt}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
PUT /mcmessages/zmitLoad/{unitId}/{moveId}/{fuelOpt} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
