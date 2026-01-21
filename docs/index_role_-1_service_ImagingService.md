# McLeod API Documentation - ImagingService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=ImagingService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# ImagingService

This service provides operations that fetch images and data out of and allows for new images to be placed in Imaging.

## Operations

name | role | description  
---|---|---  
[GET /images/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ImagingService&operation=getImage&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the image for the given ID from Imaging. If no mimetype is supplied, we'll default it as "application/pdf" for PDF since it can handle multi-page TIFFs that imaging often contains. If you send a different type like "image/png" and the image from imaging is a multi-page TIFF, you will most likely get the first page of the TIFF, although that's not guaranteed.  
[GET /images/{rowType}/{rowId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ImagingService&operation=getImageList&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of images available for the given type and ID.  
[GET /images/{rowType}/{rowId}/documentTypes](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ImagingService&operation=getImageTypes&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Gets the list of document types available for the row.  
[POST /images/{rowType}/{rowId}/{documentTypeId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=ImagingService&operation=addImage&role=-1) |  [Users, Drivers, Carriers, Carrier Drivers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Stores the uploaded image into imaging. Some providers may simply stage the uploaded image and later pick it up with a batch process whereas others may immediately store it, making it ready for immediate retrieval.
