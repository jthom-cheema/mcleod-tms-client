# McLeod API Documentation - /motorAccidents/new

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=newMotorAccident&role=-1&service=MotorAccidentService

---

go back to [MotorAccidentService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&role=-1)

# GET /motorAccidents/new

This method creates a default motor accident record. This is used as a template before creating a new record.

Roles that can access this endpoint are [ Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

_This method has no parameters._

* * *

## Result

[RowMotorAccident](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMotorAccident&role=-1) _of type: application/xml application/json_

a default RowMotorAccident record *   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the record status, found in the `motoraccident.status` field.

## Request Details

**Endpoint:** `GET /motorAccidents/new`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /motorAccidents/new HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
