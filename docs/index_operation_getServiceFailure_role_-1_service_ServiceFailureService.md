# McLeod API Documentation - /serviceFailures/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getServiceFailure&role=-1&service=ServiceFailureService

---

go back to [ServiceFailureService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&role=-1)

# GET /serviceFailures/{id}

Retrieves the service failure based on the specified ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the record to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowServiceFail](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowServiceFail&role=-1) _of type: application/xml application/json_

the requested RowServiceFail object   
  
Additional attributes: 

  * `__ediStandardCodeDescr` This value represents the description of the delay code, found in the `servicefail.edi_standard_code` field.

Child Elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the dispatcher user associated with the service failure, by the `servicefail.dispatcher_user_id` field. The element contains a `__name` attribute with the value `dispatcherUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the operations user associated with the service failure, by the `servicefail.operations_user` field. The element contains a `__name` attribute with the value `operationsUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the driver manager user associated with the service failure, by the `servicefail.fleet_manager` field. The element contains a `__name` attribute with the value `fleetManagerUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the caused by user associated with the service failure, by the `servicefail.user_id` field. The element contains a `__name` attribute with the value `causedByUser`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the reviewed by user associated with the service failure, by the `servicefail.reviewed_by` field. The element contains a `__name` attribute with the value `reviewedByUser`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This element represents the driver user associated with the service failure, by the `servicefail.driver_id` field. The element contains a `__name` attribute with the value `driver`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` This element represents the carrier user associated with the service failure, by the `servicefail.override_payee_id` field. The element contains a `__name` attribute with the value `carrier`.
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represents the customer associated with the service failure, by the `servicefail.customer_id` field. The element contains a `__name` attribute with the value `customer`.
  * `[RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation)` This element represents the location of the terminal associated with the service failure, by the `servicefail.terminal_id` field. The element contains a `__name` attribute with the value `terminalLocation`.

## Request Details

**Endpoint:** `GET /serviceFailures/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /serviceFailures/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
