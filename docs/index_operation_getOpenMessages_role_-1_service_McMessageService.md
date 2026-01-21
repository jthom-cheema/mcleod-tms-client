# McLeod API Documentation - /mcmessages

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getOpenMessages&role=-1&service=McMessageService

---

go back to [McMessageService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&role=-1)

# GET /mcmessages

Retrieves a List of RowMcMessage objects matching the given parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
messageType | indicates whether to display (I)nbound, (O)utbound or (B)oth inbound and outbound messages (the default) |  query  | B |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
currentOnly | whether to include confirmed messages |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
users | comma-delimited list of users for whom to return messages |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
drivers | comma-delimited list of drivers for whom to return messages |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
units | comma-delimited list of units for which to return messages |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
forms | comma-delimited list of forms for which to return messages |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
daysToShow | number of days back to show messages |  query  | 1 |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMcMessage](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMcMessage&role=-1) > _of type: application/xml application/json_

a list of RowMcMessage objects   
  
Child Elements: 

  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the user associated with the message, by the `mc_message.mc_user_id` field. The element contains a `__name` attribute with the value `mcUser`.

## Request Details

**Endpoint:** `GET /mcmessages`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /mcmessages HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
