# McLeod API Documentation - /brandings

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getBrandings&role=-1&service=BrandingService

---

go back to [BrandingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BrandingService&role=-1)

# GET /brandings

Gets all brandings matching the request criteria. If no criteria given, then all brandings for the current company are returned.

Roles that can access this endpoint are [ Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the `mobile_branding` table   
  
For example, `/brandings/search?profile_name=mc*&last_date_sent=>=t-100` would find brandings having a name that starts with 'mc' and was submitted to McLeod within the last 100 days. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMobileBranding](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMobileBranding&role=-1) > _of type: application/xml application/json_

a list of RowMobileBranding objects

## Request Details

**Endpoint:** `GET /brandings`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /brandings HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
