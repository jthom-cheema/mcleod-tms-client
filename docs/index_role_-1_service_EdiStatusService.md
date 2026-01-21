# McLeod API Documentation - EdiStatusService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=EdiStatusService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# EdiStatusService

This service provides operations for retrieving and managing EDI shipment statuses.

## Operations

name | role | description  
---|---|---  
[GET /ediStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=getEdiStatusesByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowEdiStatus objects with a full or partial match to the given value.  
[GET /ediStatus/partners/{direction}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=getEdiStatusPartners&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of shipment status partners for a specified direction.  
[GET /ediStatus/retrieveRecords](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=getEdiStatuses&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to retrieve a List of EdiBatch objects for a single batch number, a range of batch numbers, or a range of dates.  
[GET /ediStatus/retrieveRecords/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=getNewEdiStatuses&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to retrieve a List of 'new' EdiBatch objects (those not already sent to or retrieved by the partner).  
[GET /ediStatus/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=getEdiStatusesByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for shipment statuses matching the given request parameters.  
[GET /ediStatus/summaryBatchInfo](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=getEdiStatusBatchSummaryInfo&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a summary of batch information for the selected partner and range of batches.  
[GET /ediStatus/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowEdiStatus objects based on an existing saved search.  
[GET /ediStatus/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=getRowEdiStatus&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a RowEdiStatus object for the given shipment status ID.  
[GET /ediStatus/{id}/rawDataWithErrors](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=getRawDataWithErrors&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the raw data and error information for a single shipment status.  
[POST /ediStatus/submit](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=submitStatuses&role=-1) |  [Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to submit status data for processing.  
[POST /ediStatus/transmitBatches](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=transmitBatches&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Submits a transmission request for the specified EDI shipment status batches for a specified profile ID.  
[PUT /ediStatus/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiStatusService&operation=updateStatus&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowEdiStatus record for the given status data.
