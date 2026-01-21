# McLeod TMS API Quick Reference

This guide provides quick access to common API operations and patterns.

## Common Services

### Order Management
- **OrderService** - Create, update, and manage orders
  - `GET /orders/{id}` - Get order by ID
  - `PUT /orders/create` - Create new order
  - `PUT /orders/update` - Update existing order
  - See [OrderService operations](SERVICES_INDEX.md#orderservice)

### Movement Management  
- **MovementService** - Manage movements (loads)
  - `GET /movements/{id}` - Get movement by ID
  - `PUT /movements/create` - Create new movement
  - See [MovementService operations](SERVICES_INDEX.md#movementservice)

### Customer Management
- **CustomerService** - Manage customer records
  - `GET /customers/{id}` - Get customer by ID
  - `PUT /customers/create` - Create new customer
  - See [CustomerService operations](SERVICES_INDEX.md#customerservice)

### Carrier Management
- **CarrierService** - Manage carrier records
  - `GET /carriers/{id}` - Get carrier by ID
  - `PUT /carriers/create` - Create new carrier
  - See [CarrierService operations](SERVICES_INDEX.md#carrierservice)

### Driver Management
- **DriverService** - Manage driver records
  - `GET /drivers/{id}` - Get driver by ID
  - `PUT /drivers/create` - Create new driver
  - See [DriverService operations](SERVICES_INDEX.md#driverservice)

## Common Types

### Core Table Rows
- `RowOrders` - Order records
- `RowMovement` - Movement/load records
- `RowCustomer` - Customer records
- `RowCarrier` - Carrier records
- `RowDriver` - Driver records
- `RowStop` - Stop records
- `RowLocation` - Location records

See [Types Index](TYPES_INDEX.md) for complete list.

## Authentication

All API requests require authentication. See individual operation pages for required roles.

Common authentication methods:
- Basic Authentication
- Token Authentication

## Response Formats

The API supports both XML and JSON formats. Set the `Accept` header:
- `application/xml` for XML
- `application/json` for JSON

## Company ID

Most requests require the `X-com.mcleodsoftware.CompanyID` header to specify which company's data to access.

## Navigation

- [Services Index](SERVICES_INDEX.md) - All services organized by name
- [Types Index](TYPES_INDEX.md) - All types organized by namespace
- [Complete Index](INDEX.md) - Flat list of all pages

## File Naming Convention

- Service overview: `index_role_-1_service_{ServiceName}.md`
- Operation: `index_operation_{operationName}_role_-1_service_{ServiceName}.md`
- Type: `index_role_-1_type_{TypeName}.md` or `index_type_{TypeName}.md`

