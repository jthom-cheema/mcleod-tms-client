# McLeod API Documentation - /deductions/history/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getDeductionHistoryById&role=-1&service=DeductionService

---

go back to [DeductionService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&role=-1)

# GET /deductions/history/{id}

Retrieves the deduction history record for the given ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the Deduction History record |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowDrsDeductHist](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsDeductHist&role=-1) _of type: application/xml application/json_

the requested `A [RowDrsSettleHist](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDrsSettleHist)` record   
  
Additional attributes: 

  * `__payMethodDescr` the description of the pay method, found in the `drs_settle_hist.pay_method` field
  * `__payeeTypeDescr` the description of the payee type
  * `__commodityIdDescr` the description of the commodity, found in the `drs_settle_hist.commodity_id` field
  * `__revenueIdDescr` the description of the revenue code, found in the `drs_settle_hist.revenue_id` field

Child Elements: 
  * `[RowTractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTractor)` This element represent the tractor associated with the deduction history record. The element contains a `__name` attribute with the value `tractor`.
  * `[RowTrailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowTrailer)` This element represent the trailer associated with the deduction history record. The element contains a `__name` attribute with the value `trailer`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represent the driver associated with the deduction history record. The element contains a `__name` attribute with the value `driver`.

## Request Details

**Endpoint:** `GET /deductions/history/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /deductions/history/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
