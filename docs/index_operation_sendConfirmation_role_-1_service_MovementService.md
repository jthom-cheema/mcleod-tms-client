# McLeod API Documentation - /movements/{id}/sendConfirmation

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=sendConfirmation&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# PUT /movements/{id}/sendConfirmation

Sends a confirmation to the carrier, via return PDF, email, fax, or eRate (imaging).

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
conf | a RateConfirmation object, in XML, representing the contact and print/email/fax/eRate options for how the confirmation will be sent. |  body _of type: application/xml application/json_ |  |  [RateConfirmation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.dsp.RateConfirmation&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf_

a response object containing the PDF of the template, or a simple confirmation message (if report has not been chosen to be returned as a PDF)

## Request Details

**Endpoint:** `PUT /movements/{id}/sendConfirmation`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RateConfirmation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.ws.loadmaster.dsp.RateConfirmation&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /movements/{id}/sendConfirmation HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
Content-Type: application/xml
```
