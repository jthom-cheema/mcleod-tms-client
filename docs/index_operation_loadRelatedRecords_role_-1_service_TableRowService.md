# McLeod API Documentation - /{table}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=loadRelatedRecords&role=-1&service=TableRowService

---

go back to [TableRowService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&role=-1)

#  /{table}

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
row |  |  body _of type:_ |  |  [T](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=T&role=-1)  
  
* * *

## Result

[T](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=T&role=-1)

## Request Details

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Request Body

- **Type:** [T](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=T&role=-1)

### Example Request

```http
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
