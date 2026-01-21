# McLeod API Documentation - /mobileTableConfigs/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getMobileTableConfig&role=-1&service=MobileTableConfigService

---

go back to [MobileTableConfigService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MobileTableConfigService&role=-1)

# GET /mobileTableConfigs/{id}

Retrieves the table configuration based on the specified ID for the logged in user.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the record to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMobileTableConfig](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMobileTableConfig&role=-1) _of type: application/xml application/json_

the requested RowMobileTableConfig object   
  
Child Elements: 

  * `[RowMobileTableConfigField](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMobileTableConfigField)` This element represents field detail records associated with the table configuration. The element contains a `__name` attribute with the value `mobileTableConfigFields`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the user associated with the table configuration, by the `mobileTableConfig.user_id` field. The element contains a `__name` attribute with the value `enteredUser`.

## Request Details

**Endpoint:** `GET /mobileTableConfigs/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /mobileTableConfigs/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
