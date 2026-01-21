# McLeod API Documentation - SettlementService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=SettlementService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# SettlementService

This service provides methods for retrieving settlements (paid and unpaid), payroll history and earnings/deductions.

## Operations

name | role | description  
---|---|---  
[GET /settlements](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=getSettlements&role=-1) |  [Users, Drivers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of unpaid settlement records for the given parameters.  
[GET /settlements/history](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=getSettlementHistory&role=-1) |  [Users, Drivers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of paid settlement records for the given parameters.  
[GET /settlements/history/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=getSettlementHistoryByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for settlement history matching the given request parameters.  
[GET /settlements/history/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=getSettlementHistoryById&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the settlement history record for the given ID.  
[GET /settlements/new](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=newSettlement&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a settlement object with all configured defaults set. This doesn't create a record in the database. Instead, callers of this method can edit the returned object and then pass it back to the create method to actually insert the record in the database.  
[GET /settlements/payrollHistory](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=getPayrollHistory&role=-1) |  [Users, Drivers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of payroll history records for the given parameters.  
[GET /settlements/payrollHistory/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=getPayrollHistoryById&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the payroll history record for the given ID.  
[GET /settlements/reports/paidSettlements](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=getPaidSettlementsReport&role=-1) |  [Users, Drivers, Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Runs the settlement summary report for the given driver and check date range.  
[GET /settlements/search](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=getSettlementsByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Searches the database for settlements matching the given request parameters.  
[GET /settlements/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=getSettlementById&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns the requested unpaid settlement record.  
[POST /settlements/reverseTransfer/{reverseTransferBy}/{reverseTransferIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=reverseSettlementTransfer&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Reverses a settlement for the provided transfer id values  
[POST /settlements/transfer/{transferBy}/{transferIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=transferToSettlement&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Transfers the provided transfer id values to settlement.  
[PUT /settlements/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=SettlementService&operation=createSettlement&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a new settlement record for the given data.
