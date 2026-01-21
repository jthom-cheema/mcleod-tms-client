# McLeod API Documentation - /dispatch/dispatchControl

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDispatchControl&role=-1&service=DispatchService

---

go back to [DispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DispatchService&role=-1)

# GET /dispatch/dispatchControl

Returns the user's current company's dispatch control record.

The endpoint has no roles. 

## Parameters

_This method has no parameters._

* * *

## Result

[RowDispatchControl](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDispatchControl&role=-1) _of type: application/xml application/json_

a RowDispatchControl record

## Request Details

**Endpoint:** `GET /dispatch/dispatchControl`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /dispatch/dispatchControl HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
