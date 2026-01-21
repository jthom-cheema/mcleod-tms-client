# McLeod API Documentation - /callins/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newCallin&role=-1&service=CallinService

---

go back to [CallinService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&role=-1)

# GET /callins/new

Creates a callin object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the /create method to actually insert the record in the database.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | Include a movement id value if you want to return movement related data in the callin record |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeCallinScriptDetails | Provide this parameter if you want the callin record to include callin script template details. |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[RowCallin](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallin&role=-1) _of type: application/xml application/json_

a callin record with all appropriate defaults set   
  
Additional attributes: 

  * `__callinScriptSelectionDetail` This value represents the script template selection detail from the selected callin script template.

Child Elements: 
  * `[RowCallinScriptTemplate](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallinScriptTemplate)` This element represents the callin script template associated with the callin, by the `callin.callin_script_template` field. The element contains a `__name` attribute with the value `callinScriptTemplate`.
  * `[RowCallinScriptTemplateDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallinScriptTemplateDetail)` This element represents the callin script template detail associated with the callin script template assigned to the callin, by the `callin.callin_script_template` field. The element contains a `__name` attribute with the value `callinScriptTemplateDetail`.

## Request Details

**Endpoint:** `GET /callins/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /callins/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
