# McLeod API Documentation - /partialShipment/manifestMovements/{movementIds}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=manifestMovements&role=-1&service=PartialShipmentService

---

go back to [PartialShipmentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&role=-1)

# POST /partialShipment/manifestMovements/{movementIds}

Takes a comma delimited list of movement id values and consolidates all stops into a single manifest movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementIds | Comma separated list of movement id values to consolidate into a single movement |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1)

the created RowMovement object with order and stop details associated with the manifest.

## Request Details

**Endpoint:** `POST /partialShipment/manifestMovements/{movementIds}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
POST /partialShipment/manifestMovements/{movementIds} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
