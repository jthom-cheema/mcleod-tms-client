# McLeod API Documentation - /tractors/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newTractor&role=-1&service=TractorService

---

go back to [TractorService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&role=-1)

# GET /tractors/new

Creates a tractor object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor&role=-1) _of type: application/xml application/json_

a RowTractor record with all appropriate defaults set   
  
Additional attributes: 

  * `__fleetDescr` This value represents the description of the fleet, found in the `tractor.fleet_id` field.
  * `__payOwnerDescr` This value represents the description of the pay owner flag, found in the `tractor.pay_owner` field.
  * `__typeOfDescr` This value represents the description of the tractor type, found in the `tractor.type_of` field.
  * `__serviceStatusDescr` This value represents the description of the service status, found in the `tractor.service_status` field.
  * `__statusDescr` This value represents the description of the status, found in the `tractor.status` field.
  * `__currentMovementId` This value represents the ID of the tractor's current movement.
  * `__lastPosition` This value represents the description of the last position for the tractor.
  * `__latitude` This value represents the latitude of the last position for the tractor.
  * `__longitude` This value represents the longitude of the last position for the tractor.

Child Elements: 
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represent the primary associated with the tractor, by the `tractor.driver1_id` field. The element contains a `__name` attribute with the value `driver1`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represent the team associated with the tractor, by the `tractor.driver2_id` field. The element contains a `__name` attribute with the value `driver2`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the dispatcher associated with the tractor, by the `tractor.dispatcher` field. The element contains a `__name` attribute with the value `dispatcherUser`.

## Request Details

**Endpoint:** `GET /tractors/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /tractors/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
