# McLeod API Documentation - /tractors/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getTractorsByAdvancedSearch&role=-1&service=TractorService

---

go back to [TractorService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&role=-1)

# GET /tractors/search

Searches the database for tractors matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the location table using a prefix of `tractor` or no prefix.   
  
For example, `/tractors/search?service_status=A&tractor.current_hub=>1000000&tractor.inspection_date=<=t-100` would find active tractors with over one million miles that haven't been inspected in the last 100 days.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `tractor.id+ASC` will be applied. For example, `/tractors/search?service_status=A&orderBy=tractor.id+DESC` would return all in service tractors sorted ascending by the tractor id. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/tractors/search?tractor.id=*&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. **Changed After Date:** To return only records that have been changed or added since a specific date and time, you can provide the `changedAfterDate` parameter. Dates are limited to the audit setting and days to keep value in the table properties configuration. For example, `/tractors/search?service_status=A&changedAfterDate=t-1` would return all in service tractors that have been added or updated since the beginning of the previous day. **Change Types:** To further define the types of changes you want to filter, use the `changedAfterType` parameter. This parameter is to be used in conjunction with `changedAfterDate` to give the ability to specify if you want added or updated records. Allowed values: [Add, Update]. Any other value will result in an exception. If the `ChangedAfterType` parameter is not provided, both added and updated records will be returned. If you do not provide a corresponding `ChangedAfterDate` the `ChangedAfterType` parameter will be ignored. For example, `/tractors/search?service_status=A&changedAfterDate=t-1&changedAfterType=Add` would return all in service tractors that have been added since the beginning of the previous day. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor&role=-1) > _of type: application/xml application/json_

a list of RowTractor objects

## Request Details

**Endpoint:** `GET /tractors/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /tractors/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
