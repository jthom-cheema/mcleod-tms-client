# McLeod API Documentation - /containers/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getContainer&role=-1&service=ContainerService

---

go back to [ContainerService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ContainerService&role=-1)

# GET /containers/{id}

Retrieves the RowContainer specified by the ID.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | ID of the container to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowContainer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowContainer&role=-1) _of type: application/xml application/json_

the requested RowContainer object   
  
Additional attributes: 

  * `__statusDescr` This value represents the description of the container status, found in the `container.status` field.

Child Elements: 
  * `[RowUsers](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowUsers)` This element represents the entered user associated with the container, by the `container.entered_by` field. The element contains a `__name` attribute with the value `enteredByUser`.
  * `[RowLocation](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowLocation)` This element represents the steam ship location of the container, by the `container.ss_location_id` field. The element contains a `__name` attribute with the value `ssLocation`.
  * `[RowEquipmentType](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEquipmentType)` This element represents the equipment type of the container, by the `container.container_type_id` field. The element contains a `__name` attribute with the value `containerType`.

## Request Details

**Endpoint:** `GET /containers/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /containers/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
