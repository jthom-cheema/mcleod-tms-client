# McLeod API Documentation - /orders/userSavedSearch

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=userSavedSearch&role=-1&service=OrderService

---

go back to [OrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&role=-1)

# GET /orders/userSavedSearch

Retrieves a List of RowOrders objects based on an existing saved search.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
userId | string indicating the current user |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
createUserId | string indicating the user who created the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
screenClassName | string indicating the class of the screen that is related to the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
searchName | string indicating the name of the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
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

**Endpoint:** `GET /orders/userSavedSearch`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /orders/userSavedSearch HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
