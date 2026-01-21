# McLeod API Documentation - CarrierDriverService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CarrierDriverService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CarrierDriverService

## Operations

name | role | description  
---|---|---  
[DELETE /carrierDriver/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=deleteCarrierDriver&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carrierDriver/current](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=getCurrentMovement&role=-1) |  [Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carrierDriver/mobileMessage/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=getMessage&role=-1) |  [Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the RowOrderPostHist object for the specified ID.  
[GET /carrierDriver/mobileMessage/{id}/attachment](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=getAttachment&role=-1) |  [Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves an attachment stored with an order history record, if it exists.  
[GET /carrierDriver/mobileMessage/{id}/thumbnail](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=getThumbnail&role=-1) |  [Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carrierDriver/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=newCarrierDriver&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carrierDriver/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=getCarrierDriverList&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for carrier drivers matching the given request parameters.  
[GET /carrierDriver/{carrierDriverId}/{movementId}/messages](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=getMessages&role=-1) |  [Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carrierDriver/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=getCarrierDriver&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carrierDriver/{id}/activeMovePins](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=getActiveMovePins&role=-1) |  [Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves move pins for the carrier driver with the specified ID.  
[POST /carrierDriver/{carrierDriverId}/confirmNotDriving](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=confirmNotDriving&role=-1) |  [Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Notes that the given carrier driver has confirmed he's not driving while using the application.  
[PUT /carrierDriver/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=createCarrierDriver&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[PUT /carrierDriver/mobileMessage/send](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=createMessage&role=-1) |  [Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[PUT /carrierDriver/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverService&operation=updateCarrierDriver&role=-1) |  [Users, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | 
