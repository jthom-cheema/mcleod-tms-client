# McLeod API Documentation - LinkService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=LinkService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# LinkService

This service provides methods for retrieving links that are typically displayed on the menu screens of the mobile apps.

## Operations

name | role | description  
---|---|---  
[GET /links](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LinkService&operation=getMyLinks&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of mobile link records appropriate for the current user.  
[GET /links/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LinkService&operation=getLink&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a link based on the specified ID.  
[GET /links/{id}/icon](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=LinkService&operation=getIcon&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves an icon stored with a link, if it exists.
