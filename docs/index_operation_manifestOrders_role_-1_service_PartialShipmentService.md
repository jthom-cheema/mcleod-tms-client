# McLeod API Documentation - /partialShipment/manifestOrders/{orderIds}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=manifestOrders&role=-1&service=PartialShipmentService

---

go back to [PartialShipmentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&role=-1)

# POST /partialShipment/manifestOrders/{orderIds}

Takes a list of order id values and consolidates all stops into a single manifest movement. All provided order records and associated movements must be unconsolidated and in available status.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
orderIds | Comma separated list of order id values to consolidate into a single movement |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1)

the created RowMovement object with order and stop details associated with the manifest.

## Request Details

**Endpoint:** `POST /partialShipment/manifestOrders/{orderIds}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
POST /partialShipment/manifestOrders/{orderIds} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
