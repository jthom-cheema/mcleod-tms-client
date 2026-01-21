# McLeod API Documentation - RowQuoteFreightGroupItem

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowQuoteFreightGroupItem

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowQuoteFreightGroupItem

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <quote_freight_group_item company_id="..." fgi_uid="..." add_timestamp="..." add_userid="..." commodity_id="..." cubic_units="..." delivery_stop_id="..." density="..." description="..." dunnage_weight="..." exceeds_volume="..." fgi_commodity_type_code="..." fgi_damage_type_code="..." fgi_packaging_type_code="..." fgi_sequence_nbr="..." fgi_status_code="..." fgi_value="..." fgi_value_c="..." fgi_value_d="..." fgi_value_n="..." fgi_value_r="..." fgp_uid="..." freight_weight="..." handling_units="..." hazmat="..." hazmat_bulk_flag="..." hazmat_class_code="..." hazmat_emergency_number="..." hazmat_erg_number="..." hazmat_is_residue="..." hazmat_packing_group="..." hazmat_proper_shipname="..." hazmat_qty_code="..." hazmat_ref_type_code="..." hazmat_reference_data="..." hazmat_subclass_code="..." hazmat_subsidiary_code="..." hazmat_unna_nbr="..." height="..." is_poison="..." length="..." linear_units="..." mod_timestamp="..." mod_userid="..." nmfc_class_code="..." nmfc_code="..." override_class_code="..." pickup_stop_id="..." pieces="..." placard_required="..." poison_zone="..." product_sku="..." req_spots="..." scan_unit_type="..." seats="..." ship_ref_nbr="..." signoff_text="..." weight="..." weight_uom_type_code="..." width="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"quote_freight_group_item","company_id":"...","fgi_uid":"...","add_timestamp":"...","add_userid":"...","commodity_id":"...","cubic_units":"...","delivery_stop_id":"...","density":"...","description":"...","dunnage_weight":"...","exceeds_volume":"...","fgi_commodity_type_code":"...","fgi_damage_type_code":"...","fgi_packaging_type_code":"...","fgi_sequence_nbr":"...","fgi_status_code":"...","fgi_value":"...","fgi_value_c":"...","fgi_value_d":"...","fgi_value_n":"...","fgi_value_r":"...","fgp_uid":"...","freight_weight":"...","handling_units":"...","hazmat":"...","hazmat_bulk_flag":"...","hazmat_class_code":"...","hazmat_emergency_number":"...","hazmat_erg_number":"...","hazmat_is_residue":"...","hazmat_packing_group":"...","hazmat_proper_shipname":"...","hazmat_qty_code":"...","hazmat_ref_type_code":"...","hazmat_reference_data":"...","hazmat_subclass_code":"...","hazmat_subsidiary_code":"...","hazmat_unna_nbr":"...","height":"...","is_poison":"...","length":"...","linear_units":"...","mod_timestamp":"...","mod_userid":"...","nmfc_class_code":"...","nmfc_code":"...","override_class_code":"...","pickup_stop_id":"...","pieces":"...","placard_required":"...","poison_zone":"...","product_sku":"...","req_spots":"...","scan_unit_type":"...","seats":"...","ship_ref_nbr":"...","signoff_text":"...","weight":"...","weight_uom_type_code":"...","width":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgi_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| add_timestamp |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| add_userid |  25  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| commodity_id |  9  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| cubic_units |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| delivery_stop_id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| density |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| description |  256  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| dunnage_weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| exceeds_volume |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgi_commodity_type_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgi_damage_type_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgi_packaging_type_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgi_sequence_nbr |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| fgi_status_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgi_value |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| fgi_value_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fgi_value_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| fgi_value_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| fgi_value_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| fgp_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| freight_weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| handling_units |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| hazmat |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_bulk_flag |  1  |  [boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=boolean?role=-1)  
| hazmat_class_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_emergency_number |  16  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_erg_number |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_is_residue |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_packing_group |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_proper_shipname |  256  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_qty_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_ref_type_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_reference_data |  64  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_subclass_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_subsidiary_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| hazmat_unna_nbr |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| height |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| is_poison |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| length |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| linear_units |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| mod_timestamp |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| mod_userid |  25  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| nmfc_class_code |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| nmfc_code |  20  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| override_class_code |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| pickup_stop_id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| pieces |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| placard_required |  40  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| poison_zone |  7  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| product_sku |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| req_spots |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| scan_unit_type |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| seats |  16.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| ship_ref_nbr |  24  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| signoff_text |  256  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| weight |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| weight_uom_type_code |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| width |  53.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)
