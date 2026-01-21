# McLeod API Documentation - McMessageService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=McMessageService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# McMessageService

This service provides several operations for managing MobileComm messages and positions.

## Operations

name | role | description  
---|---|---  
[GET /mcmessages](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=getOpenMessages&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowMcMessage objects matching the given parameters.  
[GET /mcmessages/forms](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=getForms&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Gets active forms for the specified vendor.  
[GET /mcmessages/positions](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=getLatestPositions&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list containing the latest position updates for all mobile units. Note, this service returns only the most recent position update for each unit.  
[GET /mcmessages/unitMessages](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=getUnitMessages&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves all current (uncleared) messages for the specified unit and parameters.  
[GET /mcmessages/units](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=getActiveUnits&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves all active MC Units.  
[GET /mcmessages/units/q](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=getUnitByMovementId&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the proper MCUnit for the given movement. This method looks for a unit having the same ID as the tractor. If not found, then it looks for a unit having the same ID as the first driver.  
[GET /mcmessages/units/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=getUnit&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the MCUnit requested by the ID.  
[GET /mcmessages/user](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=getMessagesByUser&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves MC Messages for the specified user ID.  
[GET /mcmessages/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=getMessage&role=-1) |  [Users, Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the RowMcMessage object for the specified ID.  
[POST /mcmessages/inbound](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=handleMessageFromUnit&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a MobileComm message from a unit and adds it to the MC queue so it will appear in the message grid.  
[PUT /mcmessages](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=createMessage&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowMcMessage and sends it to the unit specified in the object.  
[PUT /mcmessages/confirm/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=confirmMessage&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Confirms the messages selected by ID.  
[PUT /mcmessages/forward/{id}/{userId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=forwardMessage&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Forwards a message to the specified user.  
[PUT /mcmessages/zmitLoad/{unitId}/{moveId}/{fuelOpt}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=zmitLoad&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Zmits load information to a unit.  
[PUT /mcmessages/zmitRoute/{unitId}/{moveId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=McMessageService&operation=zmitRoute&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Zmits route information to the specified MC Unit
