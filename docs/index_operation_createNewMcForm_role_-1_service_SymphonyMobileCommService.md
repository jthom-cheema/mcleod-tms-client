# McLeod API Documentation - /symphonymcmessages/forms

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createNewMcForm&role=-1&service=SymphonyMobileCommService

---

go back to [SymphonyMobileCommService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&role=-1)

# POST /symphonymcmessages/forms

Creates a new RowMcForm

Roles that can access this endpoint are [ Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
rowMcForm |  |  body _of type: application/xml application/json_ |  |  [RowMcForm](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcForm&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

response object indicating the success or failure of adding the mc_form to be displayed to the user

## Request Details

**Endpoint:** `POST /symphonymcmessages/forms`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowMcForm](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcForm&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
POST /symphonymcmessages/forms HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/xml
```
