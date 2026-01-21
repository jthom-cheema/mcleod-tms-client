# McLeod API Documentation - /customers/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCustomer&role=-1&service=CustomerService

---

go back to [CustomerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&role=-1)

# GET /customers/{id}

Retrieves the customer for the given customer ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID for the RowCustomer to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeComments | if related Comment records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeContacts | if related Contact records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer&role=-1) _of type: application/xml application/json_

a RowCustomer object   
  
Additional attributes: 

  * `__pastDue` This value is a calculated field, representing the past due balance for the customer.

Child Elements: 
  * `[RowSalesperson](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSalesperson)` This element represent the salesperson associated with the customer, by the `customer.salesperson_id` field. The element contains a `__name` attribute with the value `salesperson`.
  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the contacts associated with the customer. The element contains a `__name` attribute with the value `contacts`. *Note this is only returned if the `includeContacts` Query Parameter is passed as true.
  * `[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments)` These elements represent the comments associated with the customer. The element contains a `__name` attribute with the value `comments`. *Note this is only returned if the `includeComments` Query Parameter is passed as true.

## Request Details

**Endpoint:** `GET /customers/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /customers/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
