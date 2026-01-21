# McLeod API Documentation - /availableLoads/equipmentType

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEquipmentTypes&role=-1&service=AvailableLoadsService

---

go back to [AvailableLoadsService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableLoadsService&role=-1)

# GET /availableLoads/equipmentType

The endpoint has no roles. 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowWwwEquipmentType](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowWwwEquipmentType&role=-1) > _of type: application/xml_

## Request Details

**Endpoint:** `GET /availableLoads/equipmentType`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml
  - Default: application/xml (if not specified)

### Example Request

```http
GET /availableLoads/equipmentType HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
