# McLeod API Documentation - /wires/validateWire

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=validateWire&role=-1&service=WireService

---

go back to [WireService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&role=-1)

# POST /wires/validateWire

Validates a new unposted wire record without creating the record in the database.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
wire |  |  body _of type: application/xml application/json_ |  |  [RowUnpostedWire](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowUnpostedWire&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response containing a String message showing the success or failure of the wire validation

## Request Details

**Endpoint:** `POST /wires/validateWire`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowUnpostedWire](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowUnpostedWire&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
POST /wires/validateWire HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
