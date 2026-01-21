# McLeod API Documentation - LocationRatingService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=LocationRatingService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# LocationRatingService

This service contains endpoints for retrieval and manipulation of user ratings for locations.

## Operations

name | role | description  
---|---|---  
[GET /locationRatings/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationRatingService&operation=getLocationRating&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the Location Rating for the specified ID  
[GET /locationRatings/{locationId}/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationRatingService&operation=newLocationRating&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a Location Rating object with all configured defaults set. This DOES NOT create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[PUT /locationRatings/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LocationRatingService&operation=createLocationRating&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new Location Rating record for the given data.
