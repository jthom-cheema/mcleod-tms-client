# McLeod API Documentation - /metadata

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getMetadata&role=-1&service=MetadataService

---

go back to [MetadataService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MetadataService&role=-1)

# GET /metadata

Information about the current environment such as LME version, current user information, enabled companies, API major/minor version, licensing information ...

Roles that can access this endpoint are [ Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[Metadata](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.general.Metadata&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `GET /metadata`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /metadata HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
