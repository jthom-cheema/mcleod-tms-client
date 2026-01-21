# McLeod API Documentation - /salespersons/{id}/commissionReport

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getSalespersonCommission&role=-1&service=SalespersonService

---

go back to [SalespersonService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SalespersonService&role=-1)

# GET /salespersons/{id}/commissionReport

Produces a salesperson commission report for the salesperson ID specified.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the salesperson for whom the report is run |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
reportType | S - Summary, D - Detailed |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
dateType | B - Bill Date, D - Delivery Date, anything else - Ship Date |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
startDate | the start of the date range for the specified date type |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
endDate | the end of the date range for the specified date type |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf_

a response object containing the salesperson commission report in PDF format

## Request Details

**Endpoint:** `GET /salespersons/{id}/commissionReport`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
GET /salespersons/{id}/commissionReport HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
