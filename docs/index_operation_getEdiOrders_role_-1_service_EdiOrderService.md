# McLeod API Documentation - /ediOrder/retrieveRecords

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEdiOrders&role=-1&service=EdiOrderService

---

go back to [EdiOrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&role=-1)

# GET /ediOrder/retrieveRecords

Allows a partner to retrieve order information (format driven by DataFusion mapper) for a single batch number, a range of batch numbers, or a range of dates.

Roles that can access this endpoint are [ Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
partnerId | string indicating which partner's data should be retrieved |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
altPartnerId | string indicating which partner's data should be retrieved |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
version | string indicating the version of the data to be retrieved |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
transactionSet | string indicating the type of transaction set to be retrieved |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
batch | integer indicating a single batch number to be retrieved |  query  |  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
beginBatch | integer indicating the beginning of the batch number range (both begin and end batch numbers must be specified if a range is desired) |  query  |  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
endBatch | integer indicating the end of the batch number range (both begin and end batch numbers must be specified if a range is desired) |  query  |  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
beginDate | date/time indicating the beginning of the date range (both begin and end dates must be specified if a date range is desired) |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
endDate | date/time indicating the beginning of the date range (both begin and end dates must be specified if a date range is desired) |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
  
* * *

## Result

[Object](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Object&role=-1) _of type: application/xml application/json_

returns either a generated output from the EDI template in XML, Json, or X12 or returns a List objects   
  
Additional attributes: 

  * `__collectionMethodDescr` This value represents the description of the collection method, found in the `edi_order.collection_method` field.
  * `__rateTypeDescr` This value represents the description of the rate type, found in the `edi_order.rate_type` field.
  * `__purposeDescr` This value represents the tender purpose.

Child Elements: 
  * `[RowEdiStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStop)` These elements represent the stops associated with the load tender. Each element contains a `__name` attribute with the value `stops`.

## Request Details

**Endpoint:** `GET /ediOrder/retrieveRecords`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediOrder/retrieveRecords HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
