# McLeod API Documentation - /mcmessages/units/q

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getUnitByMovementId&role=-1&service=McMessageService

---

go back to [McMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&role=-1)

# GET /mcmessages/units/q

Retrieves the proper MCUnit for the given movement. This method looks for a unit having the same ID as the tractor. If not found, then it looks for a unit having the same ID as the first driver.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | the ID of the movement |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMcUnit](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcUnit&role=-1) _of type: application/xml application/json_

the MCUnit for the given movement   
  
Additional attributes: 

  * `__isActive` This value represents whether the MC Unit is active

Child Elements: 
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represent the driver associated with the MC Unit. The element contains a `__name` attribute with the value `driver`.

@see [RowMcUnit#getRowMcUnit(RowMovement)](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcUnit#getRowMcUnit\(RowMovement\))

## Request Details

**Endpoint:** `GET /mcmessages/units/q`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /mcmessages/units/q HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
