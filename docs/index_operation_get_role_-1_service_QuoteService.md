# McLeod API Documentation - /quotes/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=get&role=-1&service=QuoteService

---

go back to [QuoteService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&role=-1)

# GET /quotes/{id}

Retrieves the quote record identified by the given ID value.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the quote record in the database |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowQuote](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuote&role=-1) _of type: application/xml application/json_

the quote record

## Request Details

**Endpoint:** `GET /quotes/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /quotes/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
