# McLeod API Documentation - /comments/{parentRowType}/{parentRowId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getComments&role=-1&service=CommentService

---

go back to [CommentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&role=-1)

# GET /comments/{parentRowType}/{parentRowId}

Retrieves a list of comments for a given parent row type and row ID. For example, driver BJM01 would be requested as "/D/BJM01", where 'D' represents the parent row type of a driver and 'BJM01' the ID for the driver record.

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
parentRowType | the comment record's parent row type |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
parentRowId | the comment record's parent row ID |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments&role=-1) > _of type: application/xml application/json_

list of RowComments records   
  
Additional attributes: 

  * `__commentTypeDescr` This value represents the description of the comment type, found in the `comments.comment_type_id` field.

Child Elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the entered by user associated with the `comments.entered_user_id` field. This element contains a `__name` attribute with the value `enteredByUser`.

## Request Details

**Endpoint:** `GET /comments/{parentRowType}/{parentRowId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /comments/{parentRowType}/{parentRowId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
