# McLeod API Documentation - OrderService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=OrderService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# OrderService

This service provides operations for retrieving and managing order records.

## Operations

name | role | description  
---|---|---  
[GET /orders](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=getOrdersByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowOrders with a full or partial match to the given value.  
[GET /orders/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=newOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates an order object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database. If a recurring order ID is supplied, then we fill the order object (and its children) with data from the recurring order record.  
[GET /orders/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=getOrdersByAdvancedSearch&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for orders matching the given request parameters.  
[GET /orders/tracking](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=getOrdersForOrderTrackingSearch&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for orders matching the given request parameters. Additional options included to allow searching into equipment and reference numbers. This matches the parameters allowed in Internet Module load tracking (OrderSearchServlet.process()). Parameters reference the field name listed. Date parameters are used for a between clause.  
[GET /orders/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowOrders objects based on an existing saved search.  
[GET /orders/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=getOrder&role=-1) |  [Users, Drivers, Customers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the Order specified by the ID.  
[GET /orders/{id}/deliveryReceipt](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=getDeliveryReceipt&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a delivery receipt, in PDF format, for the specified orderId.  
[GET /orders/{id}/positions](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=getPositionsForOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves mobile communication positions for a given order  
[POST /orders/autorate/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=autorate&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Performs autorate operation on provided order id.  
[POST /orders/autorateDetailReport/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=autorateDetailReport&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns detail report of autorate for a given order.  
[POST /orders/getBillOfLadingReport/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=getBillOfLading&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the bill of lading report for a specified order id.  
[POST /orders/{id}/convertSubjectOrder](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=convertSubjectOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Converts a subject order to an order.  
[POST /orders/{id}/copy](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=copy&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a copy of the original order in the target company.  
[POST /orders/{id}/duplicate](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=duplicate&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates duplicate copies of the original order, based on supplied parameters.  
[PUT /orders/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=createOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a RowOrders record for the given order data.  
[PUT /orders/createSubjectOrder](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=createSubjectOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a RowOrders record for the given order data.  
[PUT /orders/orderPostHist/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=createOrderPostHist&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new order history record.  
[PUT /orders/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=updateOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowOrders record for the given order data.  
[PUT /orders/updateRow](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=OrderService&operation=updateOrderRow&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowOrders record for the given order data. This strictly updates the order row without some validation and without updating corresponding stop and movement data. Care should be given when using this service.
