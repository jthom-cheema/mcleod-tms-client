# McLeod API Documentation - /thumbs/{kind}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getThumb&role=-1&service=ThumbService

---

go back to [ThumbService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ThumbService&role=-1)

# GET /thumbs/{kind}

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
kind |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
field |  |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
query |  |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `GET /thumbs/{kind}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /thumbs/{kind} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
