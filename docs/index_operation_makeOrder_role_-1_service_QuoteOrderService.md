# McLeod API Documentation - /quoteOrders/makeorder/{quoteId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=makeOrder&role=-1&service=QuoteOrderService

---

go back to [QuoteOrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteOrderService&role=-1)

# POST /quoteOrders/makeorder/{quoteId}

Create an order for the given quote.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
quoteId | quote ID of the quote for which to create the order |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowAbstractOrder](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAbstractOrder&role=-1) _of type: application/xml application/json_

a response object containing an HTTP response code and string representing success or failure of the web service call

## Request Details

**Endpoint:** `POST /quoteOrders/makeorder/{quoteId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
POST /quoteOrders/makeorder/{quoteId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
