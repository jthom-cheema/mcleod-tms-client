# McLeod API Documentation - UserService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=UserService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# UserService

This service provides operations for retrieving and managing users. This service also contains methods for logging users in and out.

## Operations

name | role | description  
---|---|---  
[GET /users](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=getUsersByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowUsers with an ID, name, or email address matching that of given parameter.  
[GET /users/current](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=getCurrentUser&role=-1) |  [Logged In, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the currently logged in user.  
[GET /users/forgotPassword](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=requestDriverPasswordReset&role=-1) |  [Not Logged In](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /users/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=newUser&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a user object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /users/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=getUsersByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for users matching the given request parameters.  
[GET /users/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowUsers objects based on an existing saved search.  
[GET /users/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=getUser&role=-1) |  [Users, Drivers, Customers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a user based on the specified ID.  
[POST /users/changePassword](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=changePassword&role=-1) |  [Logged In, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Changes the current user's password.  
[POST /users/clearPushToken](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=clearPushToken&role=-1) |  [Logged In, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Removes the push token in the database so that push notifications may not be sent.  
[POST /users/login](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=login&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Logs the user in and returns a token that may be used on subsequent requests for access.  
[POST /users/loginFromVendor](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=loginFromVendor&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[POST /users/loginWithPIN](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=loginWithPIN&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[POST /users/logout](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=logout&role=-1) |  [Logged In, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Logs the user out.  
[POST /users/resetPassword](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=resetPassword&role=-1) |  [Not Logged In](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Resets the password for the user with the specified password reset token.  
[POST /users/updatePushToken](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=updatePushToken&role=-1) |  [Logged In, Users, Drivers, Customers, Carriers, Carrier Drivers, Fusion Partners, Freight Matching, Symphony MC](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates the push token in the database so that push notifications may be sent at a later time.  
[PUT /users/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=createRowUsers&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new RowUsers record for the given data.  
[PUT /users/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=UserService&operation=updateRowUsers&role=-1) |  [Users, Drivers, Customers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowUsers record for the given data.
