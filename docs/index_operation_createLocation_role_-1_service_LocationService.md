# McLeod API Documentation - /locations/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createLocation&role=-1&service=LocationService

---

go back to [LocationService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&role=-1)

# PUT /locations/create

Creates a new RowLocation record for the given Location data.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
location | the data to use when creating the new location |  body _of type: application/xml application/json_ |  |  [RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation&role=-1)  
  
* * *

## Result

[RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation&role=-1) _of type: application/xml application/json_

the created RowLocation record   
  
Additional attributes: 

  * `__categoryDescr` This value represents the description of the category, found in the `location.category` field.
  * `__defCommodityDescr` This value represents the description of the commodity, found in the `location.def_commodity_id` field.
  * `__dispatchZone` This value represents the description of the location's dispatch zone

Child Elements: 
  * `[RowSalesperson](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowSalesperson)` This element represent the salesperson associated with the location, by the `location.salesperson` field. The element contains a `__name` attribute with the value `salesperson`.
  * `[RowCustomer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowCustomer)` This element represent the customer associated with the location, by the `location.customer_id` field. The element contains a `__name` attribute with the value `customer`.

## Request Details

**Endpoint:** `PUT /locations/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Request Body

- **Type:** [RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
PUT /locations/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
Content-Type: application/xml
```
