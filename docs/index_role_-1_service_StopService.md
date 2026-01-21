# McLeod API Documentation - StopService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=StopService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# StopService

This service provides methods for getting stops, stop notes and reference numbers for orders.

## Operations

name | role | description  
---|---|---  
[DELETE /stops/{stopId}/referenceNumbers/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=StopService&operation=deleteReferenceNumber&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Deletes a reference number from a stop  
[DELETE /stops/{stopId}/stopNotes/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=StopService&operation=deleteStopNote&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Deletes a stop note from a stop  
[GET /stops/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=StopService&operation=getStop&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a stop and the associated reference numbers and stop notes.  
[GET /stops/{id}/referenceNumbers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=StopService&operation=getReferenceNumbers&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves reference numbers for the specified stop ID  
[GET /stops/{id}/referenceNumbers/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=StopService&operation=newReferenceNumber&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a reference number object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /stops/{id}/stopNotes](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=StopService&operation=getStopNotes&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves stop notes for the specified stop ID
