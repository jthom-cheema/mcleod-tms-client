# McLeod API Documentation - /dataGrafter/wsProfileSearch/{wsSearchProfileId}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=profileSearch&role=-1&service=DataGrafterService

---

go back to [DataGrafterService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DataGrafterService&role=-1)

# GET /dataGrafter/wsProfileSearch/{wsSearchProfileId}

Allows WS search profiles to be used to define custom search content.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
wsSearchProfileId | Unique identifier of WS search profile to use to generate search results. |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
request |  |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/xml application/json_

Search results as defined by the WS search profile definition.   
  
For example, `/dataGrafter/profileSearch/ORDER?shipDate=20170503144900-0500&status=A` would return the search results configured on a WS search profile named ORDER using the configured shipDate and status filter parameters.   
  
Query parameters configured in the WS search profile configuration are limited to single word alphanumeric names with no special characters or logical operators. Logical operators must be setup in the WS Search Profile in the LoadMaster Application.   
  
Normal McLeod API Date formats are supported and data pagination can be achieved by including a # value injector in the WS search profile in the LoadMaster application.   
  
For example. In the WS Search Profile SQL configuration you can include the following: `ORDER BY orders.id DESC offset #recordOffset rows FETCH first #recordLength rows only FOR json path` and provide the recordOffset and recordLength parameters when calling the profileSearch end point to return data one page at a time.   

## Request Details

**Endpoint:** `GET /dataGrafter/wsProfileSearch/{wsSearchProfileId}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /dataGrafter/wsProfileSearch/{wsSearchProfileId} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
