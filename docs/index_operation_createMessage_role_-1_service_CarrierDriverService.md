# McLeod API Documentation - /carrierDriver/mobileMessage/send

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createMessage&role=-1&service=CarrierDriverService

---

go back to [CarrierDriverService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&role=-1)

# PUT /carrierDriver/mobileMessage/send

Roles that can access this endpoint are [ Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
orderPostHist |  |  body _of type: application/xml application/json_ |  |  [RowOrderPostHist](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrderPostHist&role=-1)  
  
* * *

## Result

[RowOrderPostHist](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrderPostHist&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `PUT /carrierDriver/mobileMessage/send`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowOrderPostHist](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrderPostHist&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /carrierDriver/mobileMessage/send HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
