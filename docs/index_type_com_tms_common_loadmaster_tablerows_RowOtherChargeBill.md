# McLeod API Documentation - RowOtherChargeBill

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowOtherChargeBill

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)

# RowOtherChargeBill

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <other_charge_bill company_id="..." id="..." allocated_charge_key="..." allocation_method="..." amount="..." amount_c="..." amount_d="..." amount_n="..." amount_r="..." bill_type="..." calc_method="..." charge_id="..." customer_id="..." ded_charge_customer_id="..." descr="..." driver_id="..." empty_distance_units="..." empty_distance_units_um="..." est_fuel_surcharge="..." incl_in_freight="..." invoice_id="..." is_dedicated_distance="..." is_taxable="..." loaded_distance_units="..." loaded_distance_units_um="..." ltl_allocation_method="..." maximum_units="..." minimum_units="..." order_id="..." order_oc_id="..." rate="..." rate_id="..." revenue_share_order_id="..." sequence="..." stop_id="..." stop_loc_name="..." stop_no="..." tli_uid="..." units="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"other_charge_bill","company_id":"...","id":"...","allocated_charge_key":"...","allocation_method":"...","amount":"...","amount_c":"...","amount_d":"...","amount_n":"...","amount_r":"...","bill_type":"...","calc_method":"...","charge_id":"...","customer_id":"...","ded_charge_customer_id":"...","descr":"...","driver_id":"...","empty_distance_units":"...","empty_distance_units_um":"...","est_fuel_surcharge":"...","incl_in_freight":"...","invoice_id":"...","is_dedicated_distance":"...","is_taxable":"...","loaded_distance_units":"...","loaded_distance_units_um":"...","ltl_allocation_method":"...","maximum_units":"...","minimum_units":"...","order_id":"...","order_oc_id":"...","rate":"...","rate_id":"...","revenue_share_order_id":"...","sequence":"...","stop_id":"...","stop_loc_name":"...","stop_no":"...","tli_uid":"...","units":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| allocated_charge_key |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| allocation_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| amount |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| amount_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| amount_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| amount_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| amount_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| bill_type |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| calc_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| charge_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| customer_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ded_charge_customer_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| descr |  28  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| driver_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| empty_distance_units |  10.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| empty_distance_units_um |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| est_fuel_surcharge |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| incl_in_freight |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| invoice_id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| is_dedicated_distance |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| is_taxable |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| loaded_distance_units |  10.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| loaded_distance_units_um |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ltl_allocation_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| maximum_units |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| minimum_units |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| order_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| order_oc_id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rate |  12.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| rate_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| revenue_share_order_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| sequence |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| stop_id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| stop_loc_name |  40  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| stop_no |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| tli_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| units |  12.4  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)
