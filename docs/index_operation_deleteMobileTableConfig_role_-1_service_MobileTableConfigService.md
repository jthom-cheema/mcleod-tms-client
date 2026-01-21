# McLeod API Documentation - /mobileTableConfigs/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=deleteMobileTableConfig&role=-1&service=MobileTableConfigService

---

go back to [MobileTableConfigService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MobileTableConfigService&role=-1)

# DELETE /mobileTableConfigs/{id}

Deletes the given RowMobileTableConfig and associated RowMobileTableConfigField records specified by the supplied ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the record to delete |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response containing the success or failure message for the request

## Request Details

**Endpoint:** `DELETE /mobileTableConfigs/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
DELETE /mobileTableConfigs/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
