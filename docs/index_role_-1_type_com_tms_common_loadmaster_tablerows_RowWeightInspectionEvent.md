# McLeod API Documentation - RowWeightInspectionEvent

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=com.tms.common.loadmaster.tablerows.RowWeightInspectionEvent

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowWeightInspectionEvent

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <weight_inspection_event company_id="..." id="..." location_id="..." new_total_charge="..." new_total_charge_c="..." new_total_charge_d="..." new_total_charge_n="..." new_total_charge_r="..." old_total_charge="..." old_total_charge_c="..." old_total_charge_d="..." old_total_charge_n="..." old_total_charge_r="..." order_id="..." recorded_by_user="..." recorded_timestamp="..." requested_by_user="..." requested_timestamp="..." wi_status_code="..." wi_type_code="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"weight_inspection_event","company_id":"...","id":"...","location_id":"...","new_total_charge":"...","new_total_charge_c":"...","new_total_charge_d":"...","new_total_charge_n":"...","new_total_charge_r":"...","old_total_charge":"...","old_total_charge_c":"...","old_total_charge_d":"...","old_total_charge_n":"...","old_total_charge_r":"...","order_id":"...","recorded_by_user":"...","recorded_timestamp":"...","requested_by_user":"...","requested_timestamp":"...","wi_status_code":"...","wi_type_code":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| location_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| new_total_charge |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| new_total_charge_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| new_total_charge_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| new_total_charge_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| new_total_charge_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| old_total_charge |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| old_total_charge_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| old_total_charge_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| old_total_charge_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| old_total_charge_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| order_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| recorded_by_user |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| recorded_timestamp |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| requested_by_user |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| requested_timestamp |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| wi_status_code |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| wi_type_code |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
