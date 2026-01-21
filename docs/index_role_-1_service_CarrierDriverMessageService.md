# McLeod API Documentation - CarrierDriverMessageService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CarrierDriverMessageService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CarrierDriverMessageService

This service provides methods for viewing and sending driver text messages.

## Operations

name | role | description  
---|---|---  
[GET /carrierDriverMessages](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&operation=getCarrierDriverMessages&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Gets all driver text messages matching the request criteria. If no criteria given, then all driver text messages for the current company are returned. For example, `/carrierDriverMessages?order_id=0256189` would find driver text messages for order 0256189.  
[GET /carrierDriverMessages/previewMessage](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&operation=previewMessage&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the composed message.  
[GET /carrierDriverMessages/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&operation=getCarrierDriverMessage&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves the driver text message based on the specified ID.  
[GET /carrierDriverMessages/{id}/thumbnail](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&operation=getThumbnail&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Retrieves a PNG thumbnail of the attachment stored with a message, if it exists.  
[POST /carrierDriverMessages/sendMessage](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&operation=sendMessage&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Sends the composed message and updates certain records (carrier_driver, order_post_hist, and movement) based on the supplied query parameters.  
[POST /carrierDriverMessages/{id}/messageRead](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&operation=updateMessageRead&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates the driver text message with the specified ID as read or unread.  
[POST /carrierDriverMessages/{id}/resend](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&operation=resendMessage&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Resends the driver text message with the specified ID.  
[POST /carrierDriverMessages/{id}/updateStatus](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CarrierDriverMessageService&operation=updateStatus&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Updates the status of the driver text message with the specified ID.
