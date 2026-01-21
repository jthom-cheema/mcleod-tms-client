# McLeod API Documentation - /deductions/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDeductionsByAdvancedSearch&role=-1&service=DeductionService

---

go back to [DeductionService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&role=-1)

# GET /deductions/search

Searches the database for pending deductions matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from tables: 

  * `drs_pending_deduct` \- use `drs_pending_deduct` or no prefix
  * `movement` \- use `movement` prefix
  * `payee` \- use `payee` prefix

For example, `/deductions?drs_pending_deduct.ready_to_pay_flag=Y&movement.loaded=L` would return pending deduction records from loaded movements that are marked ready to pay.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `drs_pending_deduct.transaction_date+DESC` will be applied. For example, `/deductions/search?drs_pending_deduct.payee_id=*&orderBy=drs_pending_deduct.transaction_date+DESC` would return pending deduction records for all payees sorted descending by transaction date. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/deductions/search?drs_pending_deduct.payee_id=*&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowDrsPendingDeduct](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPendingDeduct&role=-1) > _of type: application/xml application/json_

a list of pending deduction objects

## Request Details

**Endpoint:** `GET /deductions/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /deductions/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
