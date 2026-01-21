# McLeod API Documentation - /currency/currencyControl

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCurrencyControl&role=-1&service=CurrencyService

---

go back to [CurrencyService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CurrencyService&role=-1)

# GET /currency/currencyControl

The endpoint has no roles. 

## Parameters

_This method has no parameters._

* * *

## Result

[RowCurrencyControl](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowCurrencyControl&role=-1) _of type: application/xml application/json_

## Request Details

**Endpoint:** `GET /currency/currencyControl`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /currency/currencyControl HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
