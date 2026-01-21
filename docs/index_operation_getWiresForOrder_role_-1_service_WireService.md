# McLeod API Documentation - /wires/move/{id}/

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getWiresForOrder&role=-1&service=WireService

---

go back to [WireService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&role=-1)

# GET /wires/move/{id}/

Retrieves wires for the order, based upon the specified movement in movementID. Wires displayed are always for an order, rather than specifically for the movement, although they are requested by movement.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the movement for which to return wires for the movement's order record |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [ReadOnlyRow](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.data.ReadOnlyRow&role=-1) > _of type: application/xml application/json_

a list of Wire objects   
  
Child Elements: 

  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This elements represent the entered user associated with the wire. The element contains a `__name` attribute with the value `enteredByUser`.
  * `[RowDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowDriver)` This elements represent the driver user associated with the wire. The element contains a `__name` attribute with the value `driver`.
  * `[RowPayee](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowPayee)` This elements represent the carrier user associated with the wire. The element contains a `__name` attribute with the value `payee`.

## Request Details

**Endpoint:** `GET /wires/move/{id}/`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /wires/move/{id}/ HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
