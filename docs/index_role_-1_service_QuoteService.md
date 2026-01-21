# McLeod API Documentation - QuoteService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=QuoteService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# QuoteService

This service provides operations that allow callers to create, retrieve, update and delete quotes in LoadMaster.

## Operations

name | role | description  
---|---|---  
[DELETE /quotes/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&operation=delete&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Deletes a quote record.  
[GET /quotes/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&operation=neww&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a quote object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /quotes/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&operation=find&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Finds quote records with the given criteria.  
[GET /quotes/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&operation=get&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the quote record identified by the given ID value.  
[PUT /quotes/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&operation=create&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new quote record.  
[PUT /quotes/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=QuoteService&operation=update&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a quote record.
