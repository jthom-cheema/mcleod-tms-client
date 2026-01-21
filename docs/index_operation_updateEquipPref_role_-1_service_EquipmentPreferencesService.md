# McLeod API Documentation - /equipmentPreferences/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateEquipPref&role=-1&service=EquipmentPreferencesService

---

go back to [EquipmentPreferencesService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipmentPreferencesService&role=-1)

# PUT /equipmentPreferences/update

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
updatedRow |  |  body _of type: application/xml application/json_ |  |  [RowDrsPayeeEquip](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayeeEquip&role=-1)  
  
* * *

## Result

[RowDrsPayeeEquip](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayeeEquip&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `PUT /equipmentPreferences/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowDrsPayeeEquip](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayeeEquip&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /equipmentPreferences/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
