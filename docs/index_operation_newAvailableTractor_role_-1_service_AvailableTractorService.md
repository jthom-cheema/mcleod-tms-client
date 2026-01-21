# McLeod API Documentation - /availableTractors/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newAvailableTractor&role=-1&service=AvailableTractorService

---

go back to [AvailableTractorService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&role=-1)

# GET /availableTractors/new

Creates an availableTractors user object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.

Roles that can access this endpoint are [ Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
carrierId | ID of the carrier for which to create the new RowAvailTractDetail record |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowAvailTractDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAvailTractDetail&role=-1) _of type: application/xml application/json_

a availableTractors record with all appropriate defaults set   
  
Additional attributes: 

  * `__equipmentTypeDescr` This value represents the description of the equipment type, found in the `tractor.equipment_type_id` field.
  * `__dispatcherUser` This value represents the name of the dispatcher, found in the `tractor.dispatcher` field.
  * `__statusDescr` This value represents the description of the status, found in the `tractor.status` field.

Child Elements: 
  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the contacts associated with the payee. The element contains a `__name` attribute with the value `contacts`.

## Request Details

**Endpoint:** `GET /availableTractors/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /availableTractors/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
