# McLeod API Documentation - Roles

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)

# Roles

## Overview

Roles are used to secure operation endpoints. For the user to access endpoint, the users web user type my be on endpoint. You will find the roles for each operation on the Operation and endpoint pages. Endpoints may have multiple roles.

Everyone | All logged in and not logged in users.  
---|---  
No Role | Targets only users with no defined role.  
Drivers | Drivers with a web user account. Able to access the Driver mobile app and/or Web Portal.  
Customers | This role is not yet active/released. Developed for the Customer App, which is not live. Designed to give customers visibility on where their freight is. Requires Customer App license.  
Carriers | This role is not yet active/released. Developed for the Customer App, which is not live. Designed to give customers visibility on where their freight is. Requires Customer App license.  
Carrier Drivers | Able to access the Carrier App for their assigned load via a load-specific PIN. Requires Carrier App license.  
Fusion Partners | A Fusion Partner user is a trading partner that can access the API to retrieve/submit select transactions.  
Freight Matching | User of type freight matching may access the endpoint. You must have a Freight Matching license to use this endpoint, unless other roles are assigned to endpoint.  
Not Logged In | Any user who is not logged in.   
Logged In | Any user who is logged in, regardless of role. 
