# McLeod API Documentation - /comments/{id}/thumbnail

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getThumbnail&role=-1&service=CommentService

---

go back to [CommentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&role=-1)

# GET /comments/{id}/thumbnail

Retrieves a PNG thumbnail of the attachment stored with a comment, if it exists. Image attachments yield smaller versions, PDF attachments yield a small version of the first page, other known file types such as Microsoft Word and Excel yield simple generic images of the file types and everything else yields a generic image with a question mark.

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the comment ID, included in the path |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
size | the size of the largest dimension; for example, if you have a 200x100 pixel image and you passed in 50 for this parameter, the thumbnail would be 50x25 |  query  |  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: image/png_

a response object with a PNG thumbnail body

## Request Details

**Endpoint:** `GET /comments/{id}/thumbnail`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** image/png
  - Default: application/xml (if not specified)

### Example Request

```http
GET /comments/{id}/thumbnail HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: image/png
```
