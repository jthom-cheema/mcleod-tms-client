# McLeod API Documentation - /alerts/messages/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getRapidAlertMsg&role=-1&service=AlertService

---

go back to [AlertService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&role=-1)

# GET /alerts/messages/{id}

Retrieves an RowRapidAlertMsg object for the given rapid alert message ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID for the rapid alert message |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowRapidAlertMsg](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowRapidAlertMsg&role=-1) _of type: application/xml application/json_

a RowRapidAlertMsg object   
  
Additional attributes: 

  * `__alertDescription` This value represents the description of the alert definition. The code for this is found in the `rapid_alert_msg.alert_id` field.

Child elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the user record associated with the value of `rapid_alert_msg.entered_by_userid`. This element contains a `__name` attribute with the value `enteredByUser`.

## Request Details

**Endpoint:** `GET /alerts/messages/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /alerts/messages/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
