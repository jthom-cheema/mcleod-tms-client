# McLeod API Documentation - /ediDriverExtraPay/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDriverExtraPayById&role=-1&service=EdiDriverExtraPayService

---

go back to [EdiDriverExtraPayService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiDriverExtraPayService&role=-1)

# GET /ediDriverExtraPay/{id}

Returns the requested driver extra pay record.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the other pay record to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowEdiDriverExtraPay](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiDriverExtraPay&role=-1) _of type: application/xml application/json_

the requested driver other pay record   
  
Child Elements: 

  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represent the driver associated with the driver extra pay record, by the `driver_extra_pay.driver_id` field. The element contains a `__name` attribute with the value `driver`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` This element represent the carrier associated with the driver extra pay record, by the `driver_extra_pay.payee_id` field. The element contains a `__name` attribute with the value `carrier`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the entered by user associated with the driver extra pay record, by the `driver_extra_pay.entered_user_id` field. The element contains a `__name` attribute with the value `enteredByUser`.
  * `[RowDeductCode](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDeductCode)` This element represent the deduction/earning code associated with the driver extra pay record, by the `driver_extra_pay.deduct_code_id` field. The element contains a `__name` attribute with the value `deductCode`.

## Request Details

**Endpoint:** `GET /ediDriverExtraPay/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediDriverExtraPay/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
