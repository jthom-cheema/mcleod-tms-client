# McLeod API Documentation - /ediOrder/{id}/excludeFromLTX

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=excludeFromLTX&role=-1&service=EdiOrderService

---

go back to [EdiOrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&role=-1)

# PUT /ediOrder/{id}/excludeFromLTX

Marks the 'Exclude from LT Express' (a.k.a. 'Skip Display') flag for the specified RowEdiOrder, as determined by the ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the RowEdiOrder that will be excluded from Load Tender Express |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

Response object with Success or Failure status and status string to display to the user

## Request Details

**Endpoint:** `PUT /ediOrder/{id}/excludeFromLTX`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
PUT /ediOrder/{id}/excludeFromLTX HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
