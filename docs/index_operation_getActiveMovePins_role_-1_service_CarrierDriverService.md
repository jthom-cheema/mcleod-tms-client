# McLeod API Documentation - /carrierDriver/{id}/activeMovePins

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getActiveMovePins&role=-1&service=CarrierDriverService

---

go back to [CarrierDriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&role=-1)

# GET /carrierDriver/{id}/activeMovePins

Retrieves move pins for the carrier driver with the specified ID.

Roles that can access this endpoint are [ Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID for the carrier driver to return active move pins |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1) > _of type: application/xml application/json_

a list of move pins

## Request Details

**Endpoint:** `GET /carrierDriver/{id}/activeMovePins`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierDriver/{id}/activeMovePins HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
