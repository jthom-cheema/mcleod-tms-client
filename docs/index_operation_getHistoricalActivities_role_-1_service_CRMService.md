# McLeod API Documentation - /crm/prospects/{id}/history

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getHistoricalActivities&role=-1&service=CRMService

---

go back to [CRMService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&role=-1)

# GET /crm/prospects/{id}/history

Retrieves upcoming ProspectAction records for the given customer.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the Customer for which to retrieve upcoming ProspectAction records |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowProspectAction](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowProspectAction&role=-1) > _of type: application/xml application/json_

a list of ProspectAction objects

## Request Details

**Endpoint:** `GET /crm/prospects/{id}/history`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /crm/prospects/{id}/history HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
