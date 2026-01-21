# McLeod API Documentation - BigDecimal

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=java.math.BigDecimal

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# BigDecimal

`BigDecimal` values may be real numbers with no minimum or maximum unless specified otherwise. Negative numbers must be prefixed with a minus sign. If the field, value or both are omitted, `null` will be used instead.

## Example

For example, if you had a `widget` with an `id` BigDecimal field and an `weight` BigDecimal field, it might look like:

### XML
    
    
    <widget id="1" weight="-5.25"/>

### JSON
    
    
    {"__type":"widget", "id":"1", "weight":"-5.25"}

## See also

  * [About `null` Values](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=null&role=-1)
  * [java.math.BigDecimal JavaDocs](http://docs.oracle.com/javase/11/docs/api/java/math/BigDecimal.html)


