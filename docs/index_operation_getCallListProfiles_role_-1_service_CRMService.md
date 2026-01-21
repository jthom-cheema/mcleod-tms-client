# McLeod API Documentation - /crm/callListProfiles

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCallListProfiles&role=-1&service=CRMService

---

go back to [CRMService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&role=-1)

# GET /crm/callListProfiles

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowCallListProfile](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallListProfile&role=-1) > _of type: application/xml application/json_

a list of RowCallListProfile records

## Request Details

**Endpoint:** `GET /crm/callListProfiles`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /crm/callListProfiles HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
