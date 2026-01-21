# McLeod API Documentation - /availableTractors/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getAvailableTractorsSearch&role=-1&service=AvailableTractorService

---

go back to [AvailableTractorService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&role=-1)

# GET /availableTractors/search

Searches the database for available tractors matching the given request parameters.

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | (Optional) The available tractor ID to search for.   
**Multiple available tractor ID values can be submitted if they are delimited with the '|' character**   
**If no value is submitted then all available tractor non extracted capacity records are eligible to be returned**   
For example, `/availableTractors/search?id=1234|5678` would find available tractors with ID 1234 and 5678   
|  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
availableDateStart | (Optional) Inclusive starting date to use as a filter of the available tractor available date   
**Defaults to current date** |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
availableDateEnd | (Optional) Inclusive ending date to use as a filter of the available tractor available date   
**Defaults to the day after the available date start**   
For example, `/availableTractors/search?availableDateStart=20191001000000CST&availableDateEnd=20191002000000CST` will find avail_tract_detail records with an available date between 10/01/2019 and 10/02/2019 |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
recordLength | (Optional) Number of records to return.   
**Defaults to the mobile_service.max_search value set in the PowerBroker Mobile Service control** |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
recordOffset | (Optional) Start of offset in the returned data result set.   
**Defaults to 0** |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowAvailTractDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAvailTractDetail&role=-1) > _of type: application/xml application/json_

A list of RowAvailTractDetail elements   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `avail_tract_detail.available_date+DESC` will be applied. 

For example, `/availableTractors/search?availableDateStart=20191001000000CST&orderBy=avail_tract_detail.carrier_id+DESC` would return all available tractors records sorted descending by the carrier id. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction`

**Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset`

For example, `/availableTractors/search?availableDateStart=20191001000000CST&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set.

  
**This search will exclude records added with the Freight Matching API as well as other interfaces that add available tractors (e.g. only include records where avail_tract_detail.extracted_capacity = 'N'** Additional results attributes: 

  * `dot_number` This value represents the DOT number of the payee, found in the `drs_payee.dot_number` field.
  * `icc_number` This value represents the MC number of the payee, found in the `drs_payee.icc_number` field.
  * `pnn_code_id` This value represents the PNN code of the tractor's equipment type, found in the `equipment_type_id.pnn_code_id` field.

## Request Details

**Endpoint:** `GET /availableTractors/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /availableTractors/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
