# McLeod API Documentation - /quotes/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=find&role=-1&service=QuoteService

---

go back to [QuoteService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&role=-1)

# GET /quotes/search

Finds quote records with the given criteria.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from tables: 

  * `quote` \- use `quote` or no prefix

For example, `/quotes/search?quote.bill_distance=>=100&quote.customer_id=mc*` would find quotes from customer IDs starting with 'mc' with a greater than or equal to 100 mile billing distance.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `quote.id+ASC` will be applied. For example, `/quote/search?quote.customer_id=mc*&orderBy=quote.id+DESC` would return all quotes from customer IDs starting with 'mc' sorted descending by the quote id. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/quote/search?quote.customer_id=mc*&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. **Changed After Date:** To return only records that have been changed or added since a specific date and time, you can provide the `changedAfterDate` parameter. Dates are limited to the audit setting and days to keep value in the table properties configuration. For example, `/quote/search?quote.customer_id=mc*&changedAfterDate=t-1` would return quotes from customer IDs starting with 'mc' that have been added or updated since the beginning of the previous day. **Change Types:** To further define the types of changes you want to filter, use the `changedAfterType` parameter. This parameter is to be used in conjunction with `changedAfterDate` to give the ability to specify if you want added or updated records. Allowed values: [Add, Update]. Any other value will result in an exception. If the `ChangedAfterType` parameter is not provided, both added and updated records will be returned. If you do not provide a corresponding `ChangedAfterDate` the `ChangedAfterType` parameter will be ignored. For example, `/quote/search?quote.customer_id=mc*&changedAfterDate=t-1&changedAfterType=Add` would return all quotes from customer IDs starting with 'mc' that have been added since the beginning of the previous day. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowQuote](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuote&role=-1) > _of type: application/xml application/json_

a list of quote records matching the given criteria

## Request Details

**Endpoint:** `GET /quotes/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /quotes/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
