# McLeod API Documentation - /orders/autorate/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=autorate&role=-1&service=OrderService

---

go back to [OrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&role=-1)

# POST /orders/autorate/{id}

Performs autorate operation on provided order id.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the order to be autorated |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowAbstractOrder](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAbstractOrder&role=-1) _of type: application/xml application/json application/pdf_

Returns the autorated order record and any other charges associated to the order.

## Request Details

**Endpoint:** `POST /orders/autorate/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
POST /orders/autorate/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
