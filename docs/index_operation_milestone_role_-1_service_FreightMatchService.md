# McLeod API Documentation - /freightmatch/{movementId}/milestone

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=milestone&role=-1&service=FreightMatchService

---

go back to [FreightMatchService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=FreightMatchService&role=-1)

# POST /freightmatch/{movementId}/milestone

Based on the settings on the PowerBroker Freight Matching Control Visibility tab, create callin, order post history and/or mobile communication position records

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
movementId | ID of the movement for which to create milestone |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
eventType | (Currently not used) Type of event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
eventDateTime | (Required) Date and time of the event |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
latitude | (Required, unless city and state are supplied) Latitude of the event |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
longitude | (Required, unless city and state are supplied) Longitude of the event |  query  |  |  [Double](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Double&role=-1)  
city | (Required, unless latitude and longitude are supplied) City of the event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
state | (Required, unless latitude and longitude are supplied) Two character abbreviation for state of the event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
zipCode | (Optional) Zip code of the event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
remark | (Required) Remark for the event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
stopId | (Currently not used) Stop ID of the event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierId | (Currently not used) Carrier involved with the event |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: text/plain_

## Request Details

**Endpoint:** `POST /freightmatch/{movementId}/milestone`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** text/plain
  - Default: application/xml (if not specified)

### Example Request

```http
POST /freightmatch/{movementId}/milestone HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: text/plain
```
