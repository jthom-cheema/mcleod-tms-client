# McLeod API Documentation - /contacts/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createContact&role=-1&service=ContactService

---

go back to [ContactService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ContactService&role=-1)

# PUT /contacts/create

Creates a RowContact record for the given contact data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
contact | the data to use when updating the existing contact record |  body _of type: application/xml application/json_ |  |  [RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact&role=-1)  
  
* * *

## Result

[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact&role=-1) _of type: application/xml application/json_

the created RowContact record

## Request Details

**Endpoint:** `PUT /contacts/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /contacts/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
