# McLeod API Documentation - /pnnLane/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updatePnnLane&role=-1&service=PNNLaneService

---

go back to [PNNLaneService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PNNLaneService&role=-1)

# PUT /pnnLane/update

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
updatedRow |  |  body _of type: application/xml_ |  |  [RowPnnLane](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPnnLane&role=-1)  
  
* * *

## Result

[RowPnnLane](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPnnLane&role=-1) _of type: application/xml_

## Request Details

**Endpoint:** `PUT /pnnLane/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowPnnLane](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPnnLane&role=-1)
- **Content-Type:** application/xml

### Example Request

```http
PUT /pnnLane/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
