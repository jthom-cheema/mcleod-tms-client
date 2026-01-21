# McLeod API Documentation - /equipmentPreferences

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEquipPrefList&role=-1&service=EquipmentPreferencesService

---

go back to [EquipmentPreferencesService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipmentPreferencesService&role=-1)

#  /equipmentPreferences

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
carrierId |  |  body _of type:_ |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowDrsPayeeEquip](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayeeEquip&role=-1) >

## Request Details

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Request Body

- **Type:** [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)

### Example Request

```http
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
