# McLeod API Documentation - /carriers/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createPayee&role=-1&service=CarrierService

---

go back to [CarrierService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&role=-1)

# PUT /carriers/create

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
payee |  |  body _of type: application/xml application/json_ |  |  [RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee&role=-1)  
  
* * *

## Result

[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `PUT /carriers/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /carriers/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
