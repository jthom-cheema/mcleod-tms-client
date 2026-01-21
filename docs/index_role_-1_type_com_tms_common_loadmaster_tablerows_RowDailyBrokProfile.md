# McLeod API Documentation - RowDailyBrokProfile

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=com.tms.common.loadmaster.tablerows.RowDailyBrokProfile

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowDailyBrokProfile

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <daily_brok_profile company_id="..." id="..." available_orders="..." carriersalesperson="..." covered_orders="..." cust_salesperson="..." customers="..." day_of_week="..." delivered_orders="..." dispatchers="..." end_date_value="..." exclude_weekend="..." gauge1="..." gauge2="..." gauge3="..." gauge4="..." gauge_refresh="..." inprogress_orders="..." operations_users="..." ord_dspcomp_flag="..." ord_dspmade_flag="..." ord_entorders_flag="..." ord_numorders_flag="..." order_goal_fri="..." order_goal_mon="..." order_goal_sat="..." order_goal_sun="..." order_goal_thu="..." order_goal_tue="..." order_goal_wed="..." order_type="..." pct_target_d_flag="..." pct_target_p_flag="..." profit_diff_flag="..." profit_flag="..." profit_goal_flag="..." profit_goal_fri="..." profit_goal_mon="..." profit_goal_sat="..." profit_goal_sun="..." profit_goal_thu="..." profit_goal_tue="..." profit_goal_wed="..." profit_pct_d_flag="..." profit_pct_flag="..." profit_pct_g_flag="..." profit_pctgoal_fri="..." profit_pctgoal_mon="..." profit_pctgoal_sat="..." profit_pctgoal_sun="..." profit_pctgoal_thu="..." profit_pctgoal_tue="..." profit_pctgoal_wed="..." resp_codes="..." resp_level="..." rev_billed_flag="..." rev_delivered_flag="..." rev_fuelsurch_flag="..." rev_goal_fri="..." rev_goal_mon="..." rev_goal_sat="..." rev_goal_sun="..." rev_goal_thu="..." rev_goal_tue="..." rev_goal_wed="..." rev_gross_flag="..." rev_revenue_d_flag="..." rev_revenue_flag="..." rev_revenue_g_flag="..." rev_shipped_flag="..." rev_total_acc_flag="..." revenue_codes="..." revenue_date_basis="..." revenue_goal_basis="..." start_date_value="..." target_pay_d_flag="..." target_pay_flag="..." title="..." user_list_default="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"daily_brok_profile","company_id":"...","id":"...","available_orders":"...","carriersalesperson":"...","covered_orders":"...","cust_salesperson":"...","customers":"...","day_of_week":"...","delivered_orders":"...","dispatchers":"...","end_date_value":"...","exclude_weekend":"...","gauge1":"...","gauge2":"...","gauge3":"...","gauge4":"...","gauge_refresh":"...","inprogress_orders":"...","operations_users":"...","ord_dspcomp_flag":"...","ord_dspmade_flag":"...","ord_entorders_flag":"...","ord_numorders_flag":"...","order_goal_fri":"...","order_goal_mon":"...","order_goal_sat":"...","order_goal_sun":"...","order_goal_thu":"...","order_goal_tue":"...","order_goal_wed":"...","order_type":"...","pct_target_d_flag":"...","pct_target_p_flag":"...","profit_diff_flag":"...","profit_flag":"...","profit_goal_flag":"...","profit_goal_fri":"...","profit_goal_mon":"...","profit_goal_sat":"...","profit_goal_sun":"...","profit_goal_thu":"...","profit_goal_tue":"...","profit_goal_wed":"...","profit_pct_d_flag":"...","profit_pct_flag":"...","profit_pct_g_flag":"...","profit_pctgoal_fri":"...","profit_pctgoal_mon":"...","profit_pctgoal_sat":"...","profit_pctgoal_sun":"...","profit_pctgoal_thu":"...","profit_pctgoal_tue":"...","profit_pctgoal_wed":"...","resp_codes":"...","resp_level":"...","rev_billed_flag":"...","rev_delivered_flag":"...","rev_fuelsurch_flag":"...","rev_goal_fri":"...","rev_goal_mon":"...","rev_goal_sat":"...","rev_goal_sun":"...","rev_goal_thu":"...","rev_goal_tue":"...","rev_goal_wed":"...","rev_gross_flag":"...","rev_revenue_d_flag":"...","rev_revenue_flag":"...","rev_revenue_g_flag":"...","rev_shipped_flag":"...","rev_total_acc_flag":"...","revenue_codes":"...","revenue_date_basis":"...","revenue_goal_basis":"...","start_date_value":"...","target_pay_d_flag":"...","target_pay_flag":"...","title":"...","user_list_default":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  15  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| available_orders |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| carriersalesperson |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| covered_orders |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| cust_salesperson |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| customers |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| day_of_week |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| delivered_orders |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| dispatchers |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| end_date_value |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| exclude_weekend |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gauge1 |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gauge2 |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gauge3 |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gauge4 |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gauge_refresh |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| inprogress_orders |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| operations_users |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ord_dspcomp_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ord_dspmade_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ord_entorders_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ord_numorders_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| order_goal_fri |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| order_goal_mon |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| order_goal_sat |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| order_goal_sun |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| order_goal_thu |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| order_goal_tue |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| order_goal_wed |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| order_type |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| pct_target_d_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| pct_target_p_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| profit_diff_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| profit_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| profit_goal_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| profit_goal_fri |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_goal_mon |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_goal_sat |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_goal_sun |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_goal_thu |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_goal_tue |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_goal_wed |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_pct_d_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| profit_pct_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| profit_pct_g_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| profit_pctgoal_fri |  5.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_pctgoal_mon |  5.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_pctgoal_sat |  5.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_pctgoal_sun |  5.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_pctgoal_thu |  5.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_pctgoal_tue |  5.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| profit_pctgoal_wed |  5.1  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| resp_codes |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| resp_level |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| rev_billed_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rev_delivered_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rev_fuelsurch_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rev_goal_fri |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| rev_goal_mon |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| rev_goal_sat |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| rev_goal_sun |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| rev_goal_thu |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| rev_goal_tue |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| rev_goal_wed |  16.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| rev_gross_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rev_revenue_d_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rev_revenue_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rev_revenue_g_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rev_shipped_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| rev_total_acc_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| revenue_codes |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| revenue_date_basis |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| revenue_goal_basis |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| start_date_value |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| target_pay_d_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| target_pay_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| title |  60  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| user_list_default |  40  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
