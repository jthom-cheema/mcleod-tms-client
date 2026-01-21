# McLeod API Documentation - RowMobileService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=com.tms.common.loadmaster.tablerows.RowMobileService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowMobileService

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <mobile_service company_id="..." id="..." ack_drvr_key="..." ack_drvr_lic="..." allow_driver_history_report="..." allow_driver_rec="..." allow_geotab_sso="..." allow_time_off_feature="..." android_app_url="..." apns_certificate="..." apns_password="..." base_url="..." dr_contact_email="..." dr_contact_name="..." dr_contact_phone="..." dr_email_list="..." dr_response="..." driver_arrived_flag="..." driver_settlement_flag="..." drvr_lic_cert="..." enable_begin_end_trips="..." enable_bol_prompt="..." enable_location_rating="..." enable_raterequest="..." excluded_companies="..." gcm_sender_key="..." invite_expire="..." ios_app_url="..." legal_terms="..." legal_terms_name="..." login_expire="..." max_search="..." mobile_branding_id="..." ord_contact_name="..." ord_contact_phone="..." ord_email_list="..." ord_submit_ok="..." ping_birthday="..." ping_equip_issues="..." ping_hiredate="..." ping_license_expire="..." ping_mvr_expire="..." ping_physical_expire="..." proof_of_delivery="..." qualcom_enable="..." rate_request_text="..." require_legal_term="..." require_order_term="..." scac="..." time_off_event_code="..." tracking_email="..." update_mcleod="..." use_mcleod_relay="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"mobile_service","company_id":"...","id":"...","ack_drvr_key":"...","ack_drvr_lic":"...","allow_driver_history_report":"...","allow_driver_rec":"...","allow_geotab_sso":"...","allow_time_off_feature":"...","android_app_url":"...","apns_certificate":"...","apns_password":"...","base_url":"...","dr_contact_email":"...","dr_contact_name":"...","dr_contact_phone":"...","dr_email_list":"...","dr_response":"...","driver_arrived_flag":"...","driver_settlement_flag":"...","drvr_lic_cert":"...","enable_begin_end_trips":"...","enable_bol_prompt":"...","enable_location_rating":"...","enable_raterequest":"...","excluded_companies":"...","gcm_sender_key":"...","invite_expire":"...","ios_app_url":"...","legal_terms":"...","legal_terms_name":"...","login_expire":"...","max_search":"...","mobile_branding_id":"...","ord_contact_name":"...","ord_contact_phone":"...","ord_email_list":"...","ord_submit_ok":"...","ping_birthday":"...","ping_equip_issues":"...","ping_hiredate":"...","ping_license_expire":"...","ping_mvr_expire":"...","ping_physical_expire":"...","proof_of_delivery":"...","qualcom_enable":"...","rate_request_text":"...","require_legal_term":"...","require_order_term":"...","scac":"...","time_off_event_code":"...","tracking_email":"...","update_mcleod":"...","use_mcleod_relay":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| ack_drvr_key |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| ack_drvr_lic |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| allow_driver_history_report |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| allow_driver_rec |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| allow_geotab_sso |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| allow_time_off_feature |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| android_app_url |  500  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apns_certificate |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| apns_password |  100  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| base_url |  500  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| dr_contact_email |  60  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| dr_contact_name |  40  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| dr_contact_phone |  20  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| dr_email_list |  200  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| dr_response |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| driver_arrived_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| driver_settlement_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| drvr_lic_cert |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| enable_begin_end_trips |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| enable_bol_prompt |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| enable_location_rating |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| enable_raterequest |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| excluded_companies |  100  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gcm_sender_key |  100  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| invite_expire |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| ios_app_url |  500  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| legal_terms |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| legal_terms_name |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| login_expire |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| max_search |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| mobile_branding_id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ord_contact_name |  40  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ord_contact_phone |  20  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ord_email_list |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ord_submit_ok |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ping_birthday |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ping_equip_issues |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ping_hiredate |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ping_license_expire |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ping_mvr_expire |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ping_physical_expire |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| proof_of_delivery |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| qualcom_enable |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rate_request_text |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| require_legal_term |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| require_order_term |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| scac |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| time_off_event_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| tracking_email |  60  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| update_mcleod |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| use_mcleod_relay |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
