# McLeod API Documentation - /partialShipment/{movementId}/addMovementsToManifest/{movementIds}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=addMovementsToManifest&role=-1&service=PartialShipmentService

---

go back to [PartialShipmentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&role=-1)

# POST /partialShipment/{movementId}/addMovementsToManifest/{movementIds}

Takes a movement id and a comma delimited list of movement id values to add to an existing manifest movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | Movement id of the manifest you are consolidating additional movements on. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
movementIds | Comma delimited list of movement id values you are adding to the manifest. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1)

The manifest RowMovement object with order and stop details associated with the manifest.

## Request Details

**Endpoint:** `POST /partialShipment/{movementId}/addMovementsToManifest/{movementIds}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
POST /partialShipment/{movementId}/addMovementsToManifest/{movementIds} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
