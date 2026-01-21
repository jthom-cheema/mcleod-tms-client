# McLeod API Documentation - /locations/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getLocation&role=-1&service=LocationService

---

go back to [LocationService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&role=-1)

# GET /locations/{id}

Retrieves the location for the location ID.

Roles that can access this endpoint are [ Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID for the RowLocation to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
includeComments | if related Comment records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
includeContacts | if related Contact records should be included |  query  | false |  [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1)  
  
* * *

## Result

[RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation&role=-1) _of type: application/xml application/json_

the requested RowLocation object   
  
Additional attributes: 

  * `__categoryDescr` This value represents the description of the category, found in the `location.category` field.
  * `__defCommodityDescr` This value represents the description of the commodity, found in the `location.def_commodity_id` field.
  * `__dispatchZone` This value represents the description of the location's dispatch zone

Child Elements: 
  * `[RowSalesperson](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSalesperson)` This element represent the salesperson associated with the location, by the `location.salesperson` field. The element contains a `__name` attribute with the value `salesperson`.
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represent the customer associated with the location, by the `location.customer_id` field. The element contains a `__name` attribute with the value `customer`.
  * `[RowContact](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContact)` These elements represent the contacts associated with the location. The element contains a `__name` attribute with the value `contacts`. *Note this is only returned if the `includeContacts` Query Parameter is passed as true.
  * `[RowComments](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowComments)` These elements represent the comments associated with the location. The element contains a `__name` attribute with the value `comments`. *Note this is only returned if the `includeComments` Query Parameter is passed as true.

## Request Details

**Endpoint:** `GET /locations/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /locations/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
