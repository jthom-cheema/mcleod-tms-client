# McLeod API Documentation - CarrierService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CarrierService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CarrierService

This service provides methods for creating, retrieving and updating carrier records as well as checking the qualifications of a carrier against a specific load

## Operations

name | role | description  
---|---|---  
[GET /carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&operation=getPayeeByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carriers/checkQualification](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&operation=checkQualification&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Check to see if a carrier is qualified, based on carrier qualifications, to haul a specific load.  
[GET /carriers/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&operation=newPayee&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carriers/retrieve](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&operation=retrieveCarriers&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for carrier matching the given request parameters. Query parameters to be used as search criteria; All parameters are optional.  
[GET /carriers/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&operation=getPayeesByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for carriers matching the given request parameters.  
[GET /carriers/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carriers/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&operation=getPayee&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the Payee for the payee ID  
[PUT /carriers/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&operation=createPayee&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[PUT /carriers/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierService&operation=updatePayee&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | 
