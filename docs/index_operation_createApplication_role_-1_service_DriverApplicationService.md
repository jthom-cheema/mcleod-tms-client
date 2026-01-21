# McLeod API Documentation - /driverApplications/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createApplication&role=-1&service=DriverApplicationService

---

go back to [DriverApplicationService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverApplicationService&role=-1)

# PUT /driverApplications/create

Creates a new RowDriverApplication record for the given application data.

Roles that can access this endpoint are [ Not Logged In, Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
application | the data to use when creating the new driver application |  body _of type: application/xml application/json_ |  |  [RowDriverApplication](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverApplication&role=-1)  
  
* * *

## Result

[RowDriverApplication](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverApplication&role=-1) _of type: application/xml application/json_

the created RowDriverApplication record   
  

  * `__successMessage` This value is from the `mobile_service.dr_response` field.
  * `__contactName` This value is from the `mobile_service.dr_contact_name` field.
  * `__contactPhone` This value is from the `mobile_service.dr_contact_phone` field.
  * `__contactEmail` This value is from the `mobile_service.dr_contact_email` field.

Child Elements: 
  * `[RowDriverEmpHistory](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverEmpHistory)` These elements contain the previous employment records associated with the application. Each element contains a `__name` attribute with the value `employments`.
  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements contain the contact records associated with the application. Each element contains a `__name` attribute with the value `contacts`.
  * `[RowDrViolation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrViolation)` These elements contain the list of violations the candidate entered on the application. Each element contains a `__name` attribute with the value `violations`.
  * `[RowDrAccidents](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrAccidents)` These elements contain the list of accidents the candidate entered on the application. Each element contains a `__name` attribute with the value `accidents`.

## Request Details

**Endpoint:** `PUT /driverApplications/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowDriverApplication](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriverApplication&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /driverApplications/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
