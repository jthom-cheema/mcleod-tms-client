# McLeod API Documentation - /ediOrder/{id}/makeOrder

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=makeOrder&role=-1&service=EdiOrderService

---

go back to [EdiOrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&role=-1)

# PUT /ediOrder/{id}/makeOrder

Attempts to make order from a specified RowEdiOrder, as determined by the ID, without attempting to reply.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the RowEdiOrder from which the order will be created |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

Response object with Success or Failure status and status string to display to the user

## Request Details

**Endpoint:** `PUT /ediOrder/{id}/makeOrder`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
PUT /ediOrder/{id}/makeOrder HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
