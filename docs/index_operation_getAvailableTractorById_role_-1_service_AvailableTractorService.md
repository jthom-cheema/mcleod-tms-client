# McLeod API Documentation - /availableTractors/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getAvailableTractorById&role=-1&service=AvailableTractorService

---

go back to [AvailableTractorService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&role=-1)

# GET /availableTractors/{id}

Retrieves the RowAvailTractDetail record for the given ID.

Roles that can access this endpoint are [ Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the Available Tractor record to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowAvailTractDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAvailTractDetail&role=-1) _of type: application/xml application/json_

a RowAvailTractDetail record   
  
Additional attributes: 

  * `__equipmentTypeDescr` This value represents the description of the equipment type, found in the `tractor.equipment_type_id` field.
  * `__dispatcherUser` This value represents the name of the dispatcher, found in the `tractor.dispatcher` field.
  * `__statusDescr` This value represents the description of the status, found in the `tractor.status` field.

## Request Details

**Endpoint:** `GET /availableTractors/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /availableTractors/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
