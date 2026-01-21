# McLeod API Documentation - AvailableTractorService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=AvailableTractorService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# AvailableTractorService

The service class containing the endpoints for managing brokerage available tractors.

## Operations

name | role | description  
---|---|---  
[DELETE /availableTractors/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&operation=deleteAvailableTractor&role=-1) |  [Users, Carriers, Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Deletes the given record specified by the supplied ID.  
[GET /availableTractors](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&operation=getAvailableTractors&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of available tractors for the given carrier.  
[GET /availableTractors/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&operation=newAvailableTractor&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates an availableTractors user object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /availableTractors/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&operation=getAvailableTractorsSearch&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for available tractors matching the given request parameters.  
[GET /availableTractors/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&operation=getAvailableTractorById&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the RowAvailTractDetail record for the given ID.  
[PUT /availableTractors/add](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&operation=addAvailableTractor&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates an availableTractors object with the specified parameter values.  
[PUT /availableTractors/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&operation=createRowAvailTractDetail&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowAvailTractDetail record for the given RowAvailTractDetail data.  
[PUT /availableTractors/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AvailableTractorService&operation=updateAvailTractDetail&role=-1) |  [Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowAvailTractDetail record for the given Available Tractors data.
