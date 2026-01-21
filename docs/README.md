## Vendor documentation snapshot (read-only)

This `docs/` folder is a **snapshot/export of McLeod `/ws/docs` pages** (plus a generated index).

### Rules
- **Treat this folder as read-only.** Don’t “fix” docs here; re-export/regenerate instead.
- **Don’t change `tms_client` just because a doc page exists.** Validate against the live server behavior (many endpoints differ by tenant/version/permissions).
- **No secrets.** This folder must not include credentials, tokens, or customer-private data.

### Entry point
- Start at `docs/INDEX.md`.

# McLeod TMS API Documentation

Complete API documentation for the McLeod TMS system, organized for easy reference by Cursor agents and developers.

## Statistics

- **Total Pages:** 915
- **Services:** 71
- **Operations:** 539
- **Types:** 300

## Quick Start

1. **New to the API?** Start with [GETTING_STARTED.md](GETTING_STARTED.md)
2. **Need common operations?** See [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
3. **Looking for a service by function?** Check [SERVICES_BY_CATEGORY.md](SERVICES_BY_CATEGORY.md)
4. **Need a specific endpoint?** Browse [ENDPOINTS_REFERENCE.md](ENDPOINTS_REFERENCE.md)
5. **Looking for a service?** Check [SERVICES_INDEX.md](SERVICES_INDEX.md)
6. **Need a type definition?** See [TYPES_INDEX.md](TYPES_INDEX.md)
7. **Understanding type usage?** See [TYPE_DEPENDENCIES.md](TYPE_DEPENDENCIES.md)
8. **Browse everything?** Use [INDEX.md](INDEX.md)

## Documentation Structure

### Service Pages
Service overview pages list all operations available for that service.
- Format: `index_role_-1_service_{ServiceName}.md`
- Example: `index_role_-1_service_OrderService.md`

### Operation Pages
Detailed documentation for each API operation.
- Format: `index_operation_{operationName}_role_-1_service_{ServiceName}.md`
- Example: `index_operation_getOrder_role_-1_service_OrderService.md`
- Contains: Endpoint, parameters, return types, examples

### Type Pages
Documentation for data types used in the API.
- Format: `index_role_-1_type_{TypeName}.md` or `index_type_{TypeName}.md`
- Example: `index_type_com_tms_common_loadmaster_tablerows_RowOrders.md`
- Contains: Fields, sample XML/JSON, type information

## Key Files

### Getting Started
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Complete getting started guide with examples
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick access to common operations

### Navigation & Reference
- **[SERVICES_BY_CATEGORY.md](SERVICES_BY_CATEGORY.md)** - Services organized by functional area
- **[SERVICES_INDEX.md](SERVICES_INDEX.md)** - All services with their operations (alphabetical)
- **[ENDPOINTS_REFERENCE.md](ENDPOINTS_REFERENCE.md)** - All endpoints organized by HTTP method
- **[TYPES_INDEX.md](TYPES_INDEX.md)** - All types organized by namespace
- **[TYPE_DEPENDENCIES.md](TYPE_DEPENDENCIES.md)** - Type usage and dependencies
- **[INDEX.md](INDEX.md)** - Complete alphabetical index

## Using This Documentation

### For Cursor Agents

This documentation is optimized for semantic search. Agents can:
- Search for services by name or functionality
- Find operations by endpoint or operation name
- Look up types by class name or namespace
- Reference examples and parameter details

### For Developers

- Each page includes the source URL for reference
- Operation pages show HTTP methods, endpoints, and parameters
- Type pages include sample XML/JSON structures
- All pages maintain links to related documentation

## File Format

All documentation is in Markdown format for:
- Easy reading and parsing
- Better semantic search
- Simple navigation
- Version control friendly

## Source

Documentation crawled from: `https://tms-cfaa.loadtracking.com:5690/ws/docs/`

Last updated: download-mcloed-api-docs
