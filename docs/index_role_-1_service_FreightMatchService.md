# McLeod API Documentation - FreightMatchService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=FreightMatchService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# FreightMatchService

This service provides operations for digital freight matching vendors

## Operations

name | role | description  
---|---|---  
[POST /freightmatch/{movementId}/assignCarrierDriver](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=FreightMatchService&operation=assignCarrierDriver&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Update the driver name, mobile phone number and email address on a load  
[POST /freightmatch/{movementId}/assignCarrierEquipment](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=FreightMatchService&operation=assignCarrierEquipment&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Update the carrier tractor and carrier trailer on a load  
[POST /freightmatch/{movementId}/milestone](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=FreightMatchService&operation=milestone&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Based on the settings on the PowerBroker Freight Matching Control Visibility tab, create callin, order post history and/or mobile communication position records  
[POST /freightmatch/{stopId}/arriveDepart](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=FreightMatchService&operation=arriveDepart&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Create callin record for an arrival or departure event
