# McLeod API Documentation - About null values

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/types?role=-1&type=null

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)

# About `null` Values

The service does not include XML attributes or JSON properties for `null` values. They are omitted to save space and time.

However, when sending data to the service, callers may omit fields. In this case, these fields are not nulled out. To send a `null` value, pass the word "NULL" in upper-case. 

## Examples

For example, if you had a `widget` with an `id` integer field, an `is_active` boolean field and a `descr` String field, it might look like:

### XML

#### Sending this widget to the service will not null out the `descr` field.
    
    
    <widget id="1" is_active="Y"/>

#### Sending this widget to the service will null out the `descr` field.
    
    
    <widget id="1" is_active="Y" descr="NULL"/>

### JSON

#### Sending this widget to the service will not null out the `descr` field.
    
    
    {"__type":"widget", "id":"1", "is_active":"Y"}

#### Sending this widget to the service will null out the `descr` field.
    
    
    {"__type":"widget", "id":"1", "is_active":"Y", "descr":"NULL"}
