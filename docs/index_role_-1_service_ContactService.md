# McLeod API Documentation - ContactService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=ContactService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# ContactService

This service contains endpoints for retrieving and changin contacts.

## Operations

name | role | description  
---|---|---  
[DELETE /contacts/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ContactService&operation=deleteContact&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /contacts/{type}/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ContactService&operation=getContacts&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of contacts for a given parent row type and row ID. For example, driver BJM01 would be requested as "/D/BJM01", where 'D' represents the parent row type of a driver and 'BJM01' the ID for the driver record.  
[PUT /contacts/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ContactService&operation=createContact&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a RowContact record for the given contact data.  
[PUT /contacts/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ContactService&operation=updateContact&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowContact record for the given contact data.
