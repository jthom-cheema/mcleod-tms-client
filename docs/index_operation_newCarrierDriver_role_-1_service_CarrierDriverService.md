# McLeod API Documentation - /carrierDriver/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newCarrierDriver&role=-1&service=CarrierDriverService

---

go back to [CarrierDriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&role=-1)

# GET /carrierDriver/new

Roles that can access this endpoint are [ Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[RowCarrierDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierDriver&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `GET /carrierDriver/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierDriver/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
