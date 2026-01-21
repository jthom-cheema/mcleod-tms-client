# McLeod API Documentation - /alerts/messageCount

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getTotalUnreadCountForUser&role=-1&service=AlertService

---

go back to [AlertService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&role=-1)

# GET /alerts/messageCount

Returns the number of unread messages across all companies the user is registered in.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1) _of type: text/plain_

the unread message count

## Request Details

**Endpoint:** `GET /alerts/messageCount`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
GET /alerts/messageCount HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
