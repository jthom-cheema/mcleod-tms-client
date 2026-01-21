# McLeod API Documentation - /orders/{id}/convertSubjectOrder

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=convertSubjectOrder&role=-1&service=OrderService

---

go back to [OrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&role=-1)

# POST /orders/{id}/convertSubjectOrder

Converts a subject order to an order.

Roles that can access this endpoint are [ Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | of the order to be converted |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1)

the created RowOrders object

## Request Details

**Endpoint:** `POST /orders/{id}/convertSubjectOrder`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
POST /orders/{id}/convertSubjectOrder HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
