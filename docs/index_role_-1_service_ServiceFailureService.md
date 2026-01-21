# McLeod API Documentation - ServiceFailureService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=ServiceFailureService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# ServiceFailureService

This service provides a method for getting the service failure report.

## Operations

name | role | description  
---|---|---  
[DELETE /serviceFailures/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&operation=deleteServiceFail&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Deletes the given RowServiceFail specified by the supplied ID.  
[GET /serviceFailures](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&operation=getServiceFailures&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Gets all service failures matching the request criteria. If no criteria given, then all service failures for the current company are returned. For example, `/serviceFailures?driver_id=MBROOKS&minutes_late=>60&status=O` would find open service failures in which driver MBROOKS was over 60 minutes late.  
[GET /serviceFailures/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&operation=newServiceFailure&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a RowServiceFail object. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /serviceFailures/serviceFailuresReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&operation=getServiceFailuresReport&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces a service failure report.  
[GET /serviceFailures/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&operation=getServiceFailure&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the service failure based on the specified ID.  
[POST /serviceFailures/{id}/approve](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&operation=approve&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Approves a service failure specified by the supplied ID.  
[PUT /serviceFailures/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&operation=createServiceFail&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowServiceFail record for the given data.  
[PUT /serviceFailures/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ServiceFailureService&operation=updateServiceFail&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowServiceFail record for the given data.
