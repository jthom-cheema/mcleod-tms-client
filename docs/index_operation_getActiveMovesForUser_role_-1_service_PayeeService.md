# McLeod API Documentation - /payees/activeMoves

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getActiveMovesForUser&role=-1&service=PayeeService

---

go back to [PayeeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&role=-1)

# GET /payees/activeMoves

Retrieves a List of RowMovement objects for the current user.

Roles that can access this endpoint are [ Users, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
showDelivered | whether to show moves delivered within the last 14 days |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1) > _of type: application/xml application/json_

a list of RowMovement objects

## Request Details

**Endpoint:** `GET /payees/activeMoves`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /payees/activeMoves HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
