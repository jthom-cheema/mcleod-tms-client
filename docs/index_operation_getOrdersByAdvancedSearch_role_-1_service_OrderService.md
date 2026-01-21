# McLeod API Documentation - /orders/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getOrdersByAdvancedSearch&role=-1&service=OrderService

---

go back to [OrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&role=-1)

# GET /orders/search

Searches the database for orders matching the given request parameters.

Roles that can access this endpoint are [ Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from tables: 

  * `orders` \- use `orders` or no prefix
  * `stop` \- use `shipper` or `consignee` prefixes as appropriate
  * `customer` \- use `customer` prefix
  * `freight_group` \- use `freightGroup` prefix

For example, `/orders/search?orders.status=D&shipper.location_id=WARE*&consignee.state=AL` would find delivered orders shipping from locations starting with 'WARE' to consignees in Alabama.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `orders.id+DESC` will be applied. For example, ` /orders/search?orders.status=P&orderBy=shipper.sched_arrive_early` would return all in progress orders sorted descending by the scheduled pickup date. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/orders/search?orders.status=P&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. **Changed After Date:** To return only records that have been changed or added since a specific date and time, you can provide the `changedAfterDate` parameter. Dates are limited to the audit setting and days to keep value in the table properties configuration. For example, `/orders/search?orders.status=P&changedAfterDate=t-1` would return in progress orders that have been added or updated since the beginning of the previous day. **Change Types:** To further define the types of changes you want to filter, use the `changedAfterType` parameter. This parameter is to be used in conjunction with `changedAfterDate` to give the ability to specify if you want added or updated records. Allowed values: [Add, Update]. Any other value will result in an exception. If the `ChangedAfterType` parameter is not provided, both added and updated records will be returned. If you do not provide a corresponding `ChangedAfterDate` the `ChangedAfterType` parameter will be ignored. For example, `/orders/search?orders.status=P&changedAfterDate=t-1&changedAfterType=Add` would return in progress orders that have been added since the beginning of the previous day. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1) > _of type: application/xml application/json_

a list of RowOrders objects   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the order status, found in the `orders.status` field.
  * `__collectionMethodDescr` This value represents the description of the collection method, found in the `orders.collection_method` field.
  * `__rateTypeDescr` This value represents the description of the rate type, found in the `orders.rate_type` field.
  * `__revenueTypeDescr` This value represents the description of the revenue code, found in the `orders.revenue_code_id` field.
  * `__equipmentTypeDescr` This value represents the description of the equipment type, found in the `orders.equipment_type_id` field.
  * `__tractorTypeDescr` This value represents the description of the tractor type, found in the `orders.tractor_type` field.

Child Elements: 
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represent the customer associated with the order, by the `order.customer_id` field. The element contains a `__name` attribute with the value `customer`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the entered user associated with the order, by the `order.entered_user_id` field. The element contains a `__name` attribute with the value `enteredUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the operations user associated with the order, by the `order.operations_user` field. The element contains a `__name` attribute with the value `operationsUser`.
  * `[RowFreightGroup](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowFreightGroup)` This element represents the freight group associated with the order. The element contains a `__name` attribute with the value `freightGroup`.
  * `[RowHdrXFgp](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowHdrXFgp)` These elements represent accessorials associated with the freight group. Each element contains a `__name` attribute with the value `handlingRequirements`.
  * `[RowFreightGroupItem](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowFreightGroupItem)` These elements represent freight items associated with the freight group. Each element contains a `__name` attribute with the value `freightGroupItems`.
  * `[RevenueDetailPerFgiView](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RevenueDetailPerFgiView)` These elements represent revenue details associated with freight items. Each element contains a `__name` attribute with the value `revenueDetails`.
  * `[FgpXBfg](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.FgpXBfg)` These elements represent the billing freight groups associated with the freight group. Each element contains a `__name` attribute with the value `fgpXBfgs`.
  * `[RevenueDetailPerFgiView](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RevenueDetailPerFgiView)` These elements represent revenue details not associated with freight items. Each element contains a `__name` attribute with the value `revenueDetails`.
  * `[RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop)` These elements represent the stops associated with the order. Each element contains a `__name` attribute with the value `stops`.

## Request Details

**Endpoint:** `GET /orders/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /orders/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
