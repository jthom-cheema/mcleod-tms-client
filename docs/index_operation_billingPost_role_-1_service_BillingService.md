# McLeod API Documentation - /billing/postBills

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=billingPost&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# POST /billing/postBills

Posts provided parameter list to billing history.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
orderIds | Comma separated list of order id values to post. If no value is provided all orders will be included. |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
customerIds | Comma separated list of customer id values to post. If no value is provided all customers will be included. |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
postType | Determines what bill type to post. Valid values are: [invoice, credit, debit, summary, nosum] Defaults to nosum (all but summary). |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
billStatus | Determines what bill status to post. Valid value are: [ready, notready, both] defaults to ready. |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
shouldPost | Boolean flag to determine if transfer posts or just returns a preview report. Valid values are: [true, false] Defaults to false. |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
postUserOnly | Posts only the billing records stamped with the authenticated user id. Valid values are: [true, false] Defaults to false. |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf application/xml application/json_

a response object containing the posted records and exceptions generated from the posting.

## Request Details

**Endpoint:** `POST /billing/postBills`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
POST /billing/postBills HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
