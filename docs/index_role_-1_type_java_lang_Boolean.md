# McLeod API Documentation - Boolean

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=java.lang.Boolean

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)

# Boolean

`Boolean` values may be represented by the following case-insensitive values:

  * `true` \- y, yes, t, true, 1, on
  * `false` \- anything else



Omitted values are interpreted as `null` when the service expects a `Boolean` and `false` when the service expects a `boolean` unless specified otherwise.

## Example

For example, if you had a `widget` with an `id` integer field and an `is_active` boolean field, it might look like:

### XML
    
    
    <widget id="1" is_active="Y"/>

### JSON
    
    
    {"__type":"widget", "id":"1", "is_active":"Y"}

## See also

  * [About `null` Values](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=null&role=-1)
  * [java.lang.Boolean JavaDocs](http://docs.oracle.com/javase/11/docs/api/java/lang/Boolean.html)


