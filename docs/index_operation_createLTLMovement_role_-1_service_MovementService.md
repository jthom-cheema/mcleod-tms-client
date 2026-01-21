# McLeod API Documentation - /movements/createLTLMovement

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createLTLMovement&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# POST /movements/createLTLMovement

Creates an LTL movement. If a `recurringMovementId` is given, then the movement will be created from that record and all other parameters on this request will serve to override it. When this parameter is omitted, the movement type, origin, destination, departure date and transit basis are used to find a recurring movement that best matches those values. Again, all other parameters would override those values. If no recurring movement is specified or found, a new blank movement is created with the parameters from this method filling in the details.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementType | the type of movement: `PDDL` for peddle, `LINE` for linehaul |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
recurringMovementId | the ID of the recurring movement record |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
manifestName | the name of the manifest for easier search later |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
region | the name of the region |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
bullpen | the name of the bullpen in the region |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
originLocationId | the originating location used on the begin trip stop |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
destinationLocationId | the destined location used on the end trip stop |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
door | the door number for the origin |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
transitBasis | `S` for single, `T` for team |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
departure | the date and time at which the begin trip should depart |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
arrival | the date and time at which the end trip should arrive |  query  | t |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
tractor | the ID of the tractor assigned to this movement |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
trailer1 | the ID of the first trailer assigned to this movement |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driver1 | the ID of the first driver assigned to this movement |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driver2 | the ID of the second driver assigned to this movement |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1) _of type: application/xml application/json_

a RowMovement object   
  
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

**Endpoint:** `POST /movements/createLTLMovement`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
POST /movements/createLTLMovement HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
