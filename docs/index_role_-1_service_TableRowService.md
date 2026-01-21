# McLeod API Documentation - TableRowService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=TableRowService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# TableRowService

This service provides a generic interface for retrieving, creating and updating TableRows. This service allows safe access to any table in the database because it makes sure that auditing, permissions and validation code runs before making changes.

## Operations

name | role | description  
---|---|---  
[ /{table}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=loadRelatedRecords&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[DELETE /{table}/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=delete&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /{table}/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=neww&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /{table}/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=find&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for provided table matching the given request parameters.  
[GET /{table}/unvalidatedsearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=findUnvalidated&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for provided table matching the given request parameters.  
[GET /{table}/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=get&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /{table}/{orderBy}/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=find&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /{table}/{orderby}/unvalidatedsearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=findUnvalidated&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[POST /{table}/{id}/{method}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=executeInstanceMethod&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[POST /{table}/{method}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=executeStaticMethod&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[PUT /{table}/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=create&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[PUT /{table}/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=TableRowService&operation=update&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | 
