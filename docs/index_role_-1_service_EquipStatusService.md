# McLeod API Documentation - EquipStatusService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=EquipStatusService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# EquipStatusService

This service provides operations for creating equip status events for drivers.

## Operations

name | role | description  
---|---|---  
[GET /equipStatus/approvedDriverStatuses](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipStatusService&operation=getUpcomingApprovedDriverStatuses&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for approved driver status records that are upcoming or in progress and have the provided event code type.   
  
  
[GET /equipStatus/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipStatusService&operation=newDriverStatus&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a RowDriverStatus object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /equipStatus/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipStatusService&operation=getDriverStatus&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for driver status events matching the given request parameters.  
[GET /equipStatus/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipStatusService&operation=getDriverStatus&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the RowDriverStatus record requested by the ID parameter.  
[PUT /equipStatus/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EquipStatusService&operation=createDriverStatus&role=-1) |  [Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowDriverStatus record for the given data.
