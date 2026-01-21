# McLeod API Documentation - /carriers/retrieve

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=retrieveCarriers&role=-1&service=CarrierService

---

go back to [CarrierService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&role=-1)

# GET /carriers/retrieve

Searches the database for carrier matching the given request parameters. Query parameters to be used as search criteria; All parameters are optional.

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | (Optional) The carrier ID or MC number to search for.   
**Multiple carrier ID and MC number values can be submitted if they are delimited with the '|' character**   
**If no value is submitted then all carriers are eligible to be returned**   
For example, `/carriers/retrieve?id=13ERIL|ALWALM` would find carriers 13ERIL and ALWALM   
|  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeQualifications | (Optional) Include the carrier qualification status in the response. If an override brokerage qualification profile has been set in Freight Matching control then this override profile will be used to determine the qualification status. If there is no override brokerage qualification profile set in Freight Matching control then the the brokerage dispatch control qualification profile will be used.   
**Defaults to false** |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includePrimaryContact | (Optional) Include the primary contact information in the response   
**Defaults to false** |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeLanePreferences | (Optional) Include all carrier associated PNN Lane preferences in the response   
**Defaults to false** |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeEquipmentPreferences | (Optional) Include all carrier associated equipment preferences in the response   
**Defaults to false** |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
recordLength | (Optional) Number of records to return.   
**This value will be set to the smaller value between the vendor supplied recordLength parameter and the fmvendor_control.record_return_limit value set in the PowerBroker Freight Matching control  
  
If there is no value set in the fmvendor_control.record_return_limit field then this value will default to the mobile_service.max_search value set in the PowerBroker Mobile Service control** |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
recordOffset | (Optional) Start of offset in the returned data result set.   
**Defaults to 0** |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee&role=-1) > _of type: application/xml application/json_

A list of RowPayee objects   
If pagination is used the response data will include a __type 'URI' element that represents the next paginated /retrieve URI.   
If there are no more records in the paginated result set or the id parameter is populated then the response data will not include a __type 'URI' element   
  
**Examples:**

  * `/carriers/retrieve?id=13ERIL|ZTXCNY` would find carriers 13ERIL and ZTXCNY
  * `/carriers/retrieve?id=13ERIL&includePrimaryContact=true` would find carrier 13ERIL and return the primary contact information
  * `/carriers/retrieve?id=13ERIL&includePrimaryContact=true&includeLanePreferences=true` would find carrier 13ERIL and return the primary contact information and any carrier lane preferences

**The response will be filtered to only return data that is represented by active records in the PowerBroker Freight Matching Control Carrier data output screen.**   
**Returned data will be ordered by the carrier ID value in descending order**   
  
**Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset`   
**There is a secondary control that may further limit the pagination results to a maximum specified by the customer.**

For example, `/carrier/retrieve?id=13ERIL&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied.

  
Child Elements: 

  * `[RowDrsPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayee)` This element represent the drs payee associated with the carrier. The element contains a `__name` attribute with the value `drsPayee`.
  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the primary contact associated with the payee. The element contains a `__name` attribute with the value `contacts`. *Note this is only returned if the `includePrimaryContact` Query Parameter is passed as true.
  * `[RowPnnLane](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPnnLane)` These elements represent the PNN Lanes associated with the payee. *Note this is only returned if the `includeLanePreferences` Query Parameter is passed as true and the Freight Matching control allows lane preferences to be retrieved.
  * `[RowDrsPayeeEquip](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayeeEquip)` These elements represent the preferred trailer types associated with the payee. *Note this is only returned if the `includeEquipmentPreferences` Query Parameter is passed as true and the Freight Matching control allows equipment preferences to be retrieved.
  * `[RowProhibited](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowProhibited)` These elements represent the locations and customers that have prohibited the carrier. This information is returned in the child elements `prohibitedLocations` and `prohibitedCustomers` respectively. *Note this is only returned if the Freight Matching control is set to include prohibited customer and location information

## Request Details

**Endpoint:** `GET /carriers/retrieve`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carriers/retrieve HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
