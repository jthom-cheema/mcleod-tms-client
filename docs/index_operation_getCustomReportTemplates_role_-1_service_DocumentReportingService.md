# McLeod API Documentation - /documents/customTemplates

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCustomReportTemplates&role=-1&service=DocumentReportingService

---

go back to [DocumentReportingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DocumentReportingService&role=-1)

# GET /documents/customTemplates

Retrieves a list of all custom and label type document designer report templates.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the `report_template` table   
  
For example, `/documents/customTemplates?descr=mc*` would find templates having a description that starts with 'mc'. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowReportTemplate](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowReportTemplate&role=-1) > _of type: application/xml application/json_

a list of `[RowReportTemplate](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowReportTemplate)` objects   
  
Child Elements: 

  * `[RowReportVariable](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowReportVariable)` These elements represent the input variables for the given template.

## Request Details

**Endpoint:** `GET /documents/customTemplates`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /documents/customTemplates HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
