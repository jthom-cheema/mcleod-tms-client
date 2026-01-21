# McLeod API Documentation - /deductions/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createDeduction&role=-1&service=DeductionService

---

go back to [DeductionService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&role=-1)

# PUT /deductions/create

Creates a new drs_pending_deduct record for the given data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
deduction |  |  body _of type: application/xml application/json_ |  |  [RowDrsPendingDeduct](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPendingDeduct&role=-1)  
  
* * *

## Result

[RowDrsPendingDeduct](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPendingDeduct&role=-1) _of type: application/xml application/json_

returns the created deduction record   
  
Child Elements:   
  

  * `[RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement)` This element represent the movement associated with the pending deduction. The element contains a `__name` attribute with the value `movement`.
  * `[RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders)` This element represent the order associated with the pending deduction. The element contains a `__name` attribute with the value `order`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` This element represent the payee associated with the pending deduction. The element contains a `__name` attribute with the value `payee`.
  * `[RowDrsPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayee)` This element represent the drs_payee associated with the pending deduction. The element contains a `__name` attribute with the value `drs_payee`.

## Request Details

**Endpoint:** `PUT /deductions/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowDrsPendingDeduct](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPendingDeduct&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /deductions/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
