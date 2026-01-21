# McLeod API Documentation - /settlements

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getSettlements&role=-1&service=SettlementService

---

go back to [SettlementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&role=-1)

# GET /settlements

Retrieves a list of unpaid settlement records for the given parameters.

Roles that can access this endpoint are [ Users, Drivers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
orderId | order ID |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
invoiceNumber | external invoice number |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
startDate | starting delivery date |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
endDate | ending delivery date |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
payeeId | the ID from the payee table (ignored when user is not an LME user) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [ReadOnlyRow](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.data.ReadOnlyRow&role=-1) > _of type: application/xml application/json_

a list of `[ReadOnlyRow](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.data.ReadOnlyRow)` objects, representing unpaid settlements and pending deductions   
  
Additional attributes: 

  * `__other_pay` the calculated total of other pay
  * `__total_pay` the calculate total pay of the settlement (freight pay plus other pay)
  * `__record_type` the type of record (`S` for settlement, `D` for deduction)

## Request Details

**Endpoint:** `GET /settlements`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /settlements HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
