# McLeod API Documentation - /links/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getLink&role=-1&service=LinkService

---

go back to [LinkService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LinkService&role=-1)

# GET /links/{id}

Retrieves a link based on the specified ID.

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID for the link to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowMobileLink](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowMobileLink&role=-1) _of type: application/xml application/json_

the requested RowMobileLink object

## Request Details

**Endpoint:** `GET /links/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /links/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
