# McLeod API Documentation - SymphonyMobileCommService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=SymphonyMobileCommService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# SymphonyMobileCommService

This service provides several operations for managing Vendor MobileComm positions, messages, workflow, driver hours, and engine data.

## Operations

name | role | description  
---|---|---  
[GET /symphonymcmessages](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getNewOutboundMessages&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of new Outbound RowMcMessage objects for vendorId with status of 0  
[GET /symphonymcmessages/driver](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getDriver&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get Driver by id  
[GET /symphonymcmessages/driverHours](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getDriversHours&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get Driver hours for date  
[GET /symphonymcmessages/drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getDrivers&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get all Drivers  
[GET /symphonymcmessages/events](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getEvents&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get all Events  
[GET /symphonymcmessages/forms](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getForms&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get all Forms  
[GET /symphonymcmessages/forms/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getFormImage&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get Form image  
[GET /symphonymcmessages/location](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getLocation&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get Location by id  
[GET /symphonymcmessages/locations](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getlocations&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get all Locations  
[GET /symphonymcmessages/tractor](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getTractor&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get Tractor by id  
[GET /symphonymcmessages/tractors](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getTractors&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get all Tractors  
[GET /symphonymcmessages/trailer](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getTrailer&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get Trailer by id  
[GET /symphonymcmessages/trailers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getTrailers&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Get all Trailers  
[GET /symphonymcmessages/workflow](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getWorkflow&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a Workflow for vendorId and driverId  
[GET /symphonymcmessages/workflowById](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getWorkflowById&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a Workflow for vendorId and workflowId  
[GET /symphonymcmessages/workflowspreassigned](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=getWorkflowsPreassigned&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves Workflows Preassigned for vendorId and driverId  
[POST /symphonymcmessages](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=createNewInboundMessage&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowMcMessage and sends it back to the dispatch system from the unit specified in the object.  
[POST /symphonymcmessages/errorcodes](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=createNewMcErrorCode&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowMcErrorCode  
[POST /symphonymcmessages/forms](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=createNewMcForm&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowMcForm  
[POST /symphonymcmessages/performance](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=createNewMcPerformx&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new Performance data  
[POST /symphonymcmessages/position](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=createNewMcPosition&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowMcPosition  
[POST /symphonymcmessages/trailerStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=createNewTrailerStatus&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new Trailer status and alarm messages  
[PUT /symphonymcmessages/driverAvailable](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=updateDriverAvailableHours&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Update driver available hours  
[PUT /symphonymcmessages/driverHours](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=createNewDriverHours&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new Driver hours  
[PUT /symphonymcmessages/driverHoursLogs](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=createNewDriverHoursLogs&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new Driver hours logs  
[PUT /symphonymcmessages/driverStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=updateDriverStatus&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Update driver status  
[PUT /symphonymcmessages/status](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SymphonyMobileCommService&operation=updateMessageStatus&role=-1) |  [Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Update message status
