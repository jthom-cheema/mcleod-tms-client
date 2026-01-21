# McLeod API Documentation - /movements/{id}/updateOperationalStatus

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=updateOperationalStatus&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# POST /movements/{id}/updateOperationalStatus

Updates the operational status field on the movement. Movements must be of LTL type.

Roles that can access this endpoint are [ Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the movement to be updated |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
operationalStatus | the status to set the movement to 

  * `NR` \- Not routed
  * `RT` \- Routed
  * `RM` \- Removed
  * `PL` \- Planned
  * `UL` \- Unloading
  * `LD` \- Loading
  * `LO` \- Loaded
  * `ED` \- Departed
  * `DI` \- Delivering
  * `PU` \- Picking up
  * `RTRQ` \- Return to terminal requested
  * `ET` \- Inbound
  * `AR` \- Arrived
  * `PRU` \- Partially unloaded
  * `PRL` \- Partially loaded
  * `UD` \- Unloaded
  * `CM` \- Complete
  * `RC` \- Remote complete
  * `RL` \- Ready to load
  * `RU` \- Ready to unload
  * `PA` \- Pending arrival
  * `CAN` \- Void

|  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[void](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=void&role=-1) _of type: text/plain_

## Request Details

**Endpoint:** `POST /movements/{id}/updateOperationalStatus`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /movements/{id}/updateOperationalStatus HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
