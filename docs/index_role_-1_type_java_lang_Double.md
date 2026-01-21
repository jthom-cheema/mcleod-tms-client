# McLeod API Documentation - Double

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=java.lang.Double

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)

# Double

`Double` values may be real numbers from `4.9E-324` to `1.7976931348623157E308` unless specified otherwise. Negative numbers must be prefixed with a minus sign. If the field, value or both are omitted, `null` will be used instead.

## Example

For example, if you had a `widget` with an `id` Double field and an `weight` Double field, it might look like:

### XML
    
    
    <widget id="1" weight="-5.25"/>

### JSON
    
    
    {"__type":"widget", "id":"1", "weight":"-5.25"}

## See also

  * [About `null` Values](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=null&role=-1)
  * [java.lang.Double JavaDocs](http://docs.oracle.com/javase/11/docs/api/java/lang/Double.html)


