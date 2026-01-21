# McLeod API Documentation - /ediOsds/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEdiOsd&role=-1&service=EdiOsdService

---

go back to [EdiOsdService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOsdService&role=-1)

# GET /ediOsds/{id}

Retrieves a RowEdiOsd record based on the ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the EDI OS&D record to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowEdiOsd](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiOsd&role=-1) _of type: application/xml application/json_

a RowEdiOsd object   
  
Additional attributes: 

  * `__codeDescr` This value represents the description of the OS&D codes, found in the `edi_osd.code` field.
  * `__qualifierDescr` This value represents the description of the OS&D qualifiers, found in the `edi_osd.qualifier` field.

## Request Details

**Endpoint:** `GET /ediOsds/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediOsds/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
