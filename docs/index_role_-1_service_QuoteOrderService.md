# McLeod API Documentation - QuoteOrderService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=QuoteOrderService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# QuoteOrderService

This service provides operations for retrieving and managing quote-order records.

## Operations

name | role | description  
---|---|---  
[GET /quoteOrders/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteOrderService&operation=newQuoteOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a quote-order object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /quoteOrders/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteOrderService&operation=getQuoteOrdersByAdvancedSearch&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for quote-orders matching the given request parameters.  
[GET /quoteOrders/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteOrderService&operation=userSavedSearchForQuoteOrders&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of quote-order records based on an existing saved search.  
[GET /quoteOrders/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteOrderService&operation=getQuoteOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the quote-order record specified by the ID.  
[POST /quoteOrders/makeorder/{quoteId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteOrderService&operation=makeOrder&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Create an order for the given quote.  
[PUT /quoteOrders/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteOrderService&operation=createQuoteOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a quote-order record for the given quote-order data.  
[PUT /quoteOrders/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteOrderService&operation=updateQuoteOrder&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a quote-order record for the given quote-order data.
