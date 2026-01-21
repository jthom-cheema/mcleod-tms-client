# McLeod API Documentation - /settlements/payrollHistory

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getPayrollHistory&role=-1&service=SettlementService

---

go back to [SettlementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&role=-1)

# GET /settlements/payrollHistory

Retrieves a list of payroll history records for the given parameters.

Roles that can access this endpoint are [ Users, Drivers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
startDate | starting check date |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
endDate | ending check Date |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
checkNumber | check number |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
payeeId | the ID from the payee table (ignored when the user is not an LME user) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowDrsPayrollHist](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayrollHist&role=-1) > _of type: application/xml application/json_

a list of `[RowDrsPayrollHist](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayrollHist)` records   
  
Additional attributes: 

  * `__payrollTotalPay` the total pay for the payroll record

## Request Details

**Endpoint:** `GET /settlements/payrollHistory`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /settlements/payrollHistory HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
