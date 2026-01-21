# McLeod API Documentation - CurrencyService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CurrencyService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CurrencyService

This service provides operations for accessing currency control records including the set of active currency types available in this instance of LoadMaster/PowerBroker.

## Operations

name | role | description  
---|---|---  
[GET /currency/currencyControl](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CurrencyService&operation=getCurrencyControl&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /currency/currencyTypes](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CurrencyService&operation=getActiveCurrencyTypes&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of all active RowCurrencyType objects.  
[GET /currency/currencyTypes/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CurrencyService&operation=getCurrencyType&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the details for a specific CurrencyType record.
