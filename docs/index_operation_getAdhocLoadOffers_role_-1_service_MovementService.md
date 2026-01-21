# McLeod API Documentation - /movements/adhocOffers

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getAdhocLoadOffers&role=-1&service=MovementService

---

go back to [MovementService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MovementService&role=-1)

# GET /movements/adhocOffers

Retrieves a List of RowMovement objects matching the criteria given that represent the available movements for a driver.

Roles that can access this endpoint are [ Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
driverId | ID of the driver for which to return offers |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
originRadius | miles when filtering by radius for the origin |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
originLatitude | latitude of the origin used to search |  query  |  |  [Float](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Float&role=-1)  
originLongitude | longitude of the origin used to search |  query  |  |  [Float](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Float&role=-1)  
destinationRadius | miles when filtering by radius for the destination |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
destinationLatitude | latitude of the destination used to search |  query  |  |  [Float](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Float&role=-1)  
destinationLongitude | longitude of the destination used to search |  query  |  |  [Float](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Float&role=-1)  
daysOut | days for how far out to search |  query  |  |  [Integer](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Integer&role=-1)  
equipment | comma-delimited list of equipment types |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowMovement](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowMovement&role=-1) > _of type: application/xml application/json_

a list of RowMovement objects   
  
Additional attributes: 

  * `__findNearDistance` This value represents the find near distance.
  * `__proratedRevenue` This value represents the prorated revenue of the load.
  * `__callInPhoneNumber` This value represents the phone number used to call in to request the load.

## Request Details

**Endpoint:** `GET /movements/adhocOffers`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /movements/adhocOffers HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
