# McLeod API Documentation - /availableTractors/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateAvailTractDetail&role=-1&service=AvailableTractorService

---

go back to [AvailableTractorService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&role=-1)

# PUT /availableTractors/update

Updates a RowAvailTractDetail record for the given Available Tractors data.

Roles that can access this endpoint are [ Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
availTractDetail |  |  body _of type: application/xml application/json_ |  |  [RowAvailTractDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAvailTractDetail&role=-1)  
  
* * *

## Result

[RowAvailTractDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAvailTractDetail&role=-1) _of type: application/xml application/json_

Returns the updated RowAvailTractDetail object.

## Request Details

**Endpoint:** `PUT /availableTractors/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowAvailTractDetail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowAvailTractDetail&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /availableTractors/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
