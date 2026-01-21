# McLeod API Documentation - SysAdminService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=SysAdminService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# SysAdminService

This service provides operations for managing application locks and other administrative functions.

## Operations

name | role | description  
---|---|---  
[GET /sysadmin/getServerTimeMillis](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SysAdminService&operation=getServerTimestamp&role=-1) |  [Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method returns the server time in milliseconds.  
[GET /sysadmin/locks](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SysAdminService&operation=getLocks&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | This method gets a list of current application locks.  
[POST /sysadmin/locks/unlock](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SysAdminService&operation=unlock&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[POST /sysadmin/locks/unlock/all](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SysAdminService&operation=unlockAll&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | 
