# McLeod API Documentation - /dispatch/{stopId}/acceptOffer

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=handleDriverOfferAcceptance&role=-1&service=DispatchService

---

go back to [DispatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DispatchService&role=-1)

# POST /dispatch/{stopId}/acceptOffer

Handles the changes needed to be made when a driver accepts an offered stop. If the {@link DriverStopReport#getAppliesToGroup()} variable is `true`, then this stop plus others in the same group will be accepted together. See {@link RowStop#buildGroupingKey()} for what constitutes a group of stops. Currently, this only works for LTL movements.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
stopId | the ID of the stop to accepted (not currently used) |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
report | the {@link DriverStopReport} with all fields on the root object populated |  body _of type: application/xml application/json_ |  |  [DriverStopReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.dsp.DriverStopReport&role=-1)  
  
* * *

## Result

[void](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=void&role=-1)

## Request Details

**Endpoint:** `POST /dispatch/{stopId}/acceptOffer`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

### Request Body

- **Type:** [DriverStopReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.dsp.DriverStopReport&role=-1)
- **Content-Type:** application/xml application/json

### Example Request

```http
POST /dispatch/{stopId}/acceptOffer HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Content-Type: application/xml
```
