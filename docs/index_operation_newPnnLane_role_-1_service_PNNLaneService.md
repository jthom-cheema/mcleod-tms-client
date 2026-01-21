# McLeod API Documentation - /pnnLane/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newPnnLane&role=-1&service=PNNLaneService

---

go back to [PNNLaneService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PNNLaneService&role=-1)

# GET /pnnLane/new

The endpoint has no roles. 

## Parameters

_This method has no parameters._

* * *

## Result

[RowPnnLane](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPnnLane&role=-1) _of type: application/xml_

## Request Details

**Endpoint:** `GET /pnnLane/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml
  - Default: application/xml (if not specified)

### Example Request

```http
GET /pnnLane/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
