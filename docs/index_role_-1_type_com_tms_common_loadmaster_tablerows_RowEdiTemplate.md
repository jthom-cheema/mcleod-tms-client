# McLeod API Documentation - RowEdiTemplate

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=com.tms.common.loadmaster.tablerows.RowEdiTemplate

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowEdiTemplate

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <edi_template company_id="..." id="..." ack_required="..." app_receiver_code="..." app_receiver_id="..." app_sender_code="..." app_sender_id="..." authen_info="..." authen_info_qual="..." ctl_version="..." ctl_version_qual="..." descr="..." direction="..." ele_separator="..." end_of_line_1="..." end_of_line_2="..." filepath="..." format_type="..." functional_id="..." industry="..." is_multi_partner="..." name="..." parse_batch_number="..." parse_create_date="..." parse_create_datef="..." parse_fg_segment="..." parse_tran_ctrl_no="..." parse_tran_segment="..." receiver_id="..." receiver_qual="..." secur_info="..." secur_info_qual="..." sender_id="..." sender_qual="..." spec_footer_text="..." spec_header_text="..." spec_title="..." standard="..." subele_separator="..." tag_format_text="..." test_indicator="..." transaction_set="..." transaction_type="..." translation_method="..." update_date="..." version="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"edi_template","company_id":"...","id":"...","ack_required":"...","app_receiver_code":"...","app_receiver_id":"...","app_sender_code":"...","app_sender_id":"...","authen_info":"...","authen_info_qual":"...","ctl_version":"...","ctl_version_qual":"...","descr":"...","direction":"...","ele_separator":"...","end_of_line_1":"...","end_of_line_2":"...","filepath":"...","format_type":"...","functional_id":"...","industry":"...","is_multi_partner":"...","name":"...","parse_batch_number":"...","parse_create_date":"...","parse_create_datef":"...","parse_fg_segment":"...","parse_tran_ctrl_no":"...","parse_tran_segment":"...","receiver_id":"...","receiver_qual":"...","secur_info":"...","secur_info_qual":"...","sender_id":"...","sender_qual":"...","spec_footer_text":"...","spec_header_text":"...","spec_title":"...","standard":"...","subele_separator":"...","tag_format_text":"...","test_indicator":"...","transaction_set":"...","transaction_type":"...","translation_method":"...","update_date":"...","version":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| ack_required |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| app_receiver_code |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| app_receiver_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| app_sender_code |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| app_sender_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| authen_info |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| authen_info_qual |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ctl_version |  5  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ctl_version_qual |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| descr |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| direction |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ele_separator |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| end_of_line_1 |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| end_of_line_2 |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| filepath |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| format_type |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| functional_id |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| industry |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| is_multi_partner |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| name |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| parse_batch_number |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| parse_create_date |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| parse_create_datef |  30  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| parse_fg_segment |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| parse_tran_ctrl_no |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| parse_tran_segment |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| receiver_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| receiver_qual |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| secur_info |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| secur_info_qual |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| sender_id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| sender_qual |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| spec_footer_text |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| spec_header_text |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| spec_title |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| standard |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| subele_separator |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| tag_format_text |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| test_indicator |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| transaction_set |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| transaction_type |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| translation_method |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| update_date |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| version |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
