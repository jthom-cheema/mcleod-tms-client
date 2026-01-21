# McLeod API Documentation - /crm/prospects

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getProspectByQuery&role=-1&service=CRMService

---

go back to [CRMService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&role=-1)

# GET /crm/prospects

Retrieves a List of prospects/customers with a full or partial match to the given value.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
q | string for which to search for customers/prospects by ID or name |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer&role=-1) > _of type: application/xml application/json_

a list of RowCustomer objects

## Request Details

**Endpoint:** `GET /crm/prospects`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /crm/prospects HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
