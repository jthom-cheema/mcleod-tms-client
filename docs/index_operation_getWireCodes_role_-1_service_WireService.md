# McLeod API Documentation - /wires/wireServiceCodes

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getWireCodes&role=-1&service=WireService

---

go back to [WireService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&role=-1)

# GET /wires/wireServiceCodes

Retrieves a List of active wire codes.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowWireCode](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowWireCode&role=-1) > _of type: application/xml application/json_

a list of WireCode objects

## Request Details

**Endpoint:** `GET /wires/wireServiceCodes`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /wires/wireServiceCodes HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
