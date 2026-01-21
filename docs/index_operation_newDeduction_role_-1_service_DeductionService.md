# McLeod API Documentation - /deductions/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newDeduction&role=-1&service=DeductionService

---

go back to [DeductionService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&role=-1)

# GET /deductions/new

Creates a pending deduction object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
dispatchId | Order number or manifest number of the deduction. Populates information in the new deduction object from the provided dispatchId |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
deductCodeId | Deduction code used to create the deduction. Populates information in the new deduction object from the deduction code. |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowDrsPendingDeduct](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPendingDeduct&role=-1) _of type: application/xml application/json_

a pending deduction record with all appropriate defaults set.

## Request Details

**Endpoint:** `GET /deductions/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /deductions/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
