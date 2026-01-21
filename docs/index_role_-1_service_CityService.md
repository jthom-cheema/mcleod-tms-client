# McLeod API Documentation - CityService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=CityService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# CityService

This service provides operations that allow callers to get city records.

## Operations

name | role | description  
---|---|---  
[GET /cities](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CityService&operation=findCities&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /cities/db](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CityService&operation=buildSqliteDB&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) |   
[GET /cities/findNearestCity](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CityService&operation=findNearestCity&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Finds the nearest RowCity given a latitude and longitude. This method queries all records from the city table that are within a pretend fence around the latitude and longitude.  
[GET /cities/{id}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=CityService&operation=getCity&role=-1) |  [](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | 
