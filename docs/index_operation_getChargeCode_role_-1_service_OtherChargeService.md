# McLeod API Documentation - /otherCharges/codes/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getChargeCode&role=-1&service=OtherChargeService

---

go back to [OtherChargeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OtherChargeService&role=-1)

# GET /otherCharges/codes/{id}

Retrieves the charge code specified by the ID

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the charge code to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowChargeCode](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowChargeCode&role=-1) _of type: application/xml application/json_

the requested RowChargeCode object

## Request Details

**Endpoint:** `GET /otherCharges/codes/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /otherCharges/codes/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
