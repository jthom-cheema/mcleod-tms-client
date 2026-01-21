# McLeod API Documentation - Date

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=com.tms.common.lib.Date

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)

# Date

## Parameter Values

`Date` parameter values are parsed using a [Pattern](http://docs.oracle.com/javase/11/docs/api/java/util/regex/Pattern.html) determined by the `loadmaster.ws.useServerTimezone` vmparam value. When the vmparam is set to `true`, the pattern is `yyyyMMddHHmmss` and when it is `false`, the pattern is `yyyyMMddHHmmssZ`. Currently, this vmparam is set to `false`.

Omitted parameters evaluate as `null`.

Letters  |  Date or Time Component  |  Example  
---|---|---  
`yyyy` | Year | `2020`  
`MM` | Month in year | `07`  
`dd` | Day in month | `04`  
`HH` | Hour in day (0-23) | `08`  
`mm` | Minute in hour | `05`  
`ss` | Second in minute | `00`  
`Z` | Time zone (RFC 822) | `-0500`  
  
## Response Values

A Date field is formatted using a [SimpleDateFormat](http://docs.oracle.com/javase/11/docs/api/java/text/SimpleDateFormat.html) instance.

### XML

#### This widget has a `create_date` of August 16, 2016 5:01PM CDT.
    
    
    <widget id="1" create_date="20160816170100-0500"/>

### JSON

#### This widget has a `create_date` of August 16, 2016 5:01PM CDT.
    
    
    {"__type":"widget", "id":"1", "create_date":"20160816170100-0500"}

## Request Body Values

Within a request body, services also accept LoadMaster™/PowerBroker™ date shortcut patterns.

  * `n` \- now (today at current time)
  * `t` \- today
  * `m` \- first day of current month
  * `w` \- first day of current week
  * `q` \- first day of current quarter
  * `y` \- first day of current year
  * `me` \- last day of current month
  * `we` \- last day of current week
  * `qe` \- last day of current quarter
  * `ye` \- last day of current year



Simple addition and subtraction on these values is supported. For example, use `t1` for tomorrow and `t-7` for one week ago.

Except for `n` (now), by default shortcut patterns use midnight `0000` for the time component. To specify the time component, include the hours and minutes as two digits each in military time (between `0000` and `2359`). For example, to specify tomorrow at 1:30PM, use `t1 1330`.

## See also

  * [About `null` Values](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=null&role=-1)
  * [Boolean](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=java.lang.Boolean&role=-1) (for more on acceptable values for the vmparam)
  * [java.text.SimpleDateFormat JavaDocs](http://docs.oracle.com/javase/11/docs/api/java/text/SimpleDateFormat.html)


