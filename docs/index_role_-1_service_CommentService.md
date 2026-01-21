# McLeod API Documentation - CommentService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CommentService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CommentService

This service contains endpoints for retrieval and manipulation of comments and comment attachments.

## Operations

name | role | description  
---|---|---  
[DELETE /comments/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&operation=deleteComment&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Deletes a comments record with the given ID.  
[GET /comments/commentTypes](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&operation=getCommentTypes&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Produces a list of active comment types as defined in LoadMaster.  
[GET /comments/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&operation=getComment&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a comment by its ID.  
[GET /comments/{id}/attachment](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&operation=getAttachment&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves an attachment stored with a comment, if it exists.  
[GET /comments/{id}/thumbnail](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&operation=getThumbnail&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a PNG thumbnail of the attachment stored with a comment, if it exists. Image attachments yield smaller versions, PDF attachments yield a small version of the first page, other known file types such as Microsoft Word and Excel yield simple generic images of the file types and everything else yields a generic image with a question mark.  
[GET /comments/{parentRowType}/{parentRowId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&operation=getComments&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of comments for a given parent row type and row ID. For example, driver BJM01 would be requested as "/D/BJM01", where 'D' represents the parent row type of a driver and 'BJM01' the ID for the driver record.  
[PUT /comments/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&operation=createComment&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a comments record for the given comment data.  
[PUT /comments/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&operation=updateComment&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a comments record for the given comment data.  
[PUT /comments/{id}/attachFile](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CommentService&operation=attachFile&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | 
