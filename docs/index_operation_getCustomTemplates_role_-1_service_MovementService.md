# McLeod API Documentation - /movements/customTemplates

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCustomTemplates&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# GET /movements/customTemplates

Retrieves a list of custom document designer templates. Used in conjunction with sending rate confirmations.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowReportTemplate](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowReportTemplate&role=-1) > _of type: application/xml application/json_

a list of DocumentDesigerTemplate objects, containing the ID and descriptio of the templates

## Request Details

**Endpoint:** `GET /movements/customTemplates`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /movements/customTemplates HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
