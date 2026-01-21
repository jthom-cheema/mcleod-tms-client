# McLeod API Documentation - RowMcPosition

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=com.tms.common.loadmaster.tablerows.RowMcPosition

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowMcPosition

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <mc_position company_id="..." id="..." auto_home_location="..." direction="..." driver2_id="..." driver_id="..." exclude_fueltax="..." fuel_level="..." geo_id="..." geo_location="..." ignition_on_flag="..." in_zone_id="..." latitude="..." longitude="..." mc_unit_no="..." mc_unit_type="..." movement_id="..." near_b_city="..." near_landmk="..." near_s_city="..." odometer="..." out_zone_id="..." position_date="..." position_status="..." position_type="..." speed="..." stopped_date="..." trp_uid="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"mc_position","company_id":"...","id":"...","auto_home_location":"...","direction":"...","driver2_id":"...","driver_id":"...","exclude_fueltax":"...","fuel_level":"...","geo_id":"...","geo_location":"...","ignition_on_flag":"...","in_zone_id":"...","latitude":"...","longitude":"...","mc_unit_no":"...","mc_unit_type":"...","movement_id":"...","near_b_city":"...","near_landmk":"...","near_s_city":"...","odometer":"...","out_zone_id":"...","position_date":"...","position_status":"...","position_type":"...","speed":"...","stopped_date":"...","trp_uid":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  40  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| auto_home_location |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| direction |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| driver2_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| driver_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| exclude_fueltax |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| fuel_level |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| geo_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| geo_location |  40  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| ignition_on_flag |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| in_zone_id |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| latitude |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| longitude |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| mc_unit_no |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| mc_unit_type |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| movement_id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| near_b_city |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| near_landmk |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| near_s_city |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| odometer |  9.2  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| out_zone_id |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| position_date |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| position_status |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| position_type |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| speed |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| stopped_date |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| trp_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)
