# McLeod API Documentation - EdiBillingService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=EdiBillingService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# EdiBillingService

This service provides operations for retrieving and managing EDI Billing records.

## Operations

name | role | description  
---|---|---  
[GET /ediBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=getEdiBillsByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowEdiBilling objects with a full or partial match to the given value.  
[GET /ediBilling/partners/{direction}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=getEdiBillingPartners&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of EDI Billing partners for a specified direction.  
[GET /ediBilling/retrieveRecords](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=getEdiBills&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to retrieve a List of EdiBatch objects for a single batch number, a range of batch numbers, or a range of dates.  
[GET /ediBilling/retrieveRecords/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=getNewEdiBills&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to retrieve a List of 'new' EdiBatch objects (those not already sent to or retrieved by the partner).  
[GET /ediBilling/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=getEdiBillsByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for EDI Bills matching the given request parameters.  
[GET /ediBilling/summaryBatchInfo](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=getEdiBillingBatchSummaryInfo&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a summary of batch information for the selected partner and range of batches.  
[GET /ediBilling/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowEdiBilling objects based on an existing saved search.  
[GET /ediBilling/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=getRowEdiBilling&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a RowEdiBilling object for the given EDI Billing ID.  
[GET /ediBilling/{id}/rawDataWithErrors](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=getRawDataWithErrors&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the raw data and error information for a single EDI Bill.  
[POST /ediBilling/submit](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=submitInvoices&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to submit billing data for processing.  
[POST /ediBilling/transmitBatches](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=transmitBatches&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Submits a transmission request for the specified EDI Billing batches for a specified profile ID.  
[PUT /ediBilling/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiBillingService&operation=updateBill&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowEdiBilling record for the given billing data.
