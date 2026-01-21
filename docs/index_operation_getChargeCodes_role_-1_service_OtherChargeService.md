# McLeod API Documentation - /otherCharges/codes

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getChargeCodes&role=-1&service=OtherChargeService

---

go back to [OtherChargeService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OtherChargeService&role=-1)

# GET /otherCharges/codes

Searches the database for charge codes matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from the `charge_code` table   
  
For example, `/otherCharges/codes/search?is_taxable=Y&descr=Fuel*` would find taxable charge codes having a description that starts with 'Fuel'. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowChargeCode](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowChargeCode&role=-1) > _of type: application/xml application/json_

a list of RowChargeCode objects

## Request Details

**Endpoint:** `GET /otherCharges/codes`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /otherCharges/codes HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
