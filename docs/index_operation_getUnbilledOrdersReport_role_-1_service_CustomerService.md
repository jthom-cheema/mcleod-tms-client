# McLeod API Documentation - /customers/{id}/unbilledOrdersReport

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getUnbilledOrdersReport&role=-1&service=CustomerService

---

go back to [CustomerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&role=-1)

# GET /customers/{id}/unbilledOrdersReport

Produces an unbilled orders report for the customer specified. As this is expected to be run from the customer screen, no range filter is given to select a range of customers and no option is given to allow sorting by customer.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | customer ID for which to run the report |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
reportBy | S - Ship Date, D - Delivery Date |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
cutoffDate | last date used when calculating revenue |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
transferStatus | T - Transferred, U - Untransferred, A - All |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeVoided | whether to include voided orders |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf_

a response containing the unbilled orders report in PDF format

## Request Details

**Endpoint:** `GET /customers/{id}/unbilledOrdersReport`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
GET /customers/{id}/unbilledOrdersReport HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
