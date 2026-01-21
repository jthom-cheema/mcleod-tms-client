# McLeod API Documentation - /availableTractors/add

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=addAvailableTractor&role=-1&service=AvailableTractorService

---

go back to [AvailableTractorService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&role=-1)

# PUT /availableTractors/add

Creates an availableTractors object with the specified parameter values.

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
carrierId | (**Required if iccNumber is not populated**) ID of the carrier for which to create the new RowAvailTractDetail record |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
iccNumber | (**Required if carrierId is not populated**) MC number of the carrier for which to create the new RowAvailTractDetail record |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
locationCity | (**Required**) City of where the tractor will be available |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
locationState | (**Required**) State of where the tractor will be available |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
loadToCity | (Optional) Load available tractor to this city   
**Defaults to the drs_payee.search_city_name value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
loadToState | (Optional) Load available tractor to this state   
**Defaults to the drs_payee.search_state value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
availableDate | (Optional) Start date when this tractor will be available   
**Defaults to current date** |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
expiresDate | (Optional) Date when this tractor will no longer be available   
**Defaults to current date** |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
distanceRadius | (Optional) Distance that carrier is willing to travel to pick up a load   
**There is no default value** |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
teams | (Optional) Represents if team drivers are available with this tractor   
**Defaults to false** |  query  |  |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
comments | (Optional) Comments for this available tractor   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
equipmentType | (Optional) Type of trailer available with the tractor   
Corresponds to the entries in the PowerBroker `com.tms.common.loadmaster.tablerows.RowEquipmentType` table   
**There is no default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowAvailTractDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAvailTractDetail&role=-1) _of type: application/xml application/json_

An availableTractors record with the specified parameter values and all appropriate defaults set   
  
Child Elements: 

  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the contacts associated with the carrier. 

## Request Details

**Endpoint:** `PUT /availableTractors/add`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
PUT /availableTractors/add HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
