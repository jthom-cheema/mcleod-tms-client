# McLeod API Documentation - AlertService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=AlertService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# AlertService

This service provides access to rapid alert messages. Callers may retrieve messages and mark them read or confirmed.

## Operations

name | role | description  
---|---|---  
[GET /alerts/messageCount](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&operation=getTotalUnreadCountForUser&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns the number of unread messages across all companies the user is registered in.  
[GET /alerts/messages](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&operation=getAlertsForUser&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of rapid alerts for the given user. The User ID is not passed as a parameter, but rather is determined by the Device ID in the request header.  
[GET /alerts/messages/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&operation=getRapidAlertMsg&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves an RowRapidAlertMsg object for the given rapid alert message ID.  
[GET /alerts/summary](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&operation=getAlertSummaryForUser&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves summary rapid alert information for the given user. The User ID is not passed as a parameter, but rather is determined by the Device ID in the request header.  
[POST /alerts/messages/confirm](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&operation=markAlertsConfirmed&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Marks all rapid alerts as confirmed.  
[POST /alerts/messages/read](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&operation=markAlertsRead&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Marks all messages as read, for the given user. The User ID is not passed as a parameter, but rather is determined by the Device ID in the request header.  
[POST /alerts/messages/{id}/confirm](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&operation=markAlertConfirmed&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Marks a specific message, as determined by the ID, as confirmed.  
[POST /alerts/messages/{id}/read](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=AlertService&operation=markAlertRead&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Marks a specific message, as determined by the ID, as read.
