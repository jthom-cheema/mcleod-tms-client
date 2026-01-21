# McLeod API Documentation - TrailerService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=TrailerService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# TrailerService

This service provides operations for retrieving and managing trailers. Access to several individually-scoped reports is available too.

## Operations

name | role | description  
---|---|---  
[GET /trailers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=getTrailersByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of Trailers with a full or partial match to the given value.  
[GET /trailers/near](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=getTrailersNear&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns {@link List} of Trailer-specific data in the form of ReadOnlyRow records, where the trailer is within 100 miles of the provided latitude and longitude.  
[GET /trailers/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=newTrailer&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a trailer object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /trailers/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=getTrailersByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for trailers matching the given request parameters.  
[GET /trailers/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowTrailer objects based on an existing saved search.  
[GET /trailers/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=getTrailer&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the Trailer record with the given ID.  
[GET /trailers/{id}/preassignments](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=getPreassignments&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves preassignments for the trailer with the specified ID.  
[GET /trailers/{id}/previousOrders](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=getOrdersForTrailer&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowOrders objects the trailer was previously assigned to.  
[GET /trailers/{id}/revenueReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=getRevenueReport&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces a trailer revenue report.  
[PUT /trailers/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=createTrailer&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowTrailer record for the given data.  
[PUT /trailers/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TrailerService&operation=updateTrailer&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowTrailer record for the given data.
