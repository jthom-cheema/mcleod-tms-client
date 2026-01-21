# McLeod API Documentation - /mcmessages/positions

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getLatestPositions&role=-1&service=McMessageService

---

go back to [McMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&role=-1)

# GET /mcmessages/positions

Retrieves a list containing the latest position updates for all mobile units. Note, this service returns only the most recent position update for each unit.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMcPosition](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcPosition&role=-1) > _of type: application/xml application/json_

a list of McPosition objects   
  
Additional attributes: 

  * `__positionTypeDescr` This value represents the position type, found in the `mc_position.position_type` field.

Child Elements: 
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represent the driver associated with the MC Position. The element contains a `__name` attribute with the value `driver`.
  * `[RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor)` This element represent the tractor associated with the MC Position. The element contains a `__name` attribute with the value `tractor`.
  * `[RowMcMessage](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcMessage)` This element represent the mc message associated with the MC Position. The element contains a `__name` attribute with the value `message`.

## Request Details

**Endpoint:** `GET /mcmessages/positions`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /mcmessages/positions HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
