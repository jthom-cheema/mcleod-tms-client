# McLeod API Documentation - /wires

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createWire&role=-1&service=WireService

---

go back to [WireService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&role=-1)

# PUT /wires

Creates a new unposted wire record.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
zmitWire | whether we should send the driver a message that the wire was created |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
wire | a Wire object in xml format |  body _of type: application/xml application/json_ |  |  [RowUnpostedWire](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowUnpostedWire&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response containing a String message showing the success or failure of the wire creation

## Request Details

**Endpoint:** `PUT /wires`

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
PUT /wires HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
