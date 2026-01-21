# McLeod API Documentation - /ediBilling/userSavedSearch

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=userSavedSearch&role=-1&service=EdiBillingService

---

go back to [EdiBillingService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&role=-1)

# GET /ediBilling/userSavedSearch

Retrieves a List of RowEdiBilling objects based on an existing saved search.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
userId | string indicating the current user |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
createUserId | string indicating the user who created the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
screenClassName | string indicating the class of the screen that is related to the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
searchName | string indicating the name of the saved search |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
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

**Endpoint:** `GET /ediBilling/userSavedSearch`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /ediBilling/userSavedSearch HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
