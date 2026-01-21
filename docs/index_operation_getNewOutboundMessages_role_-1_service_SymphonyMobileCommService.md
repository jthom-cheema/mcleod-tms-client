# McLeod API Documentation - /symphonymcmessages

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getNewOutboundMessages&role=-1&service=SymphonyMobileCommService

---

go back to [SymphonyMobileCommService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&role=-1)

# GET /symphonymcmessages

Retrieves a List of new Outbound RowMcMessage objects for vendorId with status of 0

Roles that can access this endpoint are [ Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
blocksize | \- maximum returned records default is 100 |  query  |  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMcMessage](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcMessage&role=-1) > _of type: application/xml application/json_

a list of RowMcMessage objects

## Request Details

**Endpoint:** `GET /symphonymcmessages`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /symphonymcmessages HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
