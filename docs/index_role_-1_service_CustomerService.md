# McLeod API Documentation - CustomerService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CustomerService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CustomerService

This service provides methods for retrieving and updating customer records. Several reports scoped to individual customers are available too.

## Operations

name | role | description  
---|---|---  
[ /customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=mapContacts&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[ /customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=mapComments&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=getCustomerByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of customers with a full or partial name match to the given query.  
[GET /customers/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=newCustomer&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a customer object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /customers/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=getCustomersByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for customers matching the given request parameters.  
[GET /customers/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowCustomer objects based on an existing saved search.  
[GET /customers/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=getCustomer&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the customer for the given customer ID.  
[GET /customers/{id}/agedARReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=getAgedAR&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Runs the Aged AR report for the given customer.  
[GET /customers/{id}/revenueReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=getRevenueReport&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces a customer revenue report.  
[GET /customers/{id}/unbilledOrdersReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=getUnbilledOrdersReport&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces an unbilled orders report for the customer specified. As this is expected to be run from the customer screen, no range filter is given to select a range of customers and no option is given to allow sorting by customer.  
[PUT /customers/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=createCustomer&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new customer record for the given data.  
[PUT /customers/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CustomerService&operation=updateCustomer&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a customer record for the given data.
