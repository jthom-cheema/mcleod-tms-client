# McLeod API Documentation - /dataGrafter/getSearchProfileParameters/{wsSearchProfile}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getSearchProfileParameters&role=-1&service=DataGrafterService

---

go back to [DataGrafterService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DataGrafterService&role=-1)

# GET /dataGrafter/getSearchProfileParameters/{wsSearchProfile}

Retrieves a list of all parameters needed for a given WS search profile.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
wsSearchProfile | Unique identifier of WS search profile for which to return required parameter names. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/xml application/json_

Search profile parameter names defined by the WS search profile configuration.   
  
For example, `/dataGrafter/getSearchProfileParameters/ORDERS` would return all the parameters needed to call the ORDERS WS search profile.   
  

## Request Details

**Endpoint:** `GET /dataGrafter/getSearchProfileParameters/{wsSearchProfile}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /dataGrafter/getSearchProfileParameters/{wsSearchProfile} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
