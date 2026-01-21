# McLeod API Documentation - RowEdiBillingProfile

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowEdiBillingProfile

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowEdiBillingProfile

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <edibilling_profile company_id="..." id="..." ack_xmit_method="..." allow_corrections="..." alt_partner_id="..." always_update_stop="..." apply_chassis_adds="..." apply_container_adds="..." apply_ep_adds="..." apply_ep_chgs="..." apply_ep_dels="..." apply_frt_adds="..." apply_frt_chgs="..." apply_frt_dels="..." apply_hdr_adds="..." apply_hdr_chgs="..." apply_hdr_dels="..." apply_move_chgs="..." apply_note_adds="..." apply_note_dels="..." apply_oc_adds="..." apply_oc_chgs="..." apply_oc_dels="..." apply_order_chgs="..." apply_refno_adds="..." apply_refno_chgs="..." apply_refno_dels="..." apply_stop_adds="..." apply_stop_chgs="..." apply_stop_dels="..." audit_cutoff_days="..." audit_interval="..." auto_accept="..." auto_compare="..." auto_compare_rt="..." auto_create_order="..." auto_deliver_order="..." auto_rate="..." carrier_id="..." compare_update="..." days_to_retain="..." direction="..." edi_comm_id="..." enf_batch_cont="..." enf_batch_cont_997="..." english_printer="..." error_options="..." error_rpt_printer="..." fa_threshold="..." filename="..." func_ack_filename="..." func_ack_st02_frmt="..." func_ack_tid="..." func_altpartner_id="..." func_comm_id="..." func_next_batch="..." func_partner_id="..." func_use_m_batch="..." func_version="..." img_def_loc_dir="..." img_dir_local="..." img_document_types="..." img_filetype="..." img_required="..." individual_batch="..." intercompany="..." next_batch="..." notes="..." partner_id="..." partner_name="..." print_before_send="..." print_bills="..." process_priority="..." purge_rpt_printer="..." remove_file="..." send_func_ack="..." send_to_company="..." skip_manual_orders="..." special_processing="..." st02_format="..." template_id="..." transaction_set="..." transmit_method="..." updaterecs_how="..." use_master_batch="..." use_ok2send="..." use_show_as="..." version="..." zip_filename="..." zip_images="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"edibilling_profile","company_id":"...","id":"...","ack_xmit_method":"...","allow_corrections":"...","alt_partner_id":"...","always_update_stop":"...","apply_chassis_adds":"...","apply_container_adds":"...","apply_ep_adds":"...","apply_ep_chgs":"...","apply_ep_dels":"...","apply_frt_adds":"...","apply_frt_chgs":"...","apply_frt_dels":"...","apply_hdr_adds":"...","apply_hdr_chgs":"...","apply_hdr_dels":"...","apply_move_chgs":"...","apply_note_adds":"...","apply_note_dels":"...","apply_oc_adds":"...","apply_oc_chgs":"...","apply_oc_dels":"...","apply_order_chgs":"...","apply_refno_adds":"...","apply_refno_chgs":"...","apply_refno_dels":"...","apply_stop_adds":"...","apply_stop_chgs":"...","apply_stop_dels":"...","audit_cutoff_days":"...","audit_interval":"...","auto_accept":"...","auto_compare":"...","auto_compare_rt":"...","auto_create_order":"...","auto_deliver_order":"...","auto_rate":"...","carrier_id":"...","compare_update":"...","days_to_retain":"...","direction":"...","edi_comm_id":"...","enf_batch_cont":"...","enf_batch_cont_997":"...","english_printer":"...","error_options":"...","error_rpt_printer":"...","fa_threshold":"...","filename":"...","func_ack_filename":"...","func_ack_st02_frmt":"...","func_ack_tid":"...","func_altpartner_id":"...","func_comm_id":"...","func_next_batch":"...","func_partner_id":"...","func_use_m_batch":"...","func_version":"...","img_def_loc_dir":"...","img_dir_local":"...","img_document_types":"...","img_filetype":"...","img_required":"...","individual_batch":"...","intercompany":"...","next_batch":"...","notes":"...","partner_id":"...","partner_name":"...","print_before_send":"...","print_bills":"...","process_priority":"...","purge_rpt_printer":"...","remove_file":"...","send_func_ack":"...","send_to_company":"...","skip_manual_orders":"...","special_processing":"...","st02_format":"...","template_id":"...","transaction_set":"...","transmit_method":"...","updaterecs_how":"...","use_master_batch":"...","use_ok2send":"...","use_show_as":"...","version":"...","zip_filename":"...","zip_images":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ack_xmit_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| allow_corrections |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| alt_partner_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| always_update_stop |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_chassis_adds |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_container_adds |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_ep_adds |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_ep_chgs |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_ep_dels |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_frt_adds |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_frt_chgs |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_frt_dels |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_hdr_adds |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_hdr_chgs |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_hdr_dels |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_move_chgs |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_note_adds |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_note_dels |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_oc_adds |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_oc_chgs |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_oc_dels |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_order_chgs |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_refno_adds |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_refno_chgs |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_refno_dels |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_stop_adds |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_stop_chgs |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| apply_stop_dels |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| audit_cutoff_days |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| audit_interval |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| auto_accept |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| auto_compare |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| auto_compare_rt |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| auto_create_order |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| auto_deliver_order |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| auto_rate |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| carrier_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| compare_update |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| days_to_retain |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| direction |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| edi_comm_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| enf_batch_cont |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| enf_batch_cont_997 |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| english_printer |  75  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| error_options |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| error_rpt_printer |  75  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
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
| img_def_loc_dir |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| img_dir_local |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| img_document_types |  20  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| img_filetype |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| img_required |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| individual_batch |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| intercompany |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| next_batch |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| notes |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| partner_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| partner_name |  40  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| print_before_send |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| print_bills |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| process_priority |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| purge_rpt_printer |  75  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| remove_file |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| send_func_ack |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| send_to_company |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| skip_manual_orders |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| special_processing |  48  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| st02_format |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| template_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| transaction_set |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| transmit_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| updaterecs_how |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| use_master_batch |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| use_ok2send |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| use_show_as |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| version |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| zip_filename |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| zip_images |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
