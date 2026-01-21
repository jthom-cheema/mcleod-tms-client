# McLeod API Documentation - MotorAccidentService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=MotorAccidentService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# MotorAccidentService

This service provides operations that allow callers to retrieve and manage motor accident records.

## Operations

name | role | description  
---|---|---  
[GET /motorAccidents](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&operation=getMotorAccidents&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of motor accident records matching the given request parameters or with an match of the given value to the driver ID or report number.  
[GET /motorAccidents/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&operation=newMotorAccident&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method creates a default motor accident record. This is used as a template before creating a new record.  
[GET /motorAccidents/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&operation=getMotorAccidentsByAdvancedSearch&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns a list of motor accident records matching the given request parameters.  
[GET /motorAccidents/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&operation=userSavedSearch&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowMotorAccident objects based on an existing saved search.  
[GET /motorAccidents/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&operation=getMotorAccident&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the RowMotorAccident record requested by the ID parameter.  
[PUT /motorAccidents/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&operation=createMotorAccident&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new motor accident record. If successful, returns the new record.  
[PUT /motorAccidents/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MotorAccidentService&operation=updateMotorAccident&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method updates an existing motor accident record with the provided values.
