# McLeod API Documentation - /settlements/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createSettlement&role=-1&service=SettlementService

---

go back to [SettlementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&role=-1)

# PUT /settlements/create

Creates a new settlement record for the given data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
settlement | the data to use when creating the new settlement |  body _of type: application/xml application/json_ |  |  [RowSettlement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSettlement&role=-1)  
  
* * *

## Result

[RowSettlement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSettlement&role=-1) _of type: application/xml application/json_

returns the created settlement record   
  
Additional attributes: 

  * `__payMethodDescr` This value represents the description of the pay method, found in the `settlement.pay_method` field.
  * `__payeeTypeDescr` This value represents the description of the payee type.
  * `__commodityIdDescr` This value represents the description of the commodity, found in the `settlement.commodity_id` field.
  * `__revenueIdDescr` This value represents the description of the revenue code, found in the `settlement.revenue_id` field.

Child Elements:   
  

  * `[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement)` This element represent the movement associated with the settlement. The element contains a `__name` attribute with the value `movement`.
  * `[RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders)` This element represent the order associated with the settlement. The element contains a `__name` attribute with the value `order`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` This element represent the payee associated with the settlement. The element contains a `__name` attribute with the value `payee`.
  * `[RowDrsPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayee)` This element represent the drs_payee associated with the settlement. The element contains a `__name` attribute with the value `drs_payee`.
  * `[RowDrsPendingDeduct](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPendingDeduct)` This element represent the pending deduction associated with the settlement. The element contains a `__name` attribute with the value `drs_pending_deduct`.

## Request Details

**Endpoint:** `PUT /settlements/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowSettlement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSettlement&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /settlements/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
