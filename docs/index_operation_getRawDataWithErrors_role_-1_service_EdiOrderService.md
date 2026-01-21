# McLeod API Documentation - /ediOrder/{id}/rawDataWithErrors

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getRawDataWithErrors&role=-1&service=EdiOrderService

---

go back to [EdiOrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&role=-1)

# GET /ediOrder/{id}/rawDataWithErrors

Retrieves the raw data and error information for a single load tender.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the load tender for which raw data should be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[EdiRawDataResult](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.edi.EdiRawDataResult&role=-1) _of type: application/xml application/json_

Returns an EdiRawDataResult object conveying raw data and error information   
  

## Request Details

**Endpoint:** `GET /ediOrder/{id}/rawDataWithErrors`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediOrder/{id}/rawDataWithErrors HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
