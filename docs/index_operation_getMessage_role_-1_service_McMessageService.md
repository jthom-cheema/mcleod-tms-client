# McLeod API Documentation - /mcmessages/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getMessage&role=-1&service=McMessageService

---

go back to [McMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&role=-1)

# GET /mcmessages/{id}

Retrieves the RowMcMessage object for the specified ID.

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID for the RowMcMessage to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMcMessage](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcMessage&role=-1) _of type: application/xml application/json_

the requested RowMcMessage object   
  
Child Elements: 

  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the user associated with the message, by the `mc_message.mc_user_id` field. The element contains a `__name` attribute with the value `mcUser`.

## Request Details

**Endpoint:** `GET /mcmessages/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /mcmessages/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
