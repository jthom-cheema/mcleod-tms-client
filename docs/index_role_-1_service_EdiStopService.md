# McLeod API Documentation - EdiStopService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=EdiStopService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# EdiStopService

This service provides methods for retrieving stops, stop notes and references numbers for EDI load tenders or inbound EDI Bills.

## Operations

name | role | description  
---|---|---  
[GET /ediStops/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStopService&operation=getStop&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a stop and the associated reference numbers and stop notes.  
[GET /ediStops/{id}/referenceNumbers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStopService&operation=getReferenceNumbers&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves reference numbers for the specified stop ID  
[GET /ediStops/{id}/stopNotes](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStopService&operation=getStopNotes&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves stop notes for the specified stop ID
