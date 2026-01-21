# McLeod API Documentation - /payees/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getPayee&role=-1&service=PayeeService

---

go back to [PayeeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&role=-1)

# GET /payees/{id}

Retrieves the Payee for the payee ID

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID for the RowPayee to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeComments | if related Comment records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeContacts | if related Contact records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee&role=-1) _of type: application/xml application/json_

the requested RowPayee object   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the payee status, found in the `payee.status` field.
  * `__safetyRatingDescr` This value represents the description of the safety rating, found in the `drs_payee.safety_rating` field.
  * `__brokerAuthStatusDescr` This value represents the description of the broker authority status, found in the `drs_payee.broker_auth_status` field.
  * `__commonAuthStatusDescr` This value represents the description of the common authority status, found in the `drs_payee.common_auth_status` field.
  * `__contractAuthStatusDescr` This value represents the description of the contract authority status, found in the `drs_payee.contract_auth_status` field.

Child Elements: 
  * `[RowDrsPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsPayee)` This element represent the drs payee associated with the payee. The element contains a `__name` attribute with the value `drsPayee`.
  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the contacts associated with the payee. The element contains a `__name` attribute with the value `contacts`. *Note this is only returned if the `includeContacts` Query Parameter is passed as true.
  * `[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments)` These elements represent the comments associated with the payee. The element contains a `__name` attribute with the value `comments`. *Note this is only returned if the `includeComments` Query Parameter is passed as true.

## Request Details

**Endpoint:** `GET /payees/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /payees/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
