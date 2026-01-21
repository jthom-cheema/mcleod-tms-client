# McLeod API Documentation - /mobileTableConfigs/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateMobileTableConfig&role=-1&service=MobileTableConfigService

---

go back to [MobileTableConfigService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MobileTableConfigService&role=-1)

# PUT /mobileTableConfigs/update

Updates a RowMobileTableConfig record for the given data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
tableConfig | the data to use when updating the existing RowMobileTableConfig record |  body _of type: application/xml application/json_ |  |  [RowMobileTableConfig](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMobileTableConfig&role=-1)  
  
* * *

## Result

[RowMobileTableConfig](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMobileTableConfig&role=-1) _of type: application/xml application/json_

the updated RowMobileTableConfig object and associated child rows   
  
Child Elements: 

  * `[RowMobileTableConfigField](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMobileTableConfigField)` This element represents the field detail records associated with the table configuration. The element contains a `__name` attribute with the value `mobileTableConfigFields`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the user associated with the table configuration, by the `mobileTableConfig.user_id` field. The element contains a `__name` attribute with the value `enteredUser`.

## Request Details

**Endpoint:** `PUT /mobileTableConfigs/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowMobileTableConfig](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMobileTableConfig&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /mobileTableConfigs/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
