# McLeod API Documentation - /partialShipment/{movementId}/dropFromManifest/{orderIds}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=dropFromManifest&role=-1&service=PartialShipmentService

---

go back to [PartialShipmentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&role=-1)

# POST /partialShipment/{movementId}/dropFromManifest/{orderIds}

Takes a movement id and a comma delimited list of order id values to drop from existing manifest.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | Movement id of the manifest you are dropping orders from. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
orderIds | Comma delimited list of orders you want to drop from manifest. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1)

The manifest RowMovement object with order and stop details associated with the manifest.

## Request Details

**Endpoint:** `POST /partialShipment/{movementId}/dropFromManifest/{orderIds}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
POST /partialShipment/{movementId}/dropFromManifest/{orderIds} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
