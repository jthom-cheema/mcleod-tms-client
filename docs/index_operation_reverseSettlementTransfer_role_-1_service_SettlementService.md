# McLeod API Documentation - /settlements/reverseTransfer/{reverseTransferBy}/{reverseTransferIds}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=reverseSettlementTransfer&role=-1&service=SettlementService

---

go back to [SettlementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&role=-1)

# POST /settlements/reverseTransfer/{reverseTransferBy}/{reverseTransferIds}

Reverses a settlement for the provided transfer id values

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
reverseTransferBy | Specifies what id values are being provided. Valid values are: [order, movement, or settlement]. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
reverseTransferIds | Single or comma separated list of order, movement or settlement id to reverse a transferred settlement. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/xml application/json application/pdf_

a response object containing the transferred records and any exceptions generated from the transfer process.   
  
For example, `/settlements/reverseTransfer/order/3000546,3000547,3000548` would un-transfer orders 3000546, 3000547 and 3000548 and return a response with information about transferred records and exception details.   
  

## Request Details

**Endpoint:** `POST /settlements/reverseTransfer/{reverseTransferBy}/{reverseTransferIds}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
POST /settlements/reverseTransfer/{reverseTransferBy}/{reverseTransferIds} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
