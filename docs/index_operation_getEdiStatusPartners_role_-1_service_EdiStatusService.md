# McLeod API Documentation - /ediStatus/partners/{direction}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEdiStatusPartners&role=-1&service=EdiStatusService

---

go back to [EdiStatusService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&role=-1)

# GET /ediStatus/partners/{direction}

Retrieves a list of shipment status partners for a specified direction.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
direction | the direction of profiles for which information should be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [ReadOnlyRow](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.data.ReadOnlyRow&role=-1) > _of type: application/xml application/json_

a list of ReadOnlyRows containing codes (key values) and their related descriptions

## Request Details

**Endpoint:** `GET /ediStatus/partners/{direction}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediStatus/partners/{direction} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
