# McLeod API Documentation - /customers/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newCustomer&role=-1&service=CustomerService

---

go back to [CustomerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&role=-1)

# GET /customers/new

Creates a customer object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer&role=-1) _of type: application/xml application/json_

a customer record with all appropriate defaults set

## Request Details

**Endpoint:** `GET /customers/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /customers/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
