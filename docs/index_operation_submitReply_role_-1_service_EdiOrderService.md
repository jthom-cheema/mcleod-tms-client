# McLeod API Documentation - /ediOrder/{id}/reply/submit

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=submitReply&role=-1&service=EdiOrderService

---

go back to [EdiOrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&role=-1)

# PUT /ediOrder/{id}/reply/submit

Replies to a specific RowEdiOrder, as determined by the ID, with the specified action, reason code, and remark.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the RowEdiOrder for which the reply is being submitted |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
action | the reply action specified by the user |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
reason | the reason code specified by the user |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
remark | the remark supplied by the user |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

response object with Success or Failure status and status string to display to the user

## Request Details

**Endpoint:** `PUT /ediOrder/{id}/reply/submit`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
PUT /ediOrder/{id}/reply/submit HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
