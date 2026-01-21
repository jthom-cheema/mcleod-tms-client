# McLeod API Documentation - List

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=java.util.List

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)

# List

When making a search-related call on the web services, the result is often a `List`. This is necessary because an XML document may only have one root node. Since our services originated with XML implementations, this rule holds over to present day even for other representations like JSON. Like Java, the sequence/order of the objects in a List is important.

Lists are never accepted as input for any call.

## Example

For example, if you had a `widget` with an `id` integer field and a `descr` String field, it might look like:

### XML
    
    
    <list><widget id="1" descr="Red Widget"/><widget id="2" descr="Blue Widget"/></list>

### JSON
    
    
    [{"__type":"widget", "id":"1", "descr":"Red Widget"},{"__type":"widget", "id":"2", "descr":"Blue Widget"}]

## See also

  * [java.util.List JavaDocs](http://docs.oracle.com/javase/11/docs/api/java/util/List.html)


