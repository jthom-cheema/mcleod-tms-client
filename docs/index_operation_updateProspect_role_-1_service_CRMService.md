# McLeod API Documentation - /crm/prospects/update

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateProspect&role=-1&service=CRMService

---

go back to [CRMService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&role=-1)

# PUT /crm/prospects/update

Updates a RowCustomer record for the given Customer/Prospect data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
prospect | the data to use when updating the existing Customer/Prospect record |  body _of type: application/xml application/json_ |  |  [RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer&role=-1)  
includeComments | if related Comment records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeContacts | if related Contact records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer&role=-1) _of type: application/xml application/json_

the updated RowCustomer record.   
  
Additional attributes: 

  * `__prospectTypeDescr` This value represents the description of the prospect type, found in the `customer.prospect_type_id` field.
  * `__salesStatusDescr` This value represents the description of the sales status, found in the `customer.sales_status_id` field.
  * `__categoryDescr` This value represents the description of the category code, found in the `customer.category` field.
  * `__bridgeName` This value represents the name of the bridge customer, found in the `customer.bridge_id` field.
  * `__marketPlanDescr` This value represents the description of the market plan, found in the `customer.mark+plan_id` field.

Child Elements: 
  * `[RowSalesperson](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSalesperson)` This element represent the salesperson associated with the prospect, by the `customer.salesperson_id` field. The element contains a `__name` attribute with the value `salesperson`.
  * `[RowSalesperson](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSalesperson)` This element represent the sales manager associated with the prospect by the `customer.sales_manager_id` field. The element contains a `__name` attribute with the value `salesManager`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the operations user associated with the prospect by the `customer.operations_user` field. The element contains a `__name` attribute with the value `operationsUser`.
  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the contacts associated with the prospect. The element contains a `__name` attribute with the value `contacts`. *Note this is only returned if the `includeContacts` Query Parameter is passed as true.
  * `[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments)` These elements represent the comments associated with the prospect. The element contains a `__name` attribute with the value `comments`. *Note this is only returned if the `includeComments` Query Parameter is passed as true.

## Request Details

**Endpoint:** `PUT /crm/prospects/update`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /crm/prospects/update HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
