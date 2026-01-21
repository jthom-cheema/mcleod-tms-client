# McLeod API Documentation - /quotes/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=delete&role=-1&service=QuoteService

---

go back to [QuoteService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&role=-1)

# DELETE /quotes/{id}

Deletes a quote record.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the quote record to delete |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

a response indicating success or failure of the delete operation

## Request Details

**Endpoint:** `DELETE /quotes/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
DELETE /quotes/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
