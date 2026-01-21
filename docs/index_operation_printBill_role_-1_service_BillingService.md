# McLeod API Documentation - /billing/printBill

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=printBill&role=-1&service=BillingService

---

go back to [BillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&role=-1)

# GET /billing/printBill

Prints a freight bill based on the given criteria and returns a PDF to the caller.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
billDate | date of invoices to reprint |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
billType | type of invoices to print, (I)nvoice (default), (C)redit, (D)ebit, (A)ll but summary, (S)ummary, and (J)Dedicated |  query  | I |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
billStatus | status of invoices to print, (R)eady to bill (default), (N)ot ready to bill, (B)oth |  query  | R |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
billingUser | user for which to print freight bills |  query  | * |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
startingRecord | starting order or invoice number to print, should be omitted for all |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
endingRecord | ending order or invoice number to print, should be omitted for all |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
startingCustomer | starting customer number for which to print, should be omitted for all |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
endingCustomer | ending customer number for which to print, should be omitted for all |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
sendToImaging | when document should be sent to imaging, setting this to true will result in document being sent to imaging |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
markAsPrinted | when set to true the bill is marked as printed |  query  |  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/pdf_

a response object containing a PDF version of the resulting freight invoice(s)

## Request Details

**Endpoint:** `GET /billing/printBill`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/pdf
  - Default: application/xml (if not specified)

### Example Request

```http
GET /billing/printBill HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/pdf
```
