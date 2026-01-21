# McLeod API Documentation - RowEdiStatusProfile

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiStatusProfile

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowEdiStatusProfile

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <edistatus_profile company_id="..." id="..." ack_xmit_method="..." agent_payee_id="..." allow_update="..." alt_partner_id="..." audit_cutoff_days="..." audit_interval="..." batch_method="..." carrier_id="..." consolidates_stops="..." create_method="..." create_svrfail="..." days_to_retain="..." delay_req="..." dest_stop_no="..." direction="..." edi_comm_id="..." enf_batch_cont="..." enf_batch_cont_997="..." fa_threshold="..." filename="..." func_ack_filename="..." func_ack_st02_frmt="..." func_ack_tid="..." func_altpartner_id="..." func_comm_id="..." func_next_batch="..." func_partner_id="..." func_use_m_batch="..." func_version="..." hold_for_preverr="..." hold_type="..." ignore_map_errors="..." img_def_loc_dir="..." img_dir_local="..." img_document_types="..." img_filetype="..." img_required="..." individual_batch="..." intercompany="..." next_batch="..." notes="..." orig_stop_no="..." partner_id="..." partner_name="..." process_priority="..." remove_file="..." remove_func_ack="..." send_func_ack="..." send_to_company="..." skip_manual_orders="..." special_processing="..." st02_format="..." status_on_delivery="..." status_on_pickup="..." template_id="..." transaction_set="..." transmit_method="..." update_stop="..." use_master_batch="..." use_show_as="..." version="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"edistatus_profile","company_id":"...","id":"...","ack_xmit_method":"...","agent_payee_id":"...","allow_update":"...","alt_partner_id":"...","audit_cutoff_days":"...","audit_interval":"...","batch_method":"...","carrier_id":"...","consolidates_stops":"...","create_method":"...","create_svrfail":"...","days_to_retain":"...","delay_req":"...","dest_stop_no":"...","direction":"...","edi_comm_id":"...","enf_batch_cont":"...","enf_batch_cont_997":"...","fa_threshold":"...","filename":"...","func_ack_filename":"...","func_ack_st02_frmt":"...","func_ack_tid":"...","func_altpartner_id":"...","func_comm_id":"...","func_next_batch":"...","func_partner_id":"...","func_use_m_batch":"...","func_version":"...","hold_for_preverr":"...","hold_type":"...","ignore_map_errors":"...","img_def_loc_dir":"...","img_dir_local":"...","img_document_types":"...","img_filetype":"...","img_required":"...","individual_batch":"...","intercompany":"...","next_batch":"...","notes":"...","orig_stop_no":"...","partner_id":"...","partner_name":"...","process_priority":"...","remove_file":"...","remove_func_ack":"...","send_func_ack":"...","send_to_company":"...","skip_manual_orders":"...","special_processing":"...","st02_format":"...","status_on_delivery":"...","status_on_pickup":"...","template_id":"...","transaction_set":"...","transmit_method":"...","update_stop":"...","use_master_batch":"...","use_show_as":"...","version":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ack_xmit_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| agent_payee_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| allow_update |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| alt_partner_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| audit_cutoff_days |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| audit_interval |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| batch_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| carrier_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| consolidates_stops |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| create_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| create_svrfail |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| days_to_retain |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| delay_req |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| dest_stop_no |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| direction |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| edi_comm_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| enf_batch_cont |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| enf_batch_cont_997 |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fa_threshold |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| filename |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| func_ack_filename |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| func_ack_st02_frmt |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| func_ack_tid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| func_altpartner_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| func_comm_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| func_next_batch |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| func_partner_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| func_use_m_batch |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| func_version |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hold_for_preverr |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hold_type |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ignore_map_errors |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| img_def_loc_dir |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| img_dir_local |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| img_document_types |  20  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| img_filetype |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| img_required |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| individual_batch |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| intercompany |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| next_batch |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| notes |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| orig_stop_no |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| partner_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| partner_name |  40  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| process_priority |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| remove_file |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| remove_func_ack |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| send_func_ack |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| send_to_company |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| skip_manual_orders |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| special_processing |  48  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| st02_format |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| status_on_delivery |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| status_on_pickup |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| template_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| transaction_set |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| transmit_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| update_stop |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| use_master_batch |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| use_show_as |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| version |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
