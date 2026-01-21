# Getting Started with McLeod TMS API

This guide will help you get started using the McLeod TMS API.

## Overview

The McLeod TMS API provides programmatic access to LoadMaster™/PowerBroker™ logic and data. It follows REST principles and supports both XML and JSON formats.

## Base URL

```
https://tms-cfaa.loadtracking.com:5690/ws
```

## Authentication

All API requests require authentication. The API supports:

### Basic Authentication
Standard HTTP Basic Authentication using username and password.

### Token Authentication
Token-based authentication (details available in the API documentation).

**Note:** Authentication details are available at: `https://tms-cfaa.loadtracking.com:5690/ws/docs/auth?role=-1`

## Required Headers

### Company ID
Most requests require the `X-com.mcleodsoftware.CompanyID` header to specify which company's data to access:

```
X-com.mcleodsoftware.CompanyID: <your-company-id>
```

### Accept Header
Specify the response format you want:

```
Accept: application/json
```
or
```
Accept: application/xml
```

**Default:** If not specified, XML is the default format.

## Response Formats

### XML Format
- Element names match database table names
- Fields are attributes on elements
- Easy to parse with SAX parsers

### JSON Format
- Table name in `__type` field
- All other fields are name/value pairs
- Standard JSON structure

## Common Operations

### Get an Order
```http
GET /orders/{id}
Authorization: Basic <credentials>
X-com.mcleodsoftware.CompanyID: <company-id>
Accept: application/json
```

### Create an Order
```http
PUT /orders/create
Authorization: Basic <credentials>
X-com.mcleodsoftware.CompanyID: <company-id>
Content-Type: application/json
Accept: application/json

{
  "__type": "orders",
  "customer_id": "...",
  ...
}
```

### Update an Order
```http
PUT /orders/update
Authorization: Basic <credentials>
X-com.mcleodsoftware.CompanyID: <company-id>
Content-Type: application/json
Accept: application/json

{
  "__type": "orders",
  "id": "...",
  ...
}
```

## Role-Based Access

Different operations require different roles:
- **Users** - Full access to most operations
- **Drivers** - Limited access for driver operations
- **Customers** - Access to customer-specific data
- **Carriers** - Access to carrier-specific data
- **Carrier Drivers** - Access for carrier driver operations

Check individual operation pages for specific role requirements.

## Finding What You Need

1. **Start with [QUICK_REFERENCE.md](QUICK_REFERENCE.md)** for common operations
2. **Browse [SERVICES_BY_CATEGORY.md](SERVICES_BY_CATEGORY.md)** to find services by function
3. **Check [ENDPOINTS_REFERENCE.md](ENDPOINTS_REFERENCE.md)** for all available endpoints
4. **See [SERVICES_INDEX.md](SERVICES_INDEX.md)** for complete service list
5. **Look up types in [TYPES_INDEX.md](TYPES_INDEX.md)**

## Example Workflow

### Creating and Managing an Order

1. **Get a new order template:**
   ```
   GET /orders/new
   ```
   Returns an order object with defaults populated.

2. **Modify the order:**
   Edit the returned object with your order details.

3. **Create the order:**
   ```
   PUT /orders/create
   ```
   Pass the modified order object in the request body.

4. **Retrieve the order:**
   ```
   GET /orders/{id}
   ```
   Use the ID returned from the create operation.

5. **Update the order:**
   ```
   PUT /orders/update
   ```
   Pass the modified order object.

## Error Handling

The API returns standard HTTP status codes:
- `200 OK` - Successful request
- `400 Bad Request` - Invalid request parameters
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Best Practices

1. **Always include the CompanyID header** for multi-company environments
2. **Use appropriate Accept headers** to get your preferred format
3. **Check role requirements** before calling operations
4. **Review type definitions** to understand data structures
5. **Use the "new" operations** to get templates with defaults

## Next Steps

- Explore [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for common patterns
- Browse [SERVICES_BY_CATEGORY.md](SERVICES_BY_CATEGORY.md) to find relevant services
- Check individual service pages for detailed operation documentation
- Review type definitions to understand data structures

## Additional Resources

- [Complete Services Index](SERVICES_INDEX.md)
- [All Endpoints](ENDPOINTS_REFERENCE.md)
- [Types Reference](TYPES_INDEX.md)
- [Full Documentation Index](INDEX.md)

