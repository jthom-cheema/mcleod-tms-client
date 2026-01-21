# McLeod API Documentation - /partialShipment/{movementId}/resequenceManifestStops/{stopIds}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=resequenceManifestStops&role=-1&service=PartialShipmentService

---

go back to [PartialShipmentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&role=-1)

# POST /partialShipment/{movementId}/resequenceManifestStops/{stopIds}

Takes a movement id and a comma delimited list of stop id values and sequences the stops on the manifest movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | Movement id of the stops you are sequencing |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
stopIds | Comma delimited list of stop id values you are sequencing on the manifested movement. Stops will be sequenced in the order you provide the stop id values in the stopIds parameter. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1)

The manifest RowMovement object with order and stop details associated with the manifest.

## Request Details

**Endpoint:** `POST /partialShipment/{movementId}/resequenceManifestStops/{stopIds}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
POST /partialShipment/{movementId}/resequenceManifestStops/{stopIds} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
