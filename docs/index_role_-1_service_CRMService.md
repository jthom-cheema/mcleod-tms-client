# McLeod API Documentation - CRMService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CRMService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CRMService

This service provides methods for retrieving and updating prospects and prospect actions. In addition it provides a mechanism for managing a saleperson's call list.

## Operations

name | role | description  
---|---|---  
[GET /crm/callListProfiles](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=getCallListProfiles&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /crm/callListProfiles/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=getCallListProfile&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /crm/prospectActions/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=newProspectAction&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a prospect action object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /crm/prospectActions/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=getProspectAction&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the specified ProspectAction  
[GET /crm/prospects](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=getProspectByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of prospects/customers with a full or partial match to the given value.  
[GET /crm/prospects/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=newProspect&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a customer object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /crm/prospects/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=getProspectsByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for customers matching the given request parameters.  
[GET /crm/prospects/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowCustomer objects based on an existing saved search.  
[GET /crm/prospects/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=getProspect&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the customer for the given customer/prospect ID.  
[GET /crm/prospects/{id}/history](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=getHistoricalActivities&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves upcoming ProspectAction records for the given customer.  
[GET /crm/prospects/{id}/upcoming](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=getUpcomingActivities&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves upcoming ProspectAction records for the given customer.  
[PUT /crm/prospectActions/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=createProspectAction&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Adds a RowProspectAction.  
[PUT /crm/prospectActions/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=updateProspectAction&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowProspectAction record if it already exists, otherwise creates a new one.  
[PUT /crm/prospects/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=createProspect&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowCustomer record for the given Customer data.  
[PUT /crm/prospects/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CRMService&operation=updateProspect&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowCustomer record for the given Customer/Prospect data.
