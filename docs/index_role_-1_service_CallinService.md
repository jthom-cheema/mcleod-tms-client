# McLeod API Documentation - CallinService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CallinService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CallinService

This service provides operations that allow users to retrieve callins and to create driver and carrier callins.

## Operations

name | role | description  
---|---|---  
[GET /callins/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&operation=newCallin&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a callin object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the /create method to actually insert the record in the database.  
[GET /callins/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&operation=getCallinsByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for callin records matching the given request parameters.  
[GET /callins/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&operation=getRowCallin&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the callin record for the specified ID.  
[GET /callins/{type}/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&operation=getCallins&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of RowCallin records for the specified type and ID.  
[PUT /callins/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&operation=createNewCallin&role=-1) |  [Users, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a RowCallin record for the given data.  
[PUT /callins/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CallinService&operation=updateCallin&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a callin record.
