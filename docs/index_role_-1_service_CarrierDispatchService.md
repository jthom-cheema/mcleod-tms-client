# McLeod API Documentation - CarrierDispatchService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CarrierDispatchService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CarrierDispatchService

The service contains endpoints for dispatch functions on brokerage moves.

## Operations

name | role | description  
---|---|---  
[GET /carrierDispatch/logisticsTender/getNextTenderInfo/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=getNextTenderInfo&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method checks to see if a payee is setup to receive EDI, and if so, return basic info about the tender to be sent.  
[GET /carrierDispatch/searchloadnotifications](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=searchFMCarrierNotifications&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method retrieves notifications created from additions, updates, or deletions to loads and carriers (freight matching transactions).  
[POST /carrierDispatch/addPendingLock/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=addPendingLock&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Adds a pending lock on the movement.  
[POST /carrierDispatch/assign/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=assignCarrier&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method allows assignment of a carrier to a movement.  
[POST /carrierDispatch/bookload/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=assignFMCarrier&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method allows assignment of a carrier to a movement for freight matching.  
[POST /carrierDispatch/cancel/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=cancelMovement&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method cancels an in-progress or delivered move.  
[POST /carrierDispatch/clearCarrier/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=clearCarrier&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method clears the assigned carrier from the movement.  
[POST /carrierDispatch/clearNextStop/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=clearNextStop&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method clears the next available stop for the given movement.  
[POST /carrierDispatch/clearStop/{stopId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=clearStop&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method clears the specified stop using the parameters given.  
[POST /carrierDispatch/deliver/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=deliverMovement&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method delivers out the specified movement with the current date/time as the stop arrival and departure times.  
[POST /carrierDispatch/lockMovement/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=lockMovement&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Request a lock to be placed on the specified move. If successful, a lock will be placed on the movement for the time period specified in the dispatch control file field "lock_clock_minutes".  
[POST /carrierDispatch/logisticsTender/sendCancelTender/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=sendCancelTender&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method generates an EDI cancel load tender for the movement.  
[POST /carrierDispatch/logisticsTender/sendNonCancelTender/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=sendNonCancelTender&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method generates an EDI original or change load tender for the movement.  
[POST /carrierDispatch/setPay/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=setPay&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Sets the carrier pay for a given movement.  
[POST /carrierDispatch/unlock/{movementId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDispatchService&operation=unlock&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This will attempt to unlock a locked move. An exception will be thrown if the move is not locked, the locked user is different than the one making the unlock request, or the requesting user does not have permission to unlock a movement.
