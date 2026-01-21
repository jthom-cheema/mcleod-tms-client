# McLeod API Documentation - /freightmatch/{stopId}/arriveDepart

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=arriveDepart&role=-1&service=FreightMatchService

---

go back to [FreightMatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=FreightMatchService&role=-1)

# POST /freightmatch/{stopId}/arriveDepart

Create callin record for an arrival or departure event

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
stopId | (Required) ID of the stop for the arrive/depart event |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
orderId | (Required) ID of the order for the arrive/depart event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
movementId | (Required) ID of the movement for the arrive/depart event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierId | (Required) ID of the carrier for the arrive/depart event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
eventType | (Required) eventType for the arrive/depart event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
eventDateTime | (Required) Date and time of the arrive/depart event |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
latitude | (Optional) Latitude of the arrive/depart event |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
longitude | (Optional) Longitude of the event |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
remark | (Optional) Remark for the arrive/depart event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

  
  
**Additional details**   
If latitude and longitude are not provided, the latitude and longitude values from the stop record will be used.   
If the stop record does not have latitude and longitude values, the latitude and longitude values from the stop's city ID value will be used.   
Valid event type codes 

  * **X3** \- Arrive at pickup location
  * **X1** \- Arrive at delivery location
  * **AF** \- Depart from pickup location
  * **CD** \- Depart from delivery location

  
If the Freight Matching control file is setup to enable auto dispatch, the submitted stop will update the respective actual_arrival or actual_departure fields with the submitted eventDateTime

## Request Details

**Endpoint:** `POST /freightmatch/{stopId}/arriveDepart`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /freightmatch/{stopId}/arriveDepart HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
