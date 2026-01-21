# McLeod API Documentation - RowQuoteFreightGroup

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuoteFreightGroup

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowQuoteFreightGroup

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <quote_freight_group company_id="..." fgp_uid="..." add_timestamp="..." add_userid="..." bol_nbr="..." bol_processed="..." cons_ect_uid="..." cons_interline_bol_nbr="..." cons_interline_plc_uid="..." cons_ofrec_plc_uid="..." cons_plc_uid="..." cons_ref_nbr="..." conveyance_id="..." conveyance_owner_plc_uid="..." conveyance_type_code="..." description="..." dest_txl_uid="..." dim_weight_multiplier="..." exceeds_volume="..." fgp_due_timestamp="..." fgp_packaging_type_code="..." fgp_reference_data_1="..." fgp_status_code="..." fgp_tendered_timestamp="..." fgp_type_code="..." fsp_uid="..." inbound_flight_trp_uid="..." lme_order_id="..." mod_timestamp="..." mod_userid="..." offline_dest_txl_uid="..." offline_orig_txl_uid="..." ord_uid="..." orig_txl_uid="..." outbound_flight_trp_uid="..." pro_nbr="..." ship_ect_uid="..." ship_interline_bol_nbr="..." ship_interline_plc_uid="..." ship_ofrec_plc_uid="..." ship_plc_uid="..." ship_ref_nbr="..." stt_uid="..." tendered_chargeable_weight="..." tendered_pieces="..." tendered_spots="..." tendered_weight="..." total_chargeable_weight="..." total_cubic_units="..." total_cubic_volume="..." total_density="..." total_dimensional_weight="..." total_dunnage_weight="..." total_freight_weight="..." total_handling_units="..." total_linear_units="..." total_pieces="..." total_req_spots="..." total_seats="..." total_value="..." total_value_c="..." total_value_d="..." total_value_n="..." total_value_r="..." total_weight="..." transit_days_actual="..." transit_days_standard="..." weight_uom_type_code="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"quote_freight_group","company_id":"...","fgp_uid":"...","add_timestamp":"...","add_userid":"...","bol_nbr":"...","bol_processed":"...","cons_ect_uid":"...","cons_interline_bol_nbr":"...","cons_interline_plc_uid":"...","cons_ofrec_plc_uid":"...","cons_plc_uid":"...","cons_ref_nbr":"...","conveyance_id":"...","conveyance_owner_plc_uid":"...","conveyance_type_code":"...","description":"...","dest_txl_uid":"...","dim_weight_multiplier":"...","exceeds_volume":"...","fgp_due_timestamp":"...","fgp_packaging_type_code":"...","fgp_reference_data_1":"...","fgp_status_code":"...","fgp_tendered_timestamp":"...","fgp_type_code":"...","fsp_uid":"...","inbound_flight_trp_uid":"...","lme_order_id":"...","mod_timestamp":"...","mod_userid":"...","offline_dest_txl_uid":"...","offline_orig_txl_uid":"...","ord_uid":"...","orig_txl_uid":"...","outbound_flight_trp_uid":"...","pro_nbr":"...","ship_ect_uid":"...","ship_interline_bol_nbr":"...","ship_interline_plc_uid":"...","ship_ofrec_plc_uid":"...","ship_plc_uid":"...","ship_ref_nbr":"...","stt_uid":"...","tendered_chargeable_weight":"...","tendered_pieces":"...","tendered_spots":"...","tendered_weight":"...","total_chargeable_weight":"...","total_cubic_units":"...","total_cubic_volume":"...","total_density":"...","total_dimensional_weight":"...","total_dunnage_weight":"...","total_freight_weight":"...","total_handling_units":"...","total_linear_units":"...","total_pieces":"...","total_req_spots":"...","total_seats":"...","total_value":"...","total_value_c":"...","total_value_d":"...","total_value_n":"...","total_value_r":"...","total_weight":"...","transit_days_actual":"...","transit_days_standard":"...","weight_uom_type_code":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgp_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| add_timestamp |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| add_userid |  25  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| bol_nbr |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| bol_processed |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| cons_ect_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| cons_interline_bol_nbr |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| cons_interline_plc_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| cons_ofrec_plc_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| cons_plc_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| cons_ref_nbr |  24  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| conveyance_id |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| conveyance_owner_plc_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| conveyance_type_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| description |  256  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| dest_txl_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| dim_weight_multiplier |  30.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| exceeds_volume |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgp_due_timestamp |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| fgp_packaging_type_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgp_reference_data_1 |  24  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgp_status_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgp_tendered_timestamp |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| fgp_type_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fsp_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| inbound_flight_trp_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| lme_order_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| mod_timestamp |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| mod_userid |  25  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| offline_dest_txl_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| offline_orig_txl_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| ord_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| orig_txl_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| outbound_flight_trp_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| pro_nbr |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ship_ect_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| ship_interline_bol_nbr |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ship_interline_plc_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| ship_ofrec_plc_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| ship_plc_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| ship_ref_nbr |  24  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| stt_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| tendered_chargeable_weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| tendered_pieces |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| tendered_spots |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| tendered_weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_chargeable_weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_cubic_units |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_cubic_volume |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_density |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_dimensional_weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_dunnage_weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_freight_weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_handling_units |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| total_linear_units |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_pieces |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| total_req_spots |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| total_seats |  16.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_value |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_value_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| total_value_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| total_value_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_value_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| total_weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| transit_days_actual |  4.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| transit_days_standard |  4.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| weight_uom_type_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
