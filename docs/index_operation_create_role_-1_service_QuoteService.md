# McLeod API Documentation - /quotes/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=create&role=-1&service=QuoteService

---

go back to [QuoteService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&role=-1)

# PUT /quotes/create

Creates a new quote record.

Roles that can access this endpoint are [ Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
quote | the data to use when creating the new quote |  body _of type: application/xml application/json_ |  |  [RowQuote](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuote&role=-1)  
  
* * *

## Result

[RowQuote](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuote&role=-1) _of type: application/xml application/json_

the posted quote record

## Request Details

**Endpoint:** `PUT /quotes/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowQuote](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuote&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /quotes/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
