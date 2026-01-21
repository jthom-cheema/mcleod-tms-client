# McLeod API Documentation - /payees/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newPayee&role=-1&service=PayeeService

---

go back to [PayeeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&role=-1)

# GET /payees/new

Creates a payee object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee&role=-1) _of type: application/xml application/json_

a payee record with all appropriate defaults set   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the payee status, found in the `payee.status` field.
  * `__safetyRatingDescr` This value represents the description of the safety rating, found in the `drs_payee.safety_rating` field.
  * `__brokerAuthStatusDescr` This value represents the description of the broker authority status, found in the `drs_payee.broker_auth_status` field.
  * `__commonAuthStatusDescr` This value represents the description of the common authority status, found in the `drs_payee.common_auth_status` field.
  * `__contractAuthStatusDescr` This value represents the description of the contract authority status, found in the `drs_payee.contract_auth_status` field.

Child Elements: 
  * `[RowDrsPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayee)` This element represent the drs payee associated with the payee. The element contains a `__name` attribute with the value `drsPayee`.

## Request Details

**Endpoint:** `GET /payees/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /payees/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
