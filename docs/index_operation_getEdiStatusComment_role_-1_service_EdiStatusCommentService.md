# McLeod API Documentation - /ediStatusComments/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEdiStatusComment&role=-1&service=EdiStatusCommentService

---

go back to [EdiStatusCommentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusCommentService&role=-1)

# GET /ediStatusComments/{id}

Retrieves a RowEdiStatusComment based on the ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the EDI status comment record to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowEdiStatusComment](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStatusComment&role=-1) _of type: application/xml application/json_

a RowEdiStatusComment object   
  
Additional attributes: 

  * `__typeDescr` This value represents the description of the comment types, found in the `edi_status_comment.comment_type` field.

## Request Details

**Endpoint:** `GET /ediStatusComments/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediStatusComments/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
