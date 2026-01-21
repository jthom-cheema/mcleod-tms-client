# McLeod API Documentation - /comments/commentTypes

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCommentTypes&role=-1&service=CommentService

---

go back to [CommentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&role=-1)

# GET /comments/commentTypes

Produces a list of active comment types as defined in LoadMaster.

The endpoint has no roles. 

## Parameters

_This method has no parameters._

* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowCommentType](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCommentType&role=-1) > _of type: application/xml application/json_

a list of CommentType objects

## Request Details

**Endpoint:** `GET /comments/commentTypes`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /comments/commentTypes HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
