# McLeod API Documentation - String

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=java.lang.String

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)

# String

`String` values are represented as a sequential set of characters. Some characters must be escaped depending on the representation used for transfer mechanism. For example, the ampersand (`&`) must be escaped as `&amp;` in XML.

Omitted values are interpreted as `null`.

## Example

For example, if you had a `widget` with an `id` integer field and a `descr` String field, it might look like:

### XML
    
    
    <widget id="1" descr="Red &amp; Blue Widget"/>

### JSON
    
    
    {"__type":"widget", "id":"1", "descr":"Red & Blue Widget"}

## See also

  * [About `null` Values](https://tms-cfaa.loadtracking.com:5690/ws/docs/types?type=null&role=-1)
  * [java.lang.String JavaDocs](http://docs.oracle.com/javase/11/docs/api/java/lang/String.html)
  * [W3 XML Character Data Syntax](http://www.w3.org/TR/xml/#syntax)
  * [JSON Syntax](http://json.org)


