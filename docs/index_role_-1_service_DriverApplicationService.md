# McLeod API Documentation - DriverApplicationService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=DriverApplicationService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# DriverApplicationService

This service provides operations that allow callers to retrieve and update drivers, enter driver applications for employment and to run various individually-scoped reports.

## Operations

name | role | description  
---|---|---  
[GET /driverApplications/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverApplicationService&operation=newApplication&role=-1) |  [Not Logged In, Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a driver application object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[POST /driverApplications/makeDriver/{applicationId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverApplicationService&operation=makeDriver&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Create a driver from the given driver application.  
[PUT /driverApplications/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverApplicationService&operation=createApplication&role=-1) |  [Not Logged In, Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowDriverApplication record for the given application data.
