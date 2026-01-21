# McLeod API Documentation - MetadataService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=MetadataService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# MetadataService

This service provides a method for callers to use when they need to know what all is licensed and permissioned for the current user.

## Operations

name | role | description  
---|---|---  
[GET /metadata](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MetadataService&operation=getMetadata&role=-1) |  [Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Information about the current environment such as LME version, current user information, enabled companies, API major/minor version, licensing information ...  
[POST /metadata/heartbeat](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MetadataService&operation=getHeartbeat&role=-1) |  [Drivers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | 
