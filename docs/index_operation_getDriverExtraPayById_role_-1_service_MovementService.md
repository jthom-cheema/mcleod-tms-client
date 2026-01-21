# McLeod API Documentation - /movements/{id}/otherPay/{otherPayId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDriverExtraPayById&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# GET /movements/{id}/otherPay/{otherPayId}

Returns the requested driver extra pay record.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the movement ID |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
otherPayId | the ID of the other pay record |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowDriverExtraPay](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverExtraPay&role=-1) _of type: application/xml application/json_

the requested driver extra pay record   
  
Child Elements: 

  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represent the driver associated with the driver extra pay record, by the `driver_extra_pay.driver_id` field. The element contains a `__name` attribute with the value `driver`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` This element represent the carrier associated with the driver extra pay record, by the `driver_extra_pay.payee_id` field. The element contains a `__name` attribute with the value `carrier`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the entered by user associated with the driver extra pay record, by the `driver_extra_pay.entered_user_id` field. The element contains a `__name` attribute with the value `enteredByUser`.
  * `[RowDeductCode](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDeductCode)` This element represent the deduction/earning code associated with the driver extra pay record, by the `driver_extra_pay.deduct_code_id` field. The element contains a `__name` attribute with the value `deductCode`.

## Request Details

**Endpoint:** `GET /movements/{id}/otherPay/{otherPayId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /movements/{id}/otherPay/{otherPayId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
