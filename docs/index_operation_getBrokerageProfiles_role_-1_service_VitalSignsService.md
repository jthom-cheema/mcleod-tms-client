# McLeod API Documentation - /vitalSigns/brokerage/profiles

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getBrokerageProfiles&role=-1&service=VitalSignsService

---

go back to [VitalSignsService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=VitalSignsService&role=-1)

# GET /vitalSigns/brokerage/profiles

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowDailyBrokProfile](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDailyBrokProfile&role=-1) > _of type: application/xml application/json_

## Request Details

**Endpoint:** `GET /vitalSigns/brokerage/profiles`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /vitalSigns/brokerage/profiles HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
