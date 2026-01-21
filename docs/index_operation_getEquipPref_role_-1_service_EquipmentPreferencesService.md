# McLeod API Documentation - /equipmentPreferences/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEquipPref&role=-1&service=EquipmentPreferencesService

---

go back to [EquipmentPreferencesService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipmentPreferencesService&role=-1)

# GET /equipmentPreferences/{id}

Retrieve carrier preferred equipment type information.

Roles that can access this endpoint are [ Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | for the RowDrsPayeeEquip to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowDrsPayeeEquip](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayeeEquip&role=-1) _of type: application/xml application/json_

RowDrsPayeeEquip object

## Request Details

**Endpoint:** `GET /equipmentPreferences/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /equipmentPreferences/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
