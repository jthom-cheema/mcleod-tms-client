# McLeod API Documentation - /carrierDriver/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateCarrierDriver&role=-1&service=CarrierDriverService

---

go back to [CarrierDriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&role=-1)

# PUT /carrierDriver/update

Roles that can access this endpoint are [ Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
updatedRow |  |  body _of type: application/xml application/json_ |  |  [RowCarrierDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierDriver&role=-1)  
  
* * *

## Result

[RowCarrierDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierDriver&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `PUT /carrierDriver/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowCarrierDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCarrierDriver&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /carrierDriver/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
