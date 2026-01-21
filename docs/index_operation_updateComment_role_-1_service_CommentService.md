# McLeod API Documentation - /comments/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateComment&role=-1&service=CommentService

---

go back to [CommentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&role=-1)

# PUT /comments/update

Updates a comments record for the given comment data.

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
comment | the data to use when updating the existing comment record |  body _of type: application/xml application/json_ |  |  [RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments&role=-1)  
  
* * *

## Result

[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments&role=-1) _of type: application/xml application/json_

the updated RowComments record   
  
Additional attributes: 

  * `__commentTypeDescr` This value represents the description of the comment type, found in the `comments.comment_type_id` field.

Child Elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the entered by user associated with the `comments.entered_user_id` field. This element contains a `__name` attribute with the value `enteredByUser`.

## Request Details

**Endpoint:** `PUT /comments/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /comments/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
