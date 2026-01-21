# McLeod API Documentation - /osd/detail/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newOsdDetail&role=-1&service=OSDService

---

go back to [OSDService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OSDService&role=-1)

# GET /osd/detail/new

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[RowOsdDtl](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOsdDtl&role=-1) _of type: application/xml_

## Request Details

**Endpoint:** `GET /osd/detail/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml
  - Default: application/xml (if not specified)

### Example Request

```http
GET /osd/detail/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
