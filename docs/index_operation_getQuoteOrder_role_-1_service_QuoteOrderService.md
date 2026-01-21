# McLeod API Documentation - /quoteOrders/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getQuoteOrder&role=-1&service=QuoteOrderService

---

go back to [QuoteOrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteOrderService&role=-1)

# GET /quoteOrders/{id}

Retrieves the quote-order record specified by the ID.

Roles that can access this endpoint are [ Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the quote_order to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowAbstractOrder](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAbstractOrder&role=-1) _of type: application/xml application/json_

the requested RowQuoteOrder object   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the quote_order status, found in the `quote_order.status` field.
  * `__collectionMethodDescr` This value represents the description of the collection method, found in the `quote_order.collection_method` field.
  * `__rateTypeDescr` This value represents the description of the rate type, found in the `quote_order.rate_type` field.
  * `__revenueTypeDescr` This value represents the description of the revenue code, found in the `quote_order.revenue_code_id` field.
  * `__equipmentTypeDescr` This value represents the description of the equipment type, found in the `quote_order.equipment_type_id` field.
  * `__tractorTypeDescr` This value represents the description of the tractor type, found in the `quote_order.tractor_type` field.

Child Elements: 
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represent the customer associated with the quote-order, by the `quote_order.customer_id` field. The element contains a `__name` attribute with the value `customer`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the entered user associated with the quote-order, by the `quote_order.entered_user_id` field. The element contains a `__name` attribute with the value `enteredUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the operations user associated with the quote-order, by the `quote_order.operations_user` field. The element contains a `__name` attribute with the value `operationsUser`.
  * `[RowQuoteFreightGroup](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuoteFreightGroup)` This element represents the quote-freight group associated with the quote-order. The element contains a `__name` attribute with the value `freightGroup`.
  * `[RowQuoteHdrXFgp](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuoteHdrXFgp)` These elements represent quote-accessorials associated with the quote-freight group. Each element contains a `__name` attribute with the value `handlingRequirements`.
  * `[RowQuoteFreightGroupItem](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuoteFreightGroupItem)` These elements represent quote-freight items associated with the quote-freight group. Each element contains a `__name` attribute with the value `freightGroupItems`.
  * `[QuoteRevenueDetailPerFgiView](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.QuoteRevenueDetailPerFgiView)` These elements represent quote-revenue details associated with quote-freight items. Each element contains a `__name` attribute with the value `revenueDetails`.
  * `[RowQuoteFgpXBfg](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuoteFgpXBfg)` These elements represent the quote-billing freight groups associated with the quote-freight group. Each element contains a `__name` attribute with the value `fgpXBfgs`.
  * `[QuoteRevenueDetailPerFgiView](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.QuoteRevenueDetailPerFgiView)` These elements represent quote revenue details not associated with quote-freight items. Each element contains a `__name` attribute with the value `revenueDetails`.
  * `[RowQuoteStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuoteStop)` These elements represent the quote-stops associated with the quote-order. Each element contains a `__name` attribute with the value `stops`.
  * `[RowOtherChargeQuote](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherChargeQuote)` These elements represent the quote-other charges associated with the quote-order. Each element contains a `__name` attribute with the value `otherCharges`.

## Request Details

**Endpoint:** `GET /quoteOrders/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /quoteOrders/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
