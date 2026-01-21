# McLeod API Documentation - /callins/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createNewCallin&role=-1&service=CallinService

---

go back to [CallinService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&role=-1)

# PUT /callins/create

Creates a RowCallin record for the given data.

Roles that can access this endpoint are [ Users, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
callin | the data to use when creating the callin record |  body _of type: application/xml application/json_ |  |  [RowCallin](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallin&role=-1)  
latitude | the latitude of the current position when the callin was sent |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
longitude | the longitude of the current position when the callin was sent |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
accuracy | the accuracy in meters when the callin was sent |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
velocity | the velocity (speed) in mph when the callin was sent |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
course | the direction in degrees when the callin was sent |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
automated | whether the callin was sent automatically |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[RowCallin](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCallin&role=-1) _of type: application/xml application/json_

a response containing the created callin record or failure message for the request   
  
Additional attributes: 

  * `__movementStatusDescr` This value represents the description of the movement status, found in the `callin.movement_status` field.

Child Elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` These elements represent the entered by user associated with the callin. The element contains `__name` attribute with the value `enteredByUser`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` These elements represent the driver associated with the callin. The element contains `__name` attribute with the value `driver`.
  * `[RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor)` These elements represent the tractor associated with the callin. The element contains `__name` attribute with the value `tractor`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` These elements represent the carrier associated with the callin. The element contains `__name` attribute with the value `carrier`.

## Request Details

**Endpoint:** `PUT /callins/create`

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
PUT /callins/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
