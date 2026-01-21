# McLeod API Documentation - /ediBilling/search

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getEdiBillsByAdvancedSearch&role=-1&service=EdiBillingService

---

go back to [EdiBillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&role=-1)

# GET /ediBilling/search

Searches the database for EDI Bills matching the given request parameters.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
request | read for query parameters to be used as search criteria; use any combination of fields from tables: 

  * `edi_billing` \- use `edi_billing` or no prefix
  * `customer` \- use `customer` prefix
  * `edibilling_profile` \- use `profile` prefix

For example, `/ediBilling/search?edi_billing.partner_id=TESTPARTNER&customer.state_id=AL` would find EDI Bills for partner ID 'TESTPARTNER' where the customer is located in Alabama.   
  
**Sorting:** To sort the result set, you can provide the following reserved query parameter: `orderBy` If the orderBy parameter is not provided a default sort of `edi_billing.order_id+ASC,edi_billing.invoice_no_string+ASC` will be applied. For example, `/ediBilling/search?edi_billing.partner_id=*&orderBy=customer.name+DESC` would return all edi billing records sorted descending by the customer name. Multiple sort columns can be provided in a comma delimited format. `orderBy=prefix.field+direction,prefix.field+direction` **Pagination:** To page the result set, you can provide the following reserved query parameters: `recordLength and recordOffset` For example, `/ediBilling/search?edi_billing.partner_id=*&recordLength=100&recordOffset=50` would return 100 records starting at the 51st record in the return record set. If no recordLength parameter is provided the search result maximum value in the mobile service control file will be applied. **Changed After Date:** To return only records that have been changed or added since a specific date and time, you can provide the `changedAfterDate` parameter. Dates are limited to the audit setting and days to keep value in the table properties configuration. For example, `/ediBilling/search?edi_billing.ready_to_process=Y&changedAfterDate=t-1` would return edi billing records that are marked ready to bill that have been added or updated since the beginning of the previous day. **Change Types:** To further define the types of changes you want to filter, use the `changedAfterType` parameter. This parameter is to be used in conjunction with `changedAfterDate` to give the ability to specify if you want added or updated records. Allowed values: [Add, Update]. Any other value will result in an exception. If the `ChangedAfterType` parameter is not provided, both added and updated records will be returned. If you do not provide a corresponding `ChangedAfterDate` the `ChangedAfterType` parameter will be ignored. For example, `/ediBilling/search?edi_billing.ready_to_process=Y&changedAfterDate=t-1&changedAfterType=Add` would return edi billing records that are marked ready to bill that have been added since the beginning of the previous day. |  context  |  |  [HttpServletRequest](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.servlet.http.HttpServletRequest&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowEdiBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBilling&role=-1) > _of type: application/xml application/json_

a list of RowEdiBilling objects   
  
Additional attributes: 

  * `__directionDescr` This value represents the bill's direction, found in the `edi_billing.direction` field.
  * `__errorDescr` This value represents the error description, found in the `edi_billing.error` field.
  * `__readyToSendDescr` This value represents the ready to send description, found in the `edi_billing.ready_to_send` field.
  * `__equipmentTypeDescr` This value represents the description of the equipment type, found in the `edi_billing.equipment_type_id` field.
  * `__shipmentMatchingDescr` This value represents the shipment matching method description, found in the `edi_billing.ship_match_type` field.

Child Elements: 
  * `[RowEdiBillingProfile](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBillingProfile)` This element represents the EDI Billing Profile associated with the invoice. The element contains a `__name` attribute with the value `profile`.

## Request Details

**Endpoint:** `GET /ediBilling/search`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediBilling/search HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
