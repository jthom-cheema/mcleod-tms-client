# McLeod API Documentation - /serviceFailures/serviceFailuresReport

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getServiceFailuresReport&role=-1&service=ServiceFailureService

---

go back to [ServiceFailureService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&role=-1)

# GET /serviceFailures/serviceFailuresReport

Produces a service failure report.

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
startDate | the start of the date range for the specified date type |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
endDate | the end of the date range for the specified date type |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
type | C - Customers, D - Drivers, anything else - Payees/Carriers |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
id | the ID for the specified type |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeShippers | whether to include shipper |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includePickups | whether to include pickups |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeDeliveries | whether to include deliveries |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeConsignees | whether to include consignees |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
secondarySort | H - Hours Late, O - Orders, A - Appointment Required |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
reportType | S - Summary, D - Detailed |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeComments | whether to include comments |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
showTrends | whether to show trends (including charts) |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf_

a response object containing the requested service failure report in PDF format

## Request Details

**Endpoint:** `GET /serviceFailures/serviceFailuresReport`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
GET /serviceFailures/serviceFailuresReport HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
