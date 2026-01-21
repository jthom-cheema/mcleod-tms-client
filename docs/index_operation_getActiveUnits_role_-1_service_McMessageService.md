# McLeod API Documentation - /mcmessages/units

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getActiveUnits&role=-1&service=McMessageService

---

go back to [McMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&role=-1)

# GET /mcmessages/units

Retrieves all active MC Units.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMcUnit](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcUnit&role=-1) > _of type: application/xml application/json_

a list of McUnit objects

## Request Details

**Endpoint:** `GET /mcmessages/units`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /mcmessages/units HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
