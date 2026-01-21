# McLeod API Documentation - LocationService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=LocationService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# LocationService

This service provides operations for retrieving and updating locations. Several individually-scoped reports are also available.

## Operations

name | role | description  
---|---|---  
[GET /locations](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&operation=getLocationByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowLocations with a full or partial match to the given value.  
[GET /locations/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&operation=newLocation&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a location object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /locations/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&operation=getLocationsByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for locations matching the given request parameters.  
[GET /locations/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowLocation objects based on an existing saved search.  
[GET /locations/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&operation=getLocation&role=-1) |  [Users, Customers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the location for the location ID.  
[GET /locations/{id}/trailerPool](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&operation=getTrailerPool&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces a trailer pool report for the location.  
[PUT /locations/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&operation=createLocation&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowLocation record for the given Location data.  
[PUT /locations/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationService&operation=updateLocation&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowLocation record for the given Location data.
