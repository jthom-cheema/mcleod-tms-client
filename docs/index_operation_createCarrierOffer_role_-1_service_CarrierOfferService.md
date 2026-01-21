# McLeod API Documentation - /carrierOffers/create

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?operation=createCarrierOffer&role=-1&service=CarrierOfferService

---

go back to [CarrierOfferService](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&role=-1)

# PUT /carrierOffers/create

Creates a carrier counter offer record for the given carrier and amount towards the given movement   
This carrier must either be identified by McLeod carrier ID, or by MC number including contact information (name and phone number, or name and email address).   

Roles that can access this endpoint are [ Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1). 

## Parameters

name | description | type | default | type  
---|---|---|---|---  
carrierId | (Optional) ID of the carrier creating the counter offer record |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
movementId | (Required) ID of the movement the counter offer is being created for |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
offeredRate | (Required) Counter offer rate of the offer |  query  |  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal&role=-1)  
mcNumber | (Optional) MC number of the carrier (no prefix, at most 12 digits)   
**Ignored if carrier ID is provided** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
dotNumber | (Optional) DOT number of the carrier (no prefix, at most 10 digits)   
**Ignored if carrier ID is provided** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
carrierName | (Optional) Name of the carrier creating the counter offer record   
**Ignored if carrier ID is provided** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
contactPhone | (Optional) Contact phone number to be used   
**Defaults to the phone number of the carrier's primary contact** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
contactEmail | (Optional) Contact email address to be used   
**Defaults to the email address of the carrier's primary contact** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
contactName | (Optional) Contact name to be used   
**No default value** |  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
comments | (Optional) Comments to be added to the counter offer record   
**There is no default value**   
  
Additional details: 

  * Counter offer can only be created for available broker movements 
  * Upon successful creation of the counter offer an Order Post History record will be created in PowerBroker and associated with the order that is associated with the given movement 
  * Upon successful creation of the counter offer an email will be sent to the recipients that are set in the PowerBroker Freight Matching control 

|  query  |  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String&role=-1)  
  
* * *

## Result

[Response](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=javax.ws.rs.core.Response&role=-1) _of type: application/xml application/json_

No data is returned

## Request Details

**Endpoint:** `PUT /carrierOffers/create`

### Headers

- **Authorization:** Required
  - See [Authentication Help](https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1)
  - Supported: Basic, Token

- **X-com.mcleodsoftware.CompanyID:** Required (company identifier)

- **Accept:** application/xml application/json
  - Default: application/xml (if not specified)

### Example Request

```http
PUT /carrierOffers/create HTTP/1.1
X-com.mcleodsoftware.CompanyID: <your-company-id>
Authorization: Basic <credentials>
Accept: application/xml
```
