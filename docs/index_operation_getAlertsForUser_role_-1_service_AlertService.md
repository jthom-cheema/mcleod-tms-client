# McLeod API Documentation - /alerts/messages

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getAlertsForUser&role=-1&service=AlertService

---

go back to [AlertService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&role=-1)

# GET /alerts/messages

Retrieves a List of rapid alerts for the given user. The User ID is not passed as a parameter, but rather is determined by the Device ID in the request header.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
isConfirmed | boolean value of is_confirmed, added as a where clause in the query |  query  |  |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
isRead | boolean value of is_read, added as a where clause in the query |  query  |  |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
alertId | string value defining the type of alerts to be queried, added as a where clause in the query |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowRapidAlertMsg](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowRapidAlertMsg&role=-1) > _of type: application/xml application/json_

a list of RowRapidAlertMsg objects   
  
Additional attributes: 

  * `__alertDescription` This value represents the description of the alert definition. The code for this is found in the `rapid_alert_msg.alert_id` field.

Child elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the user record associated with the value of `rapid_alert_msg.entered_by_userid`. This element contains a `__name` attribute with the value `enteredByUser`.

## Request Details

**Endpoint:** `GET /alerts/messages`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /alerts/messages HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
