# McLeod API Documentation - /orders/createSubjectOrder

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createSubjectOrder&role=-1&service=OrderService

---

go back to [OrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&role=-1)

# PUT /orders/createSubjectOrder

Creates a RowOrders record for the given order data.

Roles that can access this endpoint are [ Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
order | the data to use when updating the existing order record |  body _of type: application/xml application/json_ |  |  [RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1)  
  
* * *

## Result

[RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1) _of type: application/xml application/json_

the created RowOrders object   
  
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
  * `[RowOtherCharge](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherCharge)` These elements represent the other charges associated with the order. Each element contains a `__name` attribute with the value `otherCharges`.
  * `[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement)` These elements represent the other charges associated with the order. Each element contains a `__name` attribute with the value `movements`.

## Request Details

**Endpoint:** `PUT /orders/createSubjectOrder`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /orders/createSubjectOrder HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
