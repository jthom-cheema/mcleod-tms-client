# McLeod API Documentation - /movements/{id}/otherPay

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createDriverExtraPay&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# PUT /movements/{id}/otherPay

Creates other pay records tied to the movement record.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the movement record to which we're adding other pay records |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
otherPay | the RowDriverExtraPay object to be added to the movement |  body _of type: application/xml application/json_ |  |  [RowDriverExtraPay](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverExtraPay&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a String indicating if the operation was successful

## Request Details

**Endpoint:** `PUT /movements/{id}/otherPay`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowDriverExtraPay](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverExtraPay&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /movements/{id}/otherPay HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
