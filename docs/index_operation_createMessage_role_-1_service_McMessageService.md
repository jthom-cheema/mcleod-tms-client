# McLeod API Documentation - /mcmessages

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createMessage&role=-1&service=McMessageService

---

go back to [McMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&role=-1)

# PUT /mcmessages

Creates a new RowMcMessage and sends it to the unit specified in the object.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
message | the RowMcMessage to be sent |  body _of type: application/xml application/json_ |  |  [RowMcMessage](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcMessage&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

response object indicating the success or failure of sending the message and a text message to be displayed to the user

## Request Details

**Endpoint:** `PUT /mcmessages`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowMcMessage](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcMessage&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /mcmessages HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
