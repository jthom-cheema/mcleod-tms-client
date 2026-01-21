# McLeod API Documentation - /customers

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=mapContacts&role=-1&service=CustomerService

---

go back to [CustomerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&role=-1)

#  /customers

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
customerIDList |  |  body _of type:_ |  |  [List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1)  
  
* * *

## Result

[void](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=void&role=-1)

## Request Details

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Request Body

- **Type:** [List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1)

### Example Request

```http
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
```
