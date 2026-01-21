# McLeod API Documentation - /orders/updateRow

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateOrderRow&role=-1&service=OrderService

---

go back to [OrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&role=-1)

# PUT /orders/updateRow

Updates a RowOrders record for the given order data. This strictly updates the order row without some validation and without updating corresponding stop and movement data. Care should be given when using this service.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
order | the data to use when updating the existing order record |  body _of type: application/xml application/json_ |  |  [RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1)  
  
* * *

## Result

[RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1) _of type: application/xml application/json_

the updated RowOrders object

## Request Details

**Endpoint:** `PUT /orders/updateRow`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /orders/updateRow HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
