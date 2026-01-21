# McLeod API Documentation - PartialShipmentService

**Source URL:** https://tms-cfaa.loadtracking.com:5690/ws/docs/services?role=-1&service=PartialShipmentService

---

go back [ Home](https://tms-cfaa.loadtracking.com:5690/ws/docs/home?role=-1)  
  
# PartialShipmentService

This service provides operations that allow manifesting actions to be performed on orders and movements.

## Operations

name | role | description  
---|---|---  
[POST /partialShipment/manifestMovements/{movementIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&operation=manifestMovements&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Takes a comma delimited list of movement id values and consolidates all stops into a single manifest movement.  
[POST /partialShipment/manifestOptimizationOrders/{orderIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&operation=manifestOptimizationOrders&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Takes a comma delimited list of order id values and consolidates all stops into a single manifest movement for FMS optimized orders. All provided order records and associated movements must be unconsolidated and in available status.  
[POST /partialShipment/manifestOrders/{orderIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&operation=manifestOrders&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Takes a list of order id values and consolidates all stops into a single manifest movement. All provided order records and associated movements must be unconsolidated and in available status.  
[POST /partialShipment/{movementId}/addMovementsToManifest/{movementIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&operation=addMovementsToManifest&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Takes a movement id and a comma delimited list of movement id values to add to an existing manifest movement.  
[POST /partialShipment/{movementId}/addOrdersToManifest/{orderIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&operation=addOrdersToManifest&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Takes a movement id and a comma delimited list of order id values to add to an existing manifest movement.  
[POST /partialShipment/{movementId}/dropFromManifest/{orderIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&operation=dropFromManifest&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Takes a movement id and a comma delimited list of order id values to drop from existing manifest.  
[POST /partialShipment/{movementId}/resequenceManifestStops/{stopIds}](https://tms-cfaa.loadtracking.com:5690/ws/docs/services?service=PartialShipmentService&operation=resequenceManifestStops&role=-1) |  [Users](https://tms-cfaa.loadtracking.com:5690/ws/docs/roles?role=-1) | Takes a movement id and a comma delimited list of stop id values and sequences the stops on the manifest movement.
