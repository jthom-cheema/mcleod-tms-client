# McLeod API Documentation - RowMobileBranding

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=com.tms.common.loadmaster.tablerows.RowMobileBranding

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# RowMobileBranding

## Sample XML

The following is only an example of what the XML should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    <mobile_branding company_id="..." id="..." about_img="..." about_img_path="..." about_img_type="..." about_img_uselogo="..." about_text="..." appicon="..." appicon_path="..." appicon_type="..." appname="..." company_logo="..." company_logo_path="..." company_logo_type="..." contactus_email="..." contactus_subj="..." gplay_category="..." gplay_desc="..." gplay_desc_s="..." gplay_email="..." gplay_featgr="..." gplay_featgr_path="..." gplay_featgr_type="..." gplay_phone="..." gplay_priv_url="..." gplay_site_url="..." gplay_title="..." itunes_cat_1="..." itunes_cat_2="..." itunes_copyrt="..." itunes_descr="..." itunes_keywords="..." itunes_mkt_url="..." itunes_sup_url="..." itunes_title="..." last_date_sent="..." last_updated="..." profile_name="..." wallpaper_jpg="..." wallpaper_path="..."/>

## Sample JSON

The following is only an example of what the JSON should look like. The order of fields is not guaranteed and null fields are not included in returned data from the services.
    
    
    {"__type":"mobile_branding","company_id":"...","id":"...","about_img":"...","about_img_path":"...","about_img_type":"...","about_img_uselogo":"...","about_text":"...","appicon":"...","appicon_path":"...","appicon_type":"...","appname":"...","company_logo":"...","company_logo_path":"...","company_logo_type":"...","contactus_email":"...","contactus_subj":"...","gplay_category":"...","gplay_desc":"...","gplay_desc_s":"...","gplay_email":"...","gplay_featgr":"...","gplay_featgr_path":"...","gplay_featgr_type":"...","gplay_phone":"...","gplay_priv_url":"...","gplay_site_url":"...","gplay_title":"...","itunes_cat_1":"...","itunes_cat_2":"...","itunes_copyrt":"...","itunes_descr":"...","itunes_keywords":"...","itunes_mkt_url":"...","itunes_sup_url":"...","itunes_title":"...","last_date_sent":"...","last_updated":"...","profile_name":"...","wallpaper_jpg":"...","wallpaper_path":"..."}

## Fields

key | name | size | type  
---|---|---|---  
| company_id |  4  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| id |  32  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| about_img |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| about_img_path |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| about_img_type |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| about_img_uselogo |  1  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| about_text |  2048  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| appicon |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| appicon_path |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| appicon_type |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| appname |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| company_logo |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| company_logo_path |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| company_logo_type |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| contactus_email |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| contactus_subj |  100  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_category |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_desc |  4000  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_desc_s |  80  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_email |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_featgr |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| gplay_featgr_path |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_featgr_type |  3  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_phone |  20  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_priv_url |  2048  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_site_url |  2048  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| gplay_title |  30  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| itunes_cat_1 |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| itunes_cat_2 |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| itunes_copyrt |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| itunes_descr |  4000  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| itunes_keywords |  100  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| itunes_mkt_url |  2048  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| itunes_sup_url |  2048  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| itunes_title |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| last_date_sent |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| last_updated |  19  |  [Date](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=com.tms.common.lib.Date?role=-1)  
| profile_name |  50  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)  
| wallpaper_jpg |  20  |  [byte[]](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=\[B?role=-1)  
| wallpaper_path |  255  |  [String](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.String?role=-1)
