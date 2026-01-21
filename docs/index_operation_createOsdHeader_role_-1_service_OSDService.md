# McLeod API Documentation - /osd/header/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createOsdHeader&role=-1&service=OSDService

---

go back to [OSDService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OSDService&role=-1)

# PUT /osd/header/create

Roles that can access this endpoint are [ Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
newRow |  |  body _of type: application/xml_ |  |  [RowOsdHdr](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOsdHdr&role=-1)  
  
* * *

## Result

[RowOsdHdr](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOsdHdr&role=-1) _of type: application/xml_

## Request Details

**Endpoint:** `PUT /osd/header/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowOsdHdr](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOsdHdr&role=-1)
- **Content-Type:** application/xml

### Example Request

```http
PUT /osd/header/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
