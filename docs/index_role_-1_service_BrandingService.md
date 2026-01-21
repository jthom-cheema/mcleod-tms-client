# McLeod API Documentation - BrandingService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=BrandingService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# BrandingService

This service contains endpoints for retrieval and manipulation of brandings and branding attachments.

## Operations

name | role | description  
---|---|---  
[GET /brandings](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BrandingService&operation=getBrandings&role=-1) |  [Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Gets all brandings matching the request criteria. If no criteria given, then all brandings for the current company are returned.  
[GET /brandings/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BrandingService&operation=getBranding&role=-1) |  [Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Gets the branding having the given ID.  
[GET /brandings/{id}/{fieldName}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BrandingService&operation=getBlob&role=-1) |  [Not Logged In, Logged In, Everyone, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves an image stored with the branding, if it exists.
