# McLeod API Documentation - BillingService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=BillingService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# BillingService

This service provides operations that enable access to bills, billing history, miscellaneous billing, reprints and open items.

## Operations

name | role | description  
---|---|---  
[GET /billing](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=getUnpostedBillsByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of unposted billing records matching the given request parameters.  
[GET /billing/cashReceipts](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=getCashReceipts&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of open items matching the given request parameters, posted through cash receipts.  
[GET /billing/history](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=getBillingHistoryByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a List of historical freight billing records matching the given request parameters.  
[GET /billing/history/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=getBillHistory&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves details for the requested historical freight billing record.  
[GET /billing/miscBilling](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=getMiscBillByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of miscellaneous bills matching the given request parameters.  
[GET /billing/miscBilling/history](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=getMiscBillHistoryByAdvancedSearch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of historical miscellaneous bills matching the given request parameters.  
[GET /billing/miscBilling/history/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=getUnpostedMiscBillHist&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves details for the requested miscellaneous bill history.  
[GET /billing/miscBilling/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=getUnpostedMiscBill&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves details for the requested miscellaneous bill.  
[GET /billing/printBill](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=printBill&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Prints a freight bill based on the given criteria and returns a PDF to the caller.  
[GET /billing/reprint](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=reprintFreightBill&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Reprints a freight bill based on the given criteria and returns a PDF to the caller.  
[GET /billing/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=getUnpostedBill&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the billing record identified by the given ID.  
[POST /billing/postBills](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=billingPost&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Posts provided parameter list to billing history.  
[POST /billing/transfer/{transferBy}/{transferIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=transferToBilling&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Transfers the provided id values to billing.  
[POST /billing/unTransfer/{orderId}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=unTransferFromBilling&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Removes existing billing record and sets order back to untransferred status.  
[PUT /billing/cashReceipts/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=createCashReceiptsBatch&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a cash receipts batch. The batch header, receipt header and detail rows must all be included. Detail totals must match the check total. All check totals must match the header total.  
[PUT /billing/miscBilling/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=createMiscBill&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a miscellaneous bill. At least one detail records must be included.  
[PUT /billing/update](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=BillingService&operation=updateBill&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates a RowBilling record for the given data.
