# McLeod API Documentation - MobileTableConfigService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=MobileTableConfigService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# MobileTableConfigService

This service provides operations for retrieving and managing configurations used by the mobile apps.

## Operations

name | role | description  
---|---|---  
[DELETE /mobileTableConfigs/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MobileTableConfigService&operation=deleteMobileTableConfig&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Deletes the given RowMobileTableConfig and associated RowMobileTableConfigField records specified by the supplied ID.  
[GET /mobileTableConfigs](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MobileTableConfigService&operation=getMobileTableConfigs&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowMobileTableConfig records matching the given parameter for the logged in user.  
[GET /mobileTableConfigs/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MobileTableConfigService&operation=newMobileTableConfig&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a RowMobileTableConfig object. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /mobileTableConfigs/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MobileTableConfigService&operation=getMobileTableConfig&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the table configuration based on the specified ID for the logged in user.  
[PUT /mobileTableConfigs/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MobileTableConfigService&operation=createMobileTableConfig&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowMobileTableConfig record for the given data.  
[PUT /mobileTableConfigs/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=MobileTableConfigService&operation=updateMobileTableConfig&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowMobileTableConfig record for the given data.
