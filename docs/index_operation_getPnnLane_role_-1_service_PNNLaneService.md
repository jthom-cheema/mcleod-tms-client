# McLeod API Documentation - /pnnLane/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getPnnLane&role=-1&service=PNNLaneService

---

go back to [PNNLaneService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PNNLaneService&role=-1)

# GET /pnnLane/{id}

Retrieves carrier lanes information.

Roles that can access this endpoint are [ Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | for the RowPnnLane to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowPnnLane](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPnnLane&role=-1) _of type: application/xml_

RowPnnLane object

## Request Details

**Endpoint:** `GET /pnnLane/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml
  - Default: application/xml (if not specified)

### Example Request

```http
GET /pnnLane/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
