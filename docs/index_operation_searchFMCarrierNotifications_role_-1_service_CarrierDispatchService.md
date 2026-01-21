# McLeod API Documentation - /carrierDispatch/searchloadnotifications

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=searchFMCarrierNotifications&role=-1&service=CarrierDispatchService

---

go back to [CarrierDispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&role=-1)

# GET /carrierDispatch/searchloadnotifications

This method retrieves notifications created from additions, updates, or deletions to loads and carriers (freight matching transactions).

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
startDate | Start of date range for which to retrieve notifications   
|  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
endDate | End of date range for which to retrieve notifications   
|  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
includeFailedOnly | True to only retrieve failed notifications **Defaults to true**   
|  query  | true |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
recordLength | (Optional) Number of records to return.   
**This value will be set to the smaller value between the vendor supplied recordLength parameter and the fmvendor_control.record_return_limit value set in the PowerBroker Freight Matching control  
  
If there is no value set in the fmvendor_control.record_return_limit field then this value will default to the mobile_service.max_search value set in the PowerBroker Mobile Service control**   
|  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
recordOffset | (Optional) Start of offset in the returned data result set.   
**Defaults to 0** |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/xml application/json_

a response containing previously sent notifications

## Request Details

**Endpoint:** `GET /carrierDispatch/searchloadnotifications`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /carrierDispatch/searchloadnotifications HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
