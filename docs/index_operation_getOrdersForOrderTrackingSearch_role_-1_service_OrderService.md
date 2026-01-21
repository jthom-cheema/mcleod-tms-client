# McLeod API Documentation - /orders/tracking

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getOrdersForOrderTrackingSearch&role=-1&service=OrderService

---

go back to [OrderService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&role=-1)

# GET /orders/tracking

Searches the database for orders matching the given request parameters. Additional options included to allow searching into equipment and reference numbers. This matches the parameters allowed in Internet Module load tracking (OrderSearchServlet.process()). Parameters reference the field name listed. Date parameters are used for a between clause.

Roles that can access this endpoint are [ Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
orderId | orders.id |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
proNbr | freight_group.pro_nbr |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
status | orders.status |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
blnum | orders.blnum |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
consigneeRefno | orders.consignee_refno |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
referenceNumber | reference_number.reference_number (subselected on all stops for the order) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
tractorId | tractor.id (joined on final move) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
trailerId | trailer.id (joined on final move) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
driverId | driver.id (joined on final move) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
shipperLocationId | stop.location_id (joined on orders.shipper_stop_id) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
shipperCity | stop.city_name (joined on orders.shipper_stop_id) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
shipperState | stop.state (joined on orders.shipper_stop_id) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
shipperZip | stop.zip_code (joined on orders.shipper_stop_id) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
shipperStartDate | stop.sched_arrive_early (joined on orders.shipper_stop_id) |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
shipperEndDate | stop.sched_arrive_early (joined on orders.shipper_stop_id) |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
consigneeLocationId | stop.location_id (joined on orders.consignee_stop_id) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
consigneeCity | stop.city_name (joined on orders.consignee_stop_id) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
consigneeState | stop.state (joined on orders.consignee_stop_id) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
consigneeZip | stop.zip (joined on orders.consignee_stop_id) |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
consigneeStartDate | stop.sched_arrive_early (joined on orders.consignee_stop_id) |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
consigneeEndDate | stop.sched_arrive_early (joined on orders.consignee_stop_id) |  query  |  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date&role=-1)  
  
* * *

## Result

[List](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.util.List&role=-1) < [RowOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOrders&role=-1) > _of type: application/xml application/json_

a list of RowOrders objects

## Request Details

**Endpoint:** `GET /orders/tracking`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /orders/tracking HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
