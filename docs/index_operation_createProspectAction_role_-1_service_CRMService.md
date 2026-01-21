# McLeod API Documentation - /crm/prospectActions/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createProspectAction&role=-1&service=CRMService

---

go back to [CRMService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&role=-1)

# PUT /crm/prospectActions/create

Adds a RowProspectAction.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
action |  |  body _of type: application/xml application/json_ |  |  [RowProspectAction](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowProspectAction&role=-1)  
method |  |  query  | 0 |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int&role=-1)  
  
* * *

## Result

[RowProspectAction](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowProspectAction&role=-1) _of type: application/xml application/json_

the added ProspectAction object   
  
Additional attributes: 

  * `__activityDescr` This value represents the description of the activity code, found in the `prospect_action.activity_id` field.
  * `__nextActivityDescr` This value represents the description of the next activity code, found in the `prospect_action.next_act_id` field.
  * `__objection1Descr` This value represents the description of the objection code, found in the `prospect_action.objection_id1` field.
  * `__objection2Descr` This value represents the description of the objection code, found in the `prospect_action.objection_id2` field.
  * `__oppValue` This value represents the opportunity value, found in the `rate.opportunity_amt` or `customer.potential` field.
  * `__oppConfLevel` This value represents the opportunity confidence level value, found in the `rate.confidence_level` or `customer.confidence_level` field.
  * `__oppName` This value represents the opportunity name, found in the `rate.opportunity_name` field.

Child Elements: 
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represent the customer associated with the prospect action, by the `prospect_action.customer_id` field. The element contains a `__name` attribute with the value `customer`.
  * `[RowSalesperson](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSalesperson)` This element represent the salesperson associated with the prospect action, by the `prospect_action.salesperson_id` field. The element contains a `__name` attribute with the value `salesperson`.
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represent the operations user associated with the prospect action, by the `prospect_action.operations_user` field. The element contains a `__name` attribute with the value `operationsUser`.
  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the contacts associated with the prospect action. The elements contains a `__name` attribute with the value `contacts`.
  * `[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments)` These elements represent the comments associated with the prospect action. The elements contains a `__name` attribute with the value `comments`.

## Request Details

**Endpoint:** `PUT /crm/prospectActions/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowProspectAction](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowProspectAction&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /crm/prospectActions/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
