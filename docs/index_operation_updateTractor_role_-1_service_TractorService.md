# McLeod API Documentation - /tractors/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateTractor&role=-1&service=TractorService

---

go back to [TractorService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&role=-1)

# PUT /tractors/update

Updates a RowTractor record for the given data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
tractor | the data to use when updating the existing Tractor record |  body _of type: application/xml application/json_ |  |  [RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor&role=-1)  
includeComments | if related Comment records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor&role=-1) _of type: application/xml application/json_

the updated RowTractor record   
  
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
  * `[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments)` These elements represent the comments associated with the tractor. The element contains a `__name` attribute with the value `comments`. *Note this is only returned if the `includeComments` Query Parameter is passed as true.

## Request Details

**Endpoint:** `PUT /tractors/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /tractors/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
