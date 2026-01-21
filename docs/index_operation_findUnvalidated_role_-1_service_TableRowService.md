# McLeod API Documentation - /{table}/unvalidatedsearch

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=findUnvalidated&role=-1&service=TableRowService

---

go back to [TableRowService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&role=-1)

# GET /{table}/unvalidatedsearch

Searches the database for provided table matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
table |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
request | read for query parameters to be used as search criteria; use any combination of fields from the provided table using a prefix of the table name or no prefix.   
For example, `/order_type/search?order_type.is_active=Y` would find all active order type codes.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of the provided tables primary key+ASC will be applied. For example, `/order_type/search?order_type.id=*&orderBy=order_type.descr+DESC` would return all order_type records sorted descending by the order_type description. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/order_type/search?order_type.is_active=Y&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [ReadOnlyRow](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.data.ReadOnlyRow&role=-1) > _of type: application/xml application/json_

a list of table row objects matching the row class of the provided table.

## Request Details

**Endpoint:** `GET /{table}/unvalidatedsearch`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /{table}/unvalidatedsearch HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
