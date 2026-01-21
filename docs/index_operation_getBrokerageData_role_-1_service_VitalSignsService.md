# McLeod API Documentation - /vitalSigns/brokerage/data

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getBrokerageData&role=-1&service=VitalSignsService

---

go back to [VitalSignsService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=VitalSignsService&role=-1)

# GET /vitalSigns/brokerage/data

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id |  |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1) _of type: application/xml_

## Request Details

**Endpoint:** `GET /vitalSigns/brokerage/data`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml
  - Default: application/xml (if not specified)

### Example Request

```http
GET /vitalSigns/brokerage/data HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
