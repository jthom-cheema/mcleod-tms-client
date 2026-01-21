# McLeod API Documentation - /payees/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getPayeesByAdvancedSearch&role=-1&service=PayeeService

---

go back to [PayeeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&role=-1)

# GET /payees/search

Searches the database for locations matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from tables: 

  * `payee` \- use `payee` or no prefix
  * `drs_payee` \- use `drs_payee` or `drsPayee` prefix 

For example, `/payees/search?payee.state=AL&drsPayee.type_of=C` would find company payees in the state of Alabama.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `payee.id+DESC` will be applied. For example, `/payees/search?drsPayee.type_of=C&orderBy=payee.id+DESC` would return all company payee records sorted descending by the payee id. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/payees/search?drsPayee.type_of=C&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. **Changed After Date:** To return only records that have been changed or added since a specific date and time, you can provide the `changedAfterDate` parameter. Dates are limited to the audit setting and days to keep value in the table properties configuration. For example, `/payees/search?drsPayee.type_of=C&changedAfterDate=t-1` would return company payees that have been added or updated since the beginning of the previous day. **Change Types:** To further define the types of changes you want to filter, use the `changedAfterType` parameter. This parameter is to be used in conjunction with `changedAfterDate` to give the ability to specify if you want added or updated records. Allowed values: [Add, Update]. Any other value will result in an exception. If the `ChangedAfterType` parameter is not provided, both added and updated records will be returned. If you do not provide a corresponding `ChangedAfterDate` the `ChangedAfterType` parameter will be ignored. For example, `/payees/search?drsPayee.type_of=C&changedAfterDate=t-1&changedAfterType=Add` would return company payees that have been added since the beginning of the previous day. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee&role=-1) > _of type: application/xml application/json_

a list of RowPayee objects   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the payee status, found in the `payee.status` field.
  * `__safetyRatingDescr` This value represents the description of the safety rating, found in the `drs_payee.safety_rating` field.
  * `__brokerAuthStatusDescr` This value represents the description of the broker authority status, found in the `drs_payee.broker_auth_status` field.
  * `__commonAuthStatusDescr` This value represents the description of the common authority status, found in the `drs_payee.common_auth_status` field.
  * `__contractAuthStatusDescr` This value represents the description of the contract authority status, found in the `drs_payee.contract_auth_status` field.

Child Elements: 
  * `[RowDrsPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayee)` This element represent the drs payee associated with the payee. The element contains a `__name` attribute with the value `drsPayee`.

## Request Details

**Endpoint:** `GET /payees/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /payees/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
