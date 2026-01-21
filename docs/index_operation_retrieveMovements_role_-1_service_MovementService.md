# McLeod API Documentation - /movements/retrieve

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=retrieveMovements&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# GET /movements/retrieve

Searches the database for movements matching the given request parameters. Query parameters to be used as search criteria; All parameters are optional.

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | (Optional) The movement or order to search for. Multiple movement ID and order ID values can be submitted if they are delimited with '|'   
**If no value is submitted then all movements are eligible to be returned** **There is no default value**   
For example, `/movements/retrieve?id=31473|39142` would find movements 31473 and 39142   
|  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
recordLength | (Optional) Number of records to return.   
**This value will be set to the smaller value between the vendor supplied recordLength parameter and the fmvendor_control.record_return_limit value set in the PowerBroker Freight Matching control  
  
If there is no value set in the fmvendor_control.record_return_limit field then this value will default to the mobile_service.max_search value set in the PowerBroker Mobile Service control ** |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
recordOffset | (Optional) Start of offset in the returned data result set.   
**Defaults to 0** |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1) > _of type: application/xml application/json_

a list of RowMovement objects   
  
**The response will be filtered to only return data that is represented by active records in the PowerBroker Freight Matching Control Load data output screen.  
  
**Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset`   
**There is a secondary control that may further limit the pagination results to a maximum specified by the customer.**

For example, `/carrier/retrieve?carrierId=13ERIL&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied.

  
If pagination is used the response data will include a __type 'URI' element that represents the next paginated /retrieve URI.   
If there are no more records in the paginated result set or the id parameter is populated then the response data will not include a __type 'URI' element   
If a PowerBroker movement is flagged as a freight matching override then the Powerbroker Frieght Matching control filters will be ignored and the movement will be in the results   
  
Child Elements: 

  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the dispatcher associated with the movement, by the `movement.dispatcher_user_id` field. The element contains a `__name` attribute with the value `dispatcherUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the operations user associated with the movement, by the `movement.operations_user` field. The element contains a `__name` attribute with the value `operationsUser`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` This element represent the carriers user associated with the movement, by the `movement.override_payee_id` field. The element contains a `__name` attribute with the value `carrier`.
  * `[RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop)` These elements represent the stops associated with the movement. Each element contains a `__name` attribute with the value `stops`.
  * `[RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders)` These elements represent the orders associated with the movement. Each element contains a `__name` attribute with the value `orders`.
  * `[RowFreightGroupItem](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowFreightGroupItem)` These elements represent the freight group items associated with the order Each element contains a `__name` attribute with the value `freightGroupItems`.

**

## Request Details

**Endpoint:** `GET /movements/retrieve`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /movements/retrieve HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
