# McLeod API Documentation - /billing/transfer/{transferBy}/{transferIds}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=transferToBilling&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# POST /billing/transfer/{transferBy}/{transferIds}

Transfers the provided id values to billing.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
transferBy | Determines what id values are being provided. Valid values are: [order, customer]. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
transferIds | Comma separated list of orders or customer ids to transfer to billing |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
transferUserOnly | Transfers only billing records stamped with the authenticated user id |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf application/xml application/json_

Response object containing the transferred records and exceptions generated from the transfer

## Request Details

**Endpoint:** `POST /billing/transfer/{transferBy}/{transferIds}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
POST /billing/transfer/{transferBy}/{transferIds} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
