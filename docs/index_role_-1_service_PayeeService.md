# McLeod API Documentation - PayeeService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=PayeeService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# PayeeService

This service provides methods for retrieving and updating payee records.

## Operations

name | role | description  
---|---|---  
[GET /payees](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&operation=getPayeeByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowPayees with a full or partial match to the given value.  
[GET /payees/activeMoves](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&operation=getActiveMovesForUser&role=-1) |  [Users, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowMovement objects for the current user.  
[GET /payees/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&operation=newPayee&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a payee object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /payees/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&operation=getPayeesByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for locations matching the given request parameters.  
[GET /payees/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowPayee objects based on an existing saved search.  
[GET /payees/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&operation=getPayee&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the Payee for the payee ID  
[GET /payees/{id}/revenueReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&operation=getBrokerageRevenueReport&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Generates a brokerage revenue report for the specified carrier, date range, etc.  
[PUT /payees/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&operation=createPayee&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowPayee record for the given Payee data.  
[PUT /payees/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PayeeService&operation=updatePayee&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowPayee record for the given Payee data.
