# McLeod API Documentation - WireService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=WireService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# WireService

This service provides methods for retrieving and creating wires (aka advances).

## Operations

name | role | description  
---|---|---  
[GET /wires/move/{id}/](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&operation=getWiresForOrder&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves wires for the order, based upon the specified movement in movementID. Wires displayed are always for an order, rather than specifically for the movement, although they are requested by movement.  
[GET /wires/move/{id}/wirePayees](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&operation=getWirePayee&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the Payee record for a given movement as specified in the given movement ID.  
[GET /wires/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&operation=getWiresByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for unposted wires matching the given request parameters.  
[GET /wires/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowUnpostedWire objects based on an existing saved search.  
[GET /wires/wireServiceCodes](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&operation=getWireCodes&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of active wire codes.  
[GET /wires/{vendor}/checkCount](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&operation=getCheckCount&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Obtains the count of available checks for the vendor.  
[POST /wires/validateWire](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&operation=validateWire&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Validates a new unposted wire record without creating the record in the database.  
[PUT /wires](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=WireService&operation=createWire&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new unposted wire record.
