# McLeod API Documentation - Integer

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=int

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)

# Integer

`Integer` values may be whole integral numbers from `-2147483648` to `2147483647` unless specified otherwise. Negative numbers must be prefixed with a minus sign.

If the field, value or both are omitted, `null` will be used when the service uses an `Integer` and `0` will be used when the service uses an `int` unless specified otherwise.

## Example

For example, if you had a `widget` with an `id` integer field and an `pallet_balance` integer field, it might look like:

### XML
    
    
    <widget id="1" pallet_balance="-5"/>

### JSON
    
    
    {"__type":"widget", "id":"1", "pallet_balance":"-5"}

## See also

  * [About `null` Values](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=null&role=-1)
  * [java.lang.Integer JavaDocs](http://docs.oracle.com/javase/11/docs/api/java/lang/Integer.html)


