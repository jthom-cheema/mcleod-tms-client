# McLeod API Documentation - RowProhibited

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.loadmaster.tablerows.RowProhibited

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowProhibited

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <prohibited company_id="..." id="..." bidirectional_lane="..." comments="..." entered_date="..." entered_user_id="..." from_region="..." from_region_uid="..." parent_row_id="..." parent_row_type="..." prohibited_driver_id="..." prohibited_row_id="..." prohibited_row_type="..." to_region="..." to_region_uid="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"prohibited","company_id":"...","id":"...","bidirectional_lane":"...","comments":"...","entered_date":"...","entered_user_id":"...","from_region":"...","from_region_uid":"...","parent_row_id":"...","parent_row_type":"...","prohibited_driver_id":"...","prohibited_row_id":"...","prohibited_row_type":"...","to_region":"...","to_region_uid":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| bidirectional_lane |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| comments |  -1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| entered_date |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| entered_user_id |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| from_region |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| from_region_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| parent_row_id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| parent_row_type |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| prohibited_driver_id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| prohibited_row_id |  8  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| prohibited_row_type |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| to_region |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| to_region_uid |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)
