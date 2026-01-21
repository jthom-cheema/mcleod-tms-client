# McLeod API Documentation - /mcmessages/confirm/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=confirmMessage&role=-1&service=McMessageService

---

go back to [McMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&role=-1)

# PUT /mcmessages/confirm/{id}

Confirms the messages selected by ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the message to be confirmed |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1) _of type: text/plain_

a String message to be displayed to the user with success/failure of confirmation

## Request Details

**Endpoint:** `PUT /mcmessages/confirm/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
PUT /mcmessages/confirm/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
