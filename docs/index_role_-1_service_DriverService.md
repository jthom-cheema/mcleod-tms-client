# McLeod API Documentation - DriverService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=DriverService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# DriverService

This service provides operations that allow callers to retrieve and update drivers, enter driver applications for employment and to run various individually-scoped reports.

## Operations

name | role | description  
---|---|---  
[ /drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getCurrentMovement&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getDriversByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of Drivers with a full or partial match to given value.  
[GET /drivers/historyReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getHistoryReport&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces a driver history report.  
[GET /drivers/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=newDriver&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a driver object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /drivers/rollingStops](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getRollingStopList&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a rolling List of RowStop objects for a driver.   
  
Under typical circumstances, this list will included:  
1: Cleared first stop of the current movement if in transit or  
Cleared last stop of the current movement if delivered.  
2: Next uncleared stop.  
3 - given stopCount: Upcoming first and last stops of the current and preassigned movements.  
  
  
[GET /drivers/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getDriversByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for drivers matching the given request parameters.  
[GET /drivers/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowDriver objects based on an existing saved search.  
[GET /drivers/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getDriver&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the Driver record with the given ID.  
[GET /drivers/{id}/assignments](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getAssignments&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /drivers/{id}/current](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getCurrentMovement&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the current movement record for the given driver ID.  
[GET /drivers/{id}/lastStop](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getLastStop&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the last stop of the driver's last preassignment (or if none, the driver's current assignment).  
[GET /drivers/{id}/picture](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getDriverPicture&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the driver's profile picture, if it exists.  
[GET /drivers/{id}/preassignments](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getPreassignments&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves preassignments for the driver with the specified ID.  
[GET /drivers/{id}/revenueReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getRevenueReport&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces a driver revenue report.  
[GET /drivers/{id}/scorecardReport](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=getDriverScorecardReport&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces the driver scorecard report.  
[POST /drivers/{id}/confirmNotDriving](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=confirmNotDriving&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Notes that the given driver has confirmed he's not driving while using the application.  
[PUT /drivers/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DriverService&operation=createDriver&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowDriver record for the given Driver data.
