# McLeod API Documentation - /customers/{id}/agedARReport

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getAgedAR&role=-1&service=CustomerService

---

go back to [CustomerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&role=-1)

# GET /customers/{id}/agedARReport

Runs the Aged AR report for the given customer.

Roles that can access this endpoint are [ Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | customer ID for which to run the report |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
reportBy | date for which to run the report by : gl_date, bill_date, or ship_date |  query  | ship_date |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
reportType | report detail: detailed, summary or totals only |  query  | totals |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
invoiceCutoffDate | invoice cutoff date |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
paymentCutoffDate | payment cutoff date |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
ageDate | aging date |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
pastDueOnly | include past due invoices only |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeOpenCredits | include open credits |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf_

a response object containing the requested Aged AR report in PDF format

## Request Details

**Endpoint:** `GET /customers/{id}/agedARReport`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
GET /customers/{id}/agedARReport HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
