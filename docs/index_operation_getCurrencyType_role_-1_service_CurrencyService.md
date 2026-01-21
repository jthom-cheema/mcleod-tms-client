# McLeod API Documentation - /currency/currencyTypes/{id}

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=getCurrencyType&role=-1&service=CurrencyService

---

go back to [CurrencyService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CurrencyService&role=-1)

# GET /currency/currencyTypes/{id}

Retrieves the details for a specific CurrencyType record.

The endpoint has no roles. 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
id | the ID of the currency type to be returned |  path  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[RowCurrencyType](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.tablerows.RowCurrencyType&role=-1) _of type: application/xml application/json_

a RowCurrencyType record containing the details for the requested record   
  
Additional attributes: 

  * `__indicator_color_hex` This value represents the hex value of the currency's indicator value (int), found in the `currency_type.indicator_color` field.
  * `__availableInCurrentCompany` This value represents whether the currency type is available in the current company.

## Request Details

**Endpoint:** `GET /currency/currencyTypes/{id}`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
GET /currency/currencyTypes/{id} HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
