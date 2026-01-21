# McLeod API Documentation - RowWireCode

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=com.tms.common.loadmaster.tablerows.RowWireCode

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowWireCode

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <wirecode company_id="..." id="..." allow_aft_xfer_settlement="..." ap_glid="..." carrier_limit_amount="..." carrier_limit_amount_c="..." carrier_limit_amount_d="..." carrier_limit_amount_n="..." carrier_limit_amount_r="..." carrier_limit_method="..." carrier_order_pct_limit="..." carrier_valid_move_status="..." charge_code_id="..." company_limit_amount="..." company_limit_amount_c="..." company_limit_amount_d="..." company_limit_amount_n="..." company_limit_amount_r="..." company_limit_method="..." company_order_pct_limit="..." company_valid_move_status="..." contract_carrier="..." contract_driver="..." contract_no_payee="..." contract_ownerop="..." create_deduction="..." create_other_charge="..." deduct_code_id="..." deduct_in_provider_currency="..." deduct_status="..." descr="..." driver_fee_amt="..." driver_fee_amt_c="..." driver_fee_amt_d="..." driver_fee_amt_n="..." driver_fee_amt_r="..." expense_glid="..." fuel_interface_id="..." include_fee_exp="..." is_active="..." is_atm_cash="..." issuing_user_group="..." issuing_users="..." msts_addl_fee_percent="..." msts_addl_fee_threshold="..." msts_addl_fee_threshold_c="..." msts_addl_fee_threshold_d="..." msts_addl_fee_threshold_n="..." msts_addl_fee_threshold_r="..." no_validation="..." ownerop_limit_amount="..." ownerop_limit_amount_c="..." ownerop_limit_amount_d="..." ownerop_limit_amount_n="..." ownerop_limit_amount_r="..." ownerop_limit_method="..." ownerop_order_pct_limit="..." ownerop_valid_move_status="..." plus_minus="..." require_order="..." service_charge="..." service_charge_c="..." service_charge_d="..." service_charge_n="..." service_charge_r="..." subaccount_carrier="..." subaccount_driver="..." subaccount_no_payee="..." subaccount_ownerop="..." unposted_wire_status="..." wire_type="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"wirecode","company_id":"...","id":"...","allow_aft_xfer_settlement":"...","ap_glid":"...","carrier_limit_amount":"...","carrier_limit_amount_c":"...","carrier_limit_amount_d":"...","carrier_limit_amount_n":"...","carrier_limit_amount_r":"...","carrier_limit_method":"...","carrier_order_pct_limit":"...","carrier_valid_move_status":"...","charge_code_id":"...","company_limit_amount":"...","company_limit_amount_c":"...","company_limit_amount_d":"...","company_limit_amount_n":"...","company_limit_amount_r":"...","company_limit_method":"...","company_order_pct_limit":"...","company_valid_move_status":"...","contract_carrier":"...","contract_driver":"...","contract_no_payee":"...","contract_ownerop":"...","create_deduction":"...","create_other_charge":"...","deduct_code_id":"...","deduct_in_provider_currency":"...","deduct_status":"...","descr":"...","driver_fee_amt":"...","driver_fee_amt_c":"...","driver_fee_amt_d":"...","driver_fee_amt_n":"...","driver_fee_amt_r":"...","expense_glid":"...","fuel_interface_id":"...","include_fee_exp":"...","is_active":"...","is_atm_cash":"...","issuing_user_group":"...","issuing_users":"...","msts_addl_fee_percent":"...","msts_addl_fee_threshold":"...","msts_addl_fee_threshold_c":"...","msts_addl_fee_threshold_d":"...","msts_addl_fee_threshold_n":"...","msts_addl_fee_threshold_r":"...","no_validation":"...","ownerop_limit_amount":"...","ownerop_limit_amount_c":"...","ownerop_limit_amount_d":"...","ownerop_limit_amount_n":"...","ownerop_limit_amount_r":"...","ownerop_limit_method":"...","ownerop_order_pct_limit":"...","ownerop_valid_move_status":"...","plus_minus":"...","require_order":"...","service_charge":"...","service_charge_c":"...","service_charge_d":"...","service_charge_n":"...","service_charge_r":"...","subaccount_carrier":"...","subaccount_driver":"...","subaccount_no_payee":"...","subaccount_ownerop":"...","unposted_wire_status":"...","wire_type":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  5  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| allow_aft_xfer_settlement |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ap_glid |  20  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| carrier_limit_amount |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| carrier_limit_amount_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| carrier_limit_amount_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| carrier_limit_amount_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| carrier_limit_amount_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| carrier_limit_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| carrier_order_pct_limit |  6.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| carrier_valid_move_status |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| charge_code_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| company_limit_amount |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| company_limit_amount_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| company_limit_amount_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| company_limit_amount_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| company_limit_amount_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| company_limit_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| company_order_pct_limit |  6.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| company_valid_move_status |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| contract_carrier |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| contract_driver |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| contract_no_payee |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| contract_ownerop |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| create_deduction |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| create_other_charge |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| deduct_code_id |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| deduct_in_provider_currency |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| deduct_status |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| descr |  25  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| driver_fee_amt |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| driver_fee_amt_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| driver_fee_amt_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| driver_fee_amt_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| driver_fee_amt_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| expense_glid |  20  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fuel_interface_id |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| include_fee_exp |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| is_active |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| is_atm_cash |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| issuing_user_group |  254  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| issuing_users |  254  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| msts_addl_fee_percent |  6.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| msts_addl_fee_threshold |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| msts_addl_fee_threshold_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| msts_addl_fee_threshold_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| msts_addl_fee_threshold_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| msts_addl_fee_threshold_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| no_validation |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ownerop_limit_amount |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| ownerop_limit_amount_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ownerop_limit_amount_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| ownerop_limit_amount_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| ownerop_limit_amount_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| ownerop_limit_method |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ownerop_order_pct_limit |  6.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| ownerop_valid_move_status |  12  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| plus_minus |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| require_order |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| service_charge |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| service_charge_c |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| service_charge_d |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| service_charge_n |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| service_charge_r |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| subaccount_carrier |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| subaccount_driver |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| subaccount_no_payee |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| subaccount_ownerop |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| unposted_wire_status |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| wire_type |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
