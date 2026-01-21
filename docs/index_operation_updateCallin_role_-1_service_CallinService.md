# McLeod API Documentation - /callins/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateCallin&role=-1&service=CallinService

---

go back to [CallinService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&role=-1)

# PUT /callins/update

Updates a callin record.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
callin | The data to use when updating an existing callin record |  body _of type: application/xml application/json_ |  |  [RowCallin](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallin&role=-1)  
  
* * *

## Result

[RowCallin](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallin&role=-1) _of type: application/xml application/json_

The updated RowCallin object   
  
Additional attributes: 

  * `__movementStatusDescr` This value represents the description of the movement status, found in the `callin.movement_status` field.

Child Elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` These elements represent the entered by user associated with the callin. The element contains `__name` attribute with the value `enteredByUser`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` These elements represent the driver associated with the callin. The element contains `__name` attribute with the value `driver`.
  * `[RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor)` These elements represent the tractor associated with the callin. The element contains `__name` attribute with the value `tractor`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` These elements represent the carrier associated with the callin. The element contains `__name` attribute with the value `carrier`.

## Request Details

**Endpoint:** `PUT /callins/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowCallin](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallin&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /callins/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
