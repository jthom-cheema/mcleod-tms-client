# McLeod API Documentation - EdiOrderService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=EdiOrderService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# EdiOrderService

This service provides operations for retrieving and managing EDI load tender records.

## Operations

name | role | description  
---|---|---  
[GET /ediOrder](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getEdiOrdersByQuery&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowEdiOrder with a full or partial match to the given value.  
[GET /ediOrder/ltx](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getLTXEdiOrdersForUser&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List  object containing load tenders matching the Load Tender Express Profile that is in use for the supplied user ID.  
[GET /ediOrder/retrieveRecords](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getEdiOrders&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to retrieve order information (format driven by DataFusion mapper) for a single batch number, a range of batch numbers, or a range of dates.  
[GET /ediOrder/retrieveRecords/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getNewEdiOrders&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to retrieve order information (format driven by DataFusion mapper) (those not already sent to or retrieved by the partner).  
[GET /ediOrder/retrieveRecords/reply](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getEdiOrderReply&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to retrieve existing order reply information (format driven by DataFusion mapper) for a single batch number, a range of batch numbers, or a range of dates.  
[GET /ediOrder/retrieveRecords/reply/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getNewEdiOrderReply&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to retrieve order reply information (format driven by DataFusion mapper) (those not already sent to or retrieved by the partner).  
[GET /ediOrder/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getEdiOrdersByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for load tenders matching the given request parameters.  
[GET /ediOrder/userSavedSearch](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=userSavedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of RowEdiOrder objects based on an existing saved search.  
[GET /ediOrder/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getRowEdiOrder&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a RowEdiOrder object for the given load tender ID.  
[GET /ediOrder/{id}/rawDataWithErrors](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getRawDataWithErrors&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the raw data and error information for a single load tender.  
[GET /ediOrder/{id}/replyRawDataWithErrors](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getReplyRawDataWithErrors&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the reply raw data and error information for a single load tender.  
[GET /ediOrder/{id}/replyReasonCodes](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=getEdiReplyReasonCodesForRowEdiOrder&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the reply reason codes that are appropriate for a RowEdiOrder, as determined by the ID.  
[PUT /ediOrder/submitReply](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=submitReplies&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to submit reply data for processing.  
[PUT /ediOrder/submitTender](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=submitTenders&role=-1) |  [Users, Fusion Partners](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Allows a partner to submit order data for processing.  
[PUT /ediOrder/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=updateEdiOrder&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowEdiOrder record for the given load tender data.  
[PUT /ediOrder/{id}/excludeFromLTX](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=excludeFromLTX&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Marks the 'Exclude from LT Express' (a.k.a. 'Skip Display') flag for the specified RowEdiOrder, as determined by the ID.  
[PUT /ediOrder/{id}/makeOrder](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=makeOrder&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Attempts to make order from a specified RowEdiOrder, as determined by the ID, without attempting to reply.  
[PUT /ediOrder/{id}/reply/submit](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=EdiOrderService&operation=submitReply&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Replies to a specific RowEdiOrder, as determined by the ID, with the specified action, reason code, and remark.
