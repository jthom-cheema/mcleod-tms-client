# McLeod API Documentation - /pnnLane/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=deletePnnLane&role=-1&service=PNNLaneService

---

go back to [PNNLaneService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PNNLaneService&role=-1)

# DELETE /pnnLane/{id}

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id |  |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

## Request Details

**Endpoint:** `DELETE /pnnLane/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
DELETE /pnnLane/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
