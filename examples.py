#!/usr/bin/env python3
"""
Example usage patterns for the TMS Client.

These examples show common use cases and patterns that AI tools
can learn from to provide better suggestions.
"""

from tms_client import TMSClient, RowTypes

def example_basic_usage():
    """Basic API calls with the TMS client."""
    with TMSClient("username", "password") as client:
        # Get location template
        location_template = client.get_json("/locations/new")
        
        # Get all locations
        locations = client.get_json("/locations")
        
        # Get locations with filtering
        active_locations = client.get_json("/locations", params={"active": True})
        
        # Get specific location
        location = client.get_json("/locations/123")


def example_company_switching():
    """Working with different company databases (TMS vs TMS2)."""
    with TMSClient("username", "password") as client:
        # Default company (TMS)
        tms_orders = client.get_json("/orders")
        
        # Switch to TMS2 for specific call
        tms2_orders = client.get_json("/orders", company_id="TMS2")
        
        # Create order in TMS2
        order_data = {
            "customer": "ACME Corp",
            "origin": "Dallas, TX",
            "destination": "Houston, TX"
        }
        new_order = client.post_json("/orders", data=order_data, company_id="TMS2")


def example_creating_records():
    """Creating new records via POST requests."""
    with TMSClient("username", "password") as client:
        # Create a new location
        location_data = {
            "name": "ACME Warehouse",
            "address": "123 Industrial Blvd",
            "city": "Dallas",
            "state": "TX",
            "zip": "75201",
            "contact_name": "John Smith",
            "phone": "214-555-0123"
        }
        new_location = client.post_json("/locations", data=location_data)
        
        # Create a new customer
        customer_data = {
            "name": "ACME Corporation",
            "billing_address": "456 Business Way",
            "city": "Fort Worth",
            "state": "TX"
        }
        new_customer = client.post_json("/customers", data=customer_data)


def example_error_handling():
    """Proper error handling patterns."""
    with TMSClient("username", "password") as client:
        try:
            # This might fail
            orders = client.get_json("/orders/invalid-id")
        except Exception as e:
            print(f"API call failed: {e}")
            # Handle the error appropriately
            orders = []
        
        # Check response before processing
        response = client.get("/locations/123")
        if response.status_code == 200:
            location = response.json()
        elif response.status_code == 404:
            print("Location not found")
        else:
            print(f"Unexpected status: {response.status_code}")


def example_advanced_requests():
    """Advanced request patterns with custom parameters."""
    with TMSClient("username", "password") as client:
        # Request with timeout
        orders = client.get_json("/orders", timeout=30)
        
        # Request with custom headers
        data = client.get_json("/reports", headers={"Accept": "application/xml"})
        
        # Complex query parameters
        filtered_orders = client.get_json("/orders", params={
            "status": "active",
            "date_range": "2024-01-01,2024-12-31",
            "customer_id": 12345,
            "limit": 100
        })
        
        # Raw response access for non-JSON endpoints
        response = client.get("/reports/pdf/123")
        if response.status_code == 200:
            with open("report.pdf", "wb") as f:
                f.write(response.content)


def example_batch_operations():
    """Working with multiple records efficiently."""
    with TMSClient("username", "password") as client:
        # Get multiple orders by ID
        order_ids = [123, 456, 789]
        orders = []
        
        for order_id in order_ids:
            try:
                order = client.get_json(f"/orders/{order_id}")
                orders.append(order)
            except Exception as e:
                print(f"Failed to get order {order_id}: {e}")
        
        # Bulk update example
        updates = [
            {"id": 123, "status": "completed"},
            {"id": 456, "status": "in_transit"},
            {"id": 789, "status": "delivered"}
        ]
        
        for update in updates:
            try:
                result = client.post_json(f"/orders/{update['id']}/status", 
                                        data={"status": update["status"]})
                print(f"Updated order {update['id']}")
            except Exception as e:
                print(f"Failed to update order {update['id']}: {e}")


def example_shipment_workflow():
    """Complete shipment creation workflow."""
    with TMSClient("username", "password") as client:
        # 1. Create shipment
        shipment_data = {
            "customer_id": 12345,
            "origin": {
                "name": "Dallas Warehouse",
                "address": "123 Industrial Way",
                "city": "Dallas",
                "state": "TX"
            },
            "destination": {
                "name": "Houston Distribution",
                "address": "456 Commerce St",
                "city": "Houston", 
                "state": "TX"
            },
            "pickup_date": "2024-01-15",
            "delivery_date": "2024-01-16"
        }
        
        shipment = client.post_json("/shipments", data=shipment_data)
        shipment_id = shipment["id"]
        
        # 2. Add items to shipment
        items = [
            {"description": "Pallets", "quantity": 10, "weight": 5000},
            {"description": "Boxes", "quantity": 50, "weight": 2500}
        ]
        
        for item in items:
            client.post_json(f"/shipments/{shipment_id}/items", data=item)
        
        # 3. Assign driver
        driver_assignment = {
            "driver_id": 789,
            "truck_id": 456,
            "trailer_id": 123
        }
        client.post_json(f"/shipments/{shipment_id}/assign", data=driver_assignment)
        
        # 4. Update status
        client.post_json(f"/shipments/{shipment_id}/status", 
                        data={"status": "dispatched"})


def example_working_with_images():
    """Working with images using row type constants."""
    with TMSClient("username", "password") as client:
        # Get available images using the convenience method
        order_images = client.get_available_images(RowTypes.ORDER, "12345")
        location_images = client.get_available_images(RowTypes.LOCATION, "67890")
        driver_images = client.get_available_images(RowTypes.DRIVER, "ABC123")
        
        # Switch companies
        tms2_order_images = client.get_available_images(RowTypes.ORDER, "12345", company_id="TMS2")
        
        # Generic approach (still works)
        trailer_images = client.get_json(f"/images/{RowTypes.TRAILER}/TRL456")


if __name__ == "__main__":
    print("TMS Client Examples")
    print("==================")
    print("This file contains example usage patterns.")
    print("Import the functions you need or run them directly.")
    print()
    print("Available examples:")
    print("- example_basic_usage()")
    print("- example_company_switching()")
    print("- example_creating_records()")
    print("- example_error_handling()")
    print("- example_advanced_requests()")
    print("- example_batch_operations()")
    print("- example_shipment_workflow()")
    print("- example_working_with_images()")
