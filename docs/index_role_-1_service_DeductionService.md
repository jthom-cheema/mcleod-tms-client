# McLeod API Documentation - DeductionService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=DeductionService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# DeductionService

This service provides methods for retrieving earnings/deductions.

## Operations

name | role | description  
---|---|---  
[GET /deductions](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&operation=getDeductions&role=-1) |  [Users, Drivers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of pending deduction records for the given parameters.  
[GET /deductions/history](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&operation=getDeductionHistory&role=-1) |  [Users, Drivers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of deduction history records for the given parameters.  
[GET /deductions/history/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&operation=getDeductionHistoryByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for deduction history matching the given request parameters.  
[GET /deductions/history/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&operation=getDeductionHistoryById&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the deduction history record for the given ID.  
[GET /deductions/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&operation=newDeduction&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a pending deduction object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /deductions/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&operation=getDeductionsByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for pending deductions matching the given request parameters.  
[GET /deductions/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&operation=getDeductionById&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns the requested pending deduction record.  
[PUT /deductions/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=DeductionService&operation=createDeduction&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new drs_pending_deduct record for the given data.
