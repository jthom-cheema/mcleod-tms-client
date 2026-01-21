# McLeod API Documentation - CarrierOfferService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CarrierOfferService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CarrierOfferService

This service provides methods to retrieve, create, counter and decline carrier offers

## Operations

name | role | description  
---|---|---  
[ /carrierOffers](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&operation=getConfirmation&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /carrierOffers/history](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&operation=getOfferHistory&role=-1) |  [Carriers](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a list of carrier offer history records.  
[GET /carrierOffers/offerTerms](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&operation=getOfferTerms&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns the order offer terms set in mobile service control. Currently, this only returns limited fields.  
[GET /carrierOffers/{id}/confTerms](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&operation=getConfTerms&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns the confirmation terms pdf.  
[GET /carrierOffers/{id}/legalTerms](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&operation=getLegalTerms&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Returns the legal terms pdf set in mobile service control.  
[POST /carrierOffers/{id}/counter](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&operation=counterOffer&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Submits new counter offer for the given RowCarrierOffer.  
[PUT /carrierOffers/create](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&operation=createCarrierOffer&role=-1) |  [Freight Matching](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Creates a carrier counter offer record for the given carrier and amount towards the given movement   
This carrier must either be identified by McLeod carrier ID, or by MC number including contact information (name and phone number, or name and email address).   
  
[PUT /carrierOffers/{id}/accept](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&operation=acceptOffer&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Accepts the given RowCarrierOffer.  
[PUT /carrierOffers/{id}/decline](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierOfferService&operation=declineOffer&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Declines the given RowCarrierOffer.
