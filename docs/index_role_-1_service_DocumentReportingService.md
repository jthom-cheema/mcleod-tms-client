# McLeod API Documentation - DocumentReportingService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=DocumentReportingService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# DocumentReportingService

This service provides access to Document Designer reports. Callers can retrieve templates and run existing reports.

## Operations

name | role | description  
---|---|---  
[GET /documents/customTemplates](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DocumentReportingService&operation=getCustomReportTemplates&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of all custom and label type document designer report templates.  
[GET /documents/reportRunner/{type}/{template}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DocumentReportingService&operation=runReport&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns the requested custom report in PDF format.
