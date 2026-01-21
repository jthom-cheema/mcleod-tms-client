# McLeod API Documentation - /dataGrafter/token

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getToken&role=-1&service=DataGrafterService

---

go back to [DataGrafterService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DataGrafterService&role=-1)

# POST /dataGrafter/token

Roles that can access this endpoint are [ Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
authenticationString |  |  body _of type: application/x-www-form-urlencoded_ |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

## Request Details

**Endpoint:** `POST /dataGrafter/token`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)
- **Content-Type:** application/x-www-form-urlencoded

### Example Request

```http
POST /dataGrafter/token HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
Content-Type: application/x-www-form-urlencoded
```
