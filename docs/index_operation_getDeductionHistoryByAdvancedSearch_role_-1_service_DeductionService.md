# McLeod API Documentation - /deductions/history/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDeductionHistoryByAdvancedSearch&role=-1&service=DeductionService

---

go back to [DeductionService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&role=-1)

# GET /deductions/history/search

Searches the database for deduction history matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from tables: 

  * `drs_deduct_hist` \- use `drs_deduct_hist` or no prefix
  * `movement` \- use `movement` prefix
  * `payee` \- use `payee` prefix

For example, `/deductions/history?drs_deduct_hist.transaction_date=>=t-7&movement.loaded=L` would return deduction history records from loaded movements having a transaction date within the last 7 days.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `drs_deduct_hist.transaction_date+DESC` will be applied. For example, `/deductions/history/search?drs_deduct_hist.payee_id=*&orderBy=drs_deduct_hist.transaction_date+DESC` would return deduction history records for all payees sorted descending by transaction date. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/deductions/history/search?drs_deduct_hist.payee_id=*&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [? extends com.tms.common.lib.data.TableRow](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=? extends com.tms.common.lib.data.TableRow&role=-1) > _of type: application/xml application/json_

a list of deduction history objects

## Request Details

**Endpoint:** `GET /deductions/history/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /deductions/history/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
