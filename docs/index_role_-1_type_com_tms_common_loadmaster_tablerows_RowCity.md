# McLeod API Documentation - RowCity

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=com.tms.common.loadmaster.tablerows.RowCity

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowCity

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <city company_id="..." id="..." airport_code="..." alk_id="..." central_location="..." county="..." inactive="..." isi_id="..." latitude="..." longitude="..." name="..." pcm_window_city_id="..." rmm_id="..." state_id="..." three_digit_zip="..." timezone_id="..." zip_code="..." zone_id="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"city","company_id":"...","id":"...","airport_code":"...","alk_id":"...","central_location":"...","county":"...","inactive":"...","isi_id":"...","latitude":"...","longitude":"...","name":"...","pcm_window_city_id":"...","rmm_id":"...","state_id":"...","three_digit_zip":"...","timezone_id":"...","zip_code":"...","zone_id":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| airport_code |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| alk_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| central_location |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| county |  45  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| inactive |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| isi_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| latitude |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| longitude |  10.6  |  [BigDecimal](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.math.BigDecimal?role=-1)  
| name |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| pcm_window_city_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| rmm_id |  10  |  [int](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=int?role=-1)  
| state_id |  2  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| three_digit_zip |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| timezone_id |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| zip_code |  10  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| zone_id |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
