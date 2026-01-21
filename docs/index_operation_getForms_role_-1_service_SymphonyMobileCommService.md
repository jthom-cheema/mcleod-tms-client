# McLeod API Documentation - /symphonymcmessages/forms

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getForms&role=-1&service=SymphonyMobileCommService

---

go back to [SymphonyMobileCommService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&role=-1)

# GET /symphonymcmessages/forms

Get all Forms

Roles that can access this endpoint are [ Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMcForm](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcForm&role=-1) > _of type: application/xml application/json_

a list of forms for the given vendor, type and ID(s)

## Request Details

**Endpoint:** `GET /symphonymcmessages/forms`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /symphonymcmessages/forms HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
