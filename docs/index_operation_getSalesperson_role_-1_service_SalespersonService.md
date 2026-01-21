# McLeod API Documentation - /salespersons/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getSalesperson&role=-1&service=SalespersonService

---

go back to [SalespersonService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SalespersonService&role=-1)

# GET /salespersons/{id}

Retrieves the Salesperson requested by the ID

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the salesperson to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeContacts |  |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[RowSalesperson](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSalesperson&role=-1) _of type: application/xml application/json_

the requested Salesperson object   
  
Child Elements: 

  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the contacts associated with the salesperson. The element contains a `__name` attribute with the value `contacts`.

## Request Details

**Endpoint:** `GET /salespersons/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /salespersons/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
