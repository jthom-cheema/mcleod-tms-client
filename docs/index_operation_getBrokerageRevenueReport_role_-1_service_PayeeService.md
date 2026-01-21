# McLeod API Documentation - /payees/{id}/revenueReport

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getBrokerageRevenueReport&role=-1&service=PayeeService

---

go back to [PayeeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&role=-1)

# GET /payees/{id}/revenueReport

Generates a brokerage revenue report for the specified carrier, date range, etc.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the payee/carrier |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
dateType | S - Ship Date, D - Delivery Date, anything else - Bill Date |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
startDate | the start of the date range for the specified date type |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
endDate | the end of the date range for the specified date type |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
groupBy | c - Customer, a - Carrier, d - Dispatcher, r - Revenue Code, anything else - Controlling Party |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
sortBy | secondary sort; B - Bill Date, D - Delivery Date, anything else - Order number |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
reportType | S - Summary, D - Detailed |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
statusDelivered | whether to include delivered movements |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
statusAvailable | whether to include available movements |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
statusInProgress | whether to include in progress movements |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf_

a response object containing the requested brokerage revenue report in PDF format

## Request Details

**Endpoint:** `GET /payees/{id}/revenueReport`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
GET /payees/{id}/revenueReport HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
