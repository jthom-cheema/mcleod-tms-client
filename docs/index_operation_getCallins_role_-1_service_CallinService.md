# McLeod API Documentation - /callins/{type}/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCallins&role=-1&service=CallinService

---

go back to [CallinService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&role=-1)

# GET /callins/{type}/{id}

Retrieves a list of RowCallin records for the specified type and ID.

Roles that can access this endpoint are [ Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
type | a string representing the type of query: D = driver, T = tractor, R = carrier, O = order, M = movement |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
id | id of the record for which the query is being based (the rowType) |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowCallin](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallin&role=-1) > _of type: application/xml application/json_

a list of RowCallin records   
  
Additional attributes: 

  * `__movementStatusDescr` This value represents the description of the movement status, found in the `callin.movement_status` field.

Child Elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` These elements represent the entered by user associated with the callin. The element contains `__name` attribute with the value `enteredByUser`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` These elements represent the driver associated with the callin. The element contains `__name` attribute with the value `driver`.
  * `[RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor)` These elements represent the tractor associated with the callin. The element contains `__name` attribute with the value `tractor`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` These elements represent the carrier associated with the callin. The element contains `__name` attribute with the value `carrier`.

## Request Details

**Endpoint:** `GET /callins/{type}/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /callins/{type}/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
