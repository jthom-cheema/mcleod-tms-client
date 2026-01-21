# McLeod API Documentation - /orders/{id}/duplicate

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=duplicate&role=-1&service=OrderService

---

go back to [OrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&role=-1)

# POST /orders/{id}/duplicate

Creates duplicate copies of the original order, based on supplied parameters.

Roles that can access this endpoint are [ Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the original order for which to copy |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
numCopies | the number of copies to create (must be between 1 and 25) |  query  |  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
includeRate | copy rating information to new orders |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
includeOtherCharges | copy other charges to new orders |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
includeCarrierCost | copy carrier costs to new orders (LTL only) |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
includeHandlingRequirements | copy carrier handling requirements to new orders (LTL only) |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
addToMasterOrder | add new orders to existing master order (Container only) |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1) >

a list of `[RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders)` objects   
  
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
  * `[RowFreightGroup](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowFreightGroup)` This element represents the freight group associated with the order. The element contains a `__name` attribute with the value `freightGroup`.
  * `[RowHdrXFgp](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowHdrXFgp)` These elements represent accessorials associated with the freight group. Each element contains a `__name` attribute with the value `handlingRequirements`.
  * `[RowFreightGroupItem](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowFreightGroupItem)` These elements represent freight items associated with the freight group. Each element contains a `__name` attribute with the value `freightGroupItems`.
  * `[RevenueDetailPerFgiView](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RevenueDetailPerFgiView)` These elements represent revenue details associated with freight items. Each element contains a `__name` attribute with the value `revenueDetails`.
  * `[FgpXBfg](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.FgpXBfg)` These elements represent the billing freight groups associated with the freight group. Each element contains a `__name` attribute with the value `fgpXBfgs`.
  * `[RevenueDetailPerFgiView](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RevenueDetailPerFgiView)` These elements represent revenue details not associated with freight items. Each element contains a `__name` attribute with the value `revenueDetails`.
  * `[RowStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowStop)` These elements represent the stops associated with the order. Each element contains a `__name` attribute with the value `stops`.
  * `[RowOtherCharge](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherCharge)` These elements represent the other charges associated with the order. Each element contains a `__name` attribute with the value `otherCharges`.
  * `[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement)` These elements represent the other charges associated with the order. Each element contains a `__name` attribute with the value `movements`.

## Request Details

**Endpoint:** `POST /orders/{id}/duplicate`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Example Request

```http
POST /orders/{id}/duplicate HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
