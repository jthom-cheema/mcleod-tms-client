# McLeod API Documentation - /remoteNotification/echoGetRequest

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=echoGetRequestPayload&role=-1&service=RemoteNotificationService

---

go back to [RemoteNotificationService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=RemoteNotificationService&role=-1)

# GET /remoteNotification/echoGetRequest

This method echos the request payload back to the caller.

Roles that can access this endpoint are [ Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/xml application/json text/plain application/x-www-form-urlencoded */*_

a Response containing the payload of the request sent to the service.

## Request Details

**Endpoint:** `GET /remoteNotification/echoGetRequest`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json text/plain application/x-www-form-urlencoded */*
  - Default: application/xml (if not specified)

### Example Request

```http
GET /remoteNotification/echoGetRequest HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
