# McLeod API Documentation - TractorService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=TractorService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# TractorService

This service provides operations for retrieving and managing tractors. Access to several individually-scoped reports is available too.

## Operations

name | role | description  
---|---|---  
[GET /tractors](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&operation=getTractorsByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of Tractors with a full or partial match to the given value.  
[GET /tractors/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&operation=newTractor&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a tractor object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /tractors/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&operation=getTractorsByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for tractors matching the given request parameters.  
[GET /tractors/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowTractor objects based on an existing saved search.  
[GET /tractors/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&operation=getTractor&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the Tractor record with the given ID.  
[GET /tractors/{id}/preassignments](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&operation=getPreassignments&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves preassignments for the tractor with the specified ID.  
[GET /tractors/{id}/revenueReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&operation=getTractorRevenueReport&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces a tractor revenue report.  
[PUT /tractors/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&operation=createTractor&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowTractor record for the given Tractor data.  
[PUT /tractors/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TractorService&operation=updateTractor&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowTractor record for the given data.
