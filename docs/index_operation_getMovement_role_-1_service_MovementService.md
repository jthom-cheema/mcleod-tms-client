# McLeod API Documentation - /movements/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getMovement&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# GET /movements/{id}

Retrieves the Movement specified by the ID.

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the movement to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1) _of type: application/xml application/json_

the requested RowMovement object   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the move status, found in the `move.status` field.
  * `__overrideTypeDescr` This value represents the description of the override pay method, found in the `move.override_type` field.
  * `__brokerageStatusDescr` This value represents the description of the brokerage status, found in the `move.brokerage_status` field.
  * `__freightRevenue` This value represents the calculated freight revenue.
  * `__otherRevenue` This value represents the calculated other revenue.
  * `__totalRevenue` This value represents the calculated total revenue.
  * `__otherPay` This value represents the calculated other pay.
  * `__totalPay` This value represents the calculated total pay.
  * `__profit` This value represents the calculated profit.
  * `__profitPercentage` This value represents the calculated profit percentage.
  * `__tractor_id` This value represents the assigned tractor ID.
  * `__driver%_id` This value represents the assigned driver ID, where % is the driver number (driver1_id, driver2_id).
  * `__trailer%_id` This value represents the assigned trailer ID, where % is the trailer number (trailer1_id, etc).

Child Elements: 
  * `[RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor)` This element represent the tractor associated with the movement. The element contains a `__name` attribute with the value `tractor`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` These element represent the drivers associated with the movement. The element contains a `__name` attribute with the value `driver%`, where % is the driver number (driver1, driver2).
  * `[RowTrailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTrailer)` These element represent the trailers associated with the movement. The element contains a `__name` attribute with the value `trailer%`, where % is the trailer number (trailer1, trailer2, etc).
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the dispatcher associated with the movement, by the `movement.dispatcher_user_id` field. The element contains a `__name` attribute with the value `dispatcherUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the operations user associated with the movement, by the `movement.operations_user` field. The element contains a `__name` attribute with the value `operationsUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the fleet manager user associated with the movement, by the `movement.fleet_manager` field. The element contains a `__name` attribute with the value `fleetManagerUser`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` This element represent the carriers user associated with the movement, by the `movement.override_payee_id` field. The element contains a `__name` attribute with the value `carrier`.
  * `[RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop)` These elements represent the stops associated with the movement. Each element contains a `__name` attribute with the value `stops`.
  * `[RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders)` These elements represent the orders associated with the movement. Each element contains a `__name` attribute with the value `orders`.
  * `[RowMcUnit](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcUnit)` This element represents the mc_unit associated with the tractor or driver on the movement. The element contains a `__name` attribute with the value `mc_unit`.

## Request Details

**Endpoint:** `GET /movements/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /movements/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
