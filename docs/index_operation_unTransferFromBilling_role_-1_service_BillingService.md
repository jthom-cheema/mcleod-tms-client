# McLeod API Documentation - /billing/unTransfer/{orderId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=unTransferFromBilling&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# POST /billing/unTransfer/{orderId}

Removes existing billing record and sets order back to untransferred status.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
orderId | Order id to untransfer from billing |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

String representation of success or failure of the untransfer process.

## Request Details

**Endpoint:** `POST /billing/unTransfer/{orderId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /billing/unTransfer/{orderId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
