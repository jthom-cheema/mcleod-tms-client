#!/usr/bin/env python3
"""
Example usage patterns for the TMS Client.

These examples show common use cases and patterns that AI tools
can learn from to provide better suggestions.
"""

from tms_client import TMSClient, RowTypes

def example_basic_usage():
    """Basic API calls with the TMS client."""
    # Option 1: Username/password authentication
    with TMSClient("username", "password") as client:
        # Get location template
        location_template = client.get_json("/locations/new")
        
        # Get all locations
        locations = client.get_json("/locations")
        
        # Get locations with filtering
        active_locations = client.get_json("/locations", params={"active": True})
        
        # Get specific location
        location = client.get_json("/locations/123")
    
    # Option 2: API key authentication
    with TMSClient(api_key="your-api-key") as client:
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
    # Can use either username/password or API key
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
    # Works with both authentication methods
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


def example_customer_search():
    """Searching for customers by name or ID."""
    # Username/password or API key both work
    with TMSClient("username", "password") as client:
        # Search by company name
        acme_customers = client.search_customers("ACME")
        print(f"Found {len(acme_customers)} ACME customers")
        
        # Search by partial name
        corp_customers = client.search_customers("Corp")
        print(f"Found {len(corp_customers)} customers with 'Corp' in name")
        
        # Search by customer ID
        specific_customer = client.search_customers("12345")
        if specific_customer:
            customer = specific_customer[0]
            print(f"Customer: {customer.get('name')} - {customer.get('city')}, {customer.get('state')}")
        
        # Get all customers (empty query)
        all_customers = client.search_customers("")
        print(f"Total customers: {len(all_customers)}")
        
        # Search in different company
        tms2_customers = client.search_customers("ACME", company_id="TMS2")
        print(f"Found {len(tms2_customers)} ACME customers in TMS2")
        
        # Process customer data
        for customer in acme_customers[:5]:  # Show first 5
            print(f"  {customer.get('id')}: {customer.get('name')}")
            print(f"    Address: {customer.get('address', 'N/A')}")
            print(f"    City: {customer.get('city', 'N/A')}, {customer.get('state', 'N/A')}")
            print(f"    Phone: {customer.get('phone', 'N/A')}")
            print()


def example_error_handling():
    """Proper error handling patterns."""
    # Works with any authentication method
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
    # All authentication methods supported
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
    # Username/password or API key authentication
    with TMSClient("username", "password") as client:
        # Get multiple orders by ID
        order_ids = [123, 456, 789]
        orders = []
        
        for order_id in order_ids:
            try:
                order = client.get_load_json(order_id)
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
    # Supports both authentication methods
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
    # Works with username/password or API key
    with TMSClient("username", "password") as client:
        # Get available images using the convenience method
        order_images = client.get_available_images(RowTypes.ORDER, "12345")
        location_images = client.get_available_images(RowTypes.LOCATION, "67890")
        driver_images = client.get_available_images(RowTypes.DRIVER, "ABC123")
        
        # Switch companies
        tms2_order_images = client.get_available_images(RowTypes.ORDER, "12345", company_id="TMS2")
        
        # Generic approach (still works)
        trailer_images = client.get_json(f"/images/{RowTypes.TRAILER}/TRL456")
        
        # Get enriched images with clean document type names
        enriched_images = client.get_enriched_images(RowTypes.ORDER, "5000003")
        for image in enriched_images:
            print(f"📄 {image['documentTypeName']} - {image['imageCount']} files")
            print(f"   ID: {image['id']}")
            print(f"   Full Description: {image['documentTypeFullDescription']}")


def example_uploading_images():
    """Uploading images to TMS object history."""
    # All authentication methods supported
    with TMSClient("username", "password") as client:
        order_id = "12345"
        
        # First, get available document types for the order
        doctypes = client.get_available_doctypes(RowTypes.ORDER, order_id)
        print(f"Available document types: {len(doctypes)}")
        for doctype in doctypes:
            print(f"  ID: {doctype['id']} - {doctype['description']}")
        
        # Upload from file path
        try:
            batch_id = client.upload_image_to_history(
                row_type=RowTypes.ORDER,
                row_id=order_id,
                document_type_id="7",  # Freight Bill/Invoice
                image_file="/path/to/invoice.pdf"
            )
            print(f"Upload successful! Batch ID: {batch_id}")
        except Exception as e:
            print(f"Upload failed: {e}")
        
        # Upload from file object
        try:
            with open("receipt.jpg", "rb") as f:
                batch_id = client.upload_image_to_history(
                    row_type=RowTypes.ORDER,
                    row_id=order_id,
                    document_type_id="5",  # Fuel Receipt
                    image_file=f
                )
                print(f"File object upload successful! Batch ID: {batch_id}")
        except Exception as e:
            print(f"File object upload failed: {e}")
        
        # Upload binary data directly
        try:
            with open("proof_of_delivery.pdf", "rb") as f:
                pdf_data = f.read()
            
            batch_id = client.upload_image_to_history(
                row_type=RowTypes.ORDER,
                row_id=order_id,
                document_type_id="1",  # Proof of Delivery-Signed
                image_file=pdf_data
            )
            print(f"Binary data upload successful! Batch ID: {batch_id}")
        except Exception as e:
            print(f"Binary data upload failed: {e}")
        
        # Upload with movement ID (if order has movements)
        try:
            # First get order details to find movement ID
            order = client.get_load_json(order_id)
            movement_id = order.get("curr_movement_id")
            
            if movement_id:
                batch_id = client.upload_image_to_history(
                    row_type=RowTypes.ORDER,
                    row_id=order_id,
                    document_type_id="12",  # Other/Misc Receipts
                    image_file="misc_document.pdf",
                    movement_id=str(movement_id)
                )
                print(f"Upload with movement ID successful! Batch ID: {batch_id}")
            else:
                print("No current movement ID found for this order")
        except Exception as e:
            print(f"Movement-based upload failed: {e}")
        
        # Upload to different record types
        examples = [
            (RowTypes.LOCATION, "LOC123", "location_photo.jpg"),
            (RowTypes.DRIVER, "DRV456", "license_scan.pdf"),
            (RowTypes.TRACTOR, "TRC789", "inspection_report.pdf")
        ]
        
        for row_type, row_id, filename in examples:
            try:
                # Get document types for this record type
                doctypes = client.get_available_doctypes(row_type, row_id)
                if doctypes:
                    first_doctype = doctypes[0]['id']
                    batch_id = client.upload_image_to_history(
                        row_type=row_type,
                        row_id=row_id,
                        document_type_id=first_doctype,
                        image_file=filename
                    )
                    print(f"{row_type} upload successful! Batch ID: {batch_id}")
            except Exception as e:
                print(f"{row_type} upload failed: {e}")


def example_working_with_doctypes():
    """Discovering and working with document types dynamically."""
    # Username/password or API key authentication
    with TMSClient("username", "password") as client:
        # Get available document types for specific order (cached automatically)
        order_doctypes = client.get_available_doctypes(RowTypes.ORDER, "12345")
        print(f"Available ORDER doctypes: {len(order_doctypes)} types")
        
        # Get doctypes for different company
        tms2_doctypes = client.get_available_doctypes(RowTypes.ORDER, "12345", company_id="TMS2")
        
        # Get doctypes with movement association
        movement_doctypes = client.get_available_doctypes(RowTypes.ORDER, "12345", movement_id="MOV789")
        
        # Force fresh fetch (bypass cache)
        fresh_doctypes = client.get_available_doctypes(RowTypes.ORDER, "12345", use_cache=False)
        
        # Get doctypes for other record types
        location_doctypes = client.get_available_doctypes(RowTypes.LOCATION, "67890")
        driver_doctypes = client.get_available_doctypes(RowTypes.DRIVER, "DRV123")
        
        # Use doctypes in your business logic
        for doctype in order_doctypes:
            if doctype.get('name') == 'BOL':  # Bill of Lading
                print(f"Found BOL doctype: {doctype['id']}")
                # Use this doctype ID for document operations


def example_charge_codes_and_billing():
    """Working with charge codes and adding charges to orders."""
    # Supports both authentication methods
    with TMSClient("username", "password") as client:
        order_id = "12345"
        
        # Get all available charge codes (cached for 24 hours by default)
        charge_codes = client.get_available_charge_codes()
        print(f"Available charge codes: {len(charge_codes)}")
        
        # Display some common charge codes
        common_codes = ['LUM', 'DTU', 'FSC', 'LAY', 'HAZ']
        for code in charge_codes:
            if code.get('id') in common_codes:
                print(f"  {code['id']}: {code.get('description', 'No description')}")
        
        # Force fresh data from API
        fresh_codes = client.get_available_charge_codes(use_cache=False)
        
        # Get charge codes for different company
        tms2_codes = client.get_available_charge_codes(company_id="TMS2")
        
        # Refresh cache manually
        success = client.refresh_charge_codes_cache()
        print(f"Cache refresh successful: {success}")
        
        # Add various types of charges to an order
        try:
            # Basic lumper charge
            success = client.add_charge(order_id, "LUM", "LUMPER", 75.00)
            print(f"Added lumper charge: {success}")
            
            # Detention charge with units
            success = client.add_charge(order_id, "DTU", "DETENTION", 50.00, units=2.0)
            print(f"Added detention charge: {success}")
            
            # Fuel surcharge with percentage calculation
            success = client.add_charge(order_id, "FSC", "FUEL SURCHARGE", 10.00, calc_method="P")
            print(f"Added fuel surcharge: {success}")
            
            # Layover charge
            success = client.add_charge(order_id, "LAY", "LAYOVER", 125.00)
            print(f"Added layover charge: {success}")
            
        except Exception as e:
            print(f"Failed to add charge: {e}")
        
        # Add charge with validation (will fail for invalid charge codes)
        try:
            # This will fail with helpful error message
            client.add_charge(order_id, "INVALID", "Bad Code", 100.00)
        except Exception as e:
            print(f"Expected error for invalid code: {e}")
        
        # Add charges to different company
        try:
            success = client.add_charge(order_id, "LUM", "LUMPER", 80.00, company_id="TMS2")
            print(f"Added charge to TMS2: {success}")
        except Exception as e:
            print(f"TMS2 charge failed: {e}")


def example_order_management():
    """Complete order management workflow with charges."""
    # Works with username/password or API key
    with TMSClient("username", "password") as client:
        order_id = "12345"
        
        # Get order details
        order = client.get_json(f"/orders/{order_id}")
        print(f"Order {order_id}: {order.get('customer_name', 'Unknown customer')}")
        
        # Show existing charges
        existing_charges = order.get('otherCharges', [])
        print(f"Existing charges: {len(existing_charges)}")
        for charge in existing_charges:
            charge_id = charge.get('charge_id', 'N/A')
            description = charge.get('descr', 'No description')
            amount = charge.get('amount', 0)
            print(f"  {charge_id}: {description} - ${amount}")
        
        # Add new charges based on business logic
        order_total = order.get('total_amount', 0)
        
        # Add fuel surcharge if order total is over $1000
        if order_total > 1000:
            try:
                client.add_charge(order_id, "FSC", "FUEL SURCHARGE", order_total * 0.05, calc_method="P")
                print("Added fuel surcharge (5%)")
            except Exception as e:
                print(f"Failed to add fuel surcharge: {e}")
        
        # Add detention if delivery is on weekend
        from datetime import datetime
        delivery_date = order.get('delivery_date')
        if delivery_date:
            delivery_dt = datetime.fromisoformat(delivery_date)
            if delivery_dt.weekday() >= 5:  # Saturday or Sunday
                try:
                    client.add_charge(order_id, "DTU", "WEEKEND DETENTION", 100.00)
                    print("Added weekend detention charge")
                except Exception as e:
                    print(f"Failed to add detention: {e}")
        
        # Get updated order to see new charges
        updated_order = client.get_load_json(order_id)
        new_charges = updated_order.get('otherCharges', [])
        print(f"Updated charges: {len(new_charges)}")
        
        # Calculate total charge amount
        total_charges = sum(charge.get('amount', 0) for charge in new_charges)
        print(f"Total additional charges: ${total_charges}")


def example_bulk_charge_operations():
    """Bulk operations for charges across multiple orders."""
    # All authentication methods supported
    with TMSClient("username", "password") as client:
        # Process multiple orders for fuel surcharge
        order_ids = ["12345", "12346", "12347"]
        fuel_surcharge_rate = 0.03  # 3%
        
        # Get charge codes once (cached)
        charge_codes = client.get_available_charge_codes()
        valid_codes = [code.get('id') for code in charge_codes]
        
        # Verify FSC code exists before processing orders
        if "FSC" not in valid_codes:
            print("Error: FSC charge code not available")
            return
        
        successful_updates = 0
        failed_updates = 0
        
        for order_id in order_ids:
            try:
                # Get order details for calculation
                order = client.get_load_json(order_id)
                order_total = order.get('total_amount', 0)
                
                if order_total > 0:
                    surcharge_amount = order_total * fuel_surcharge_rate
                    success = client.add_charge(
                        order_id, 
                        "FSC", 
                        f"FUEL SURCHARGE ({fuel_surcharge_rate*100}%)",
                        surcharge_amount,
                        calc_method="P"
                    )
                    
                    if success:
                        successful_updates += 1
                        print(f"✅ Order {order_id}: Added ${surcharge_amount:.2f} fuel surcharge")
                    else:
                        failed_updates += 1
                        print(f"❌ Order {order_id}: Failed to add charge")
                else:
                    print(f"⚠️  Order {order_id}: No order total, skipping")
                    
            except Exception as e:
                failed_updates += 1
                print(f"❌ Order {order_id}: Error - {e}")
        
        print(f"\nBulk operation complete:")
        print(f"  Successful: {successful_updates}")
        print(f"  Failed: {failed_updates}")
        print(f"  Total processed: {len(order_ids)}")


def example_search_movements():
    """Search movements with flexible filters and change tracking."""
    from datetime import datetime, timedelta
    
    # Username/password or API key authentication
    with TMSClient("username", "password") as client:
        # Basic movement search with multiple filters
        print("=== Basic Movement Search ===")
        movements = client.search_movements({
            "destination.state": "AL",
            "movement.status": "P"
        })
        print(f"Found {len(movements)} in-progress movements to Alabama")
        
        # Search by origin location with wildcards
        print("\n=== Origin Location Search ===")
        warehouse_movements = client.search_movements({
            "origin.location_id": "WARE*",
            "destination.stop_type": "SO"
        })
        print(f"Found {len(warehouse_movements)} movements from WARE* locations")
        
        # Search with change tracking using string date
        print("\n=== Change Tracking (String) ===")
        recent = client.search_movements(
            {"movement.status": "P"},
            changed_after_date="20251012000000-0700",
            changed_after_type="Add"
        )
        print(f"Found {len(recent)} movements added since 2025-10-12")
        
        # Search with datetime object (naive defaults to -0700)
        print("\n=== Change Tracking (Datetime) ===")
        yesterday = datetime.now() - timedelta(days=1)
        updated = client.search_movements(
            {"destination.driver_load_unload": "DRP"},
            changed_after_date=yesterday,
            changed_after_type="Update"
        )
        print(f"Found {len(updated)} movements updated since yesterday")
        
        # Search with pagination and sorting
        print("\n=== Pagination and Sorting ===")
        page1 = client.search_movements(
            {"movement.status": "P"},
            order_by="movement.id DESC",
            record_length=50,
            record_offset=0
        )
        print(f"Page 1: {len(page1)} movements")
        
        page2 = client.search_movements(
            {"movement.status": "P"},
            order_by="movement.id DESC",
            record_length=50,
            record_offset=50
        )
        print(f"Page 2: {len(page2)} movements")
        
        # Search by driver
        print("\n=== Driver Search ===")
        driver_movements = client.search_movements({
            "driver.user": "DPR",
            "movement.status": "P"
        })
        print(f"Found {len(driver_movements)} in-progress movements for driver DPR")
        
        # Search by tractor and trailer
        print("\n=== Equipment Search ===")
        equipment = client.search_movements({
            "tractor.trctr": "TRC123",
            "trailer.trlr": "TRL456"
        })
        print(f"Found {len(equipment)} movements with tractor TRC123 and trailer TRL456")
        
        # Complex multi-criteria search
        print("\n=== Complex Search ===")
        complex_search = client.search_movements(
            {
                "destination.state": "TX",
                "destination.stop_type": "SO",
                "destination.driver_load_unload": "DRP",
                "movement.brokerage": "Y"
            },
            changed_after_date=datetime.now() - timedelta(days=7),
            changed_after_type="Add",
            order_by="movement.id DESC",
            record_length=100
        )
        print(f"Found {len(complex_search)} brokered drop movements to Texas in last 7 days")
        
        # Display sample movement details
        if complex_search:
            print("\n=== Sample Movement ===")
            sample = complex_search[0]
            print(f"Movement ID: {sample.get('id')}")
            print(f"Status: {sample.get('status')}")
            print(f"Brokerage: {sample.get('brokerage')}")


def example_movement_change_monitoring():
    """Monitor movement changes for integration/sync workflows."""
    from datetime import datetime, timedelta
    
    # Works with both authentication methods
    with TMSClient("username", "password") as client:
        # Track newly added movements in last hour
        one_hour_ago = datetime.now() - timedelta(hours=1)
        new_movements = client.search_movements(
            {},  # No filters - get all
            changed_after_date=one_hour_ago,
            changed_after_type="Add",
            order_by="movement.id DESC"
        )
        
        print(f"New movements in last hour: {len(new_movements)}")
        for movement in new_movements:
            print(f"  - Movement {movement.get('id')}: {movement.get('status')}")
        
        # Track updated movements for specific status
        updated_in_progress = client.search_movements(
            {"movement.status": "P"},
            changed_after_date=one_hour_ago,
            changed_after_type="Update"
        )
        
        print(f"\nUpdated in-progress movements: {len(updated_in_progress)}")
        
        # Track all changes (both add and update) by omitting changedAfterType
        all_changes = client.search_movements(
            {"destination.state": "CA"},
            changed_after_date=one_hour_ago
            # No changed_after_type means both Add and Update
        )
        
        print(f"\nAll CA movements changed in last hour: {len(all_changes)}")


def example_order_search():
    """Search orders with flexible criteria."""
    from datetime import datetime, timedelta
    
    # Username/password or API key authentication
    with TMSClient("username", "password") as client:
        # Basic order search by status
        print("=== Search Delivered Orders ===")
        delivered = client.search_orders({"orders.status": "D"})
        print(f"Found {len(delivered)} delivered orders")
        
        # Search by multiple criteria
        print("\n=== Multi-Criteria Search ===")
        orders = client.search_orders({
            "orders.status": "P",
            "shipper.state": "CA",
            "consignee.state": "OR"
        })
        print(f"Found {len(orders)} in-progress orders from CA to OR")
        
        # Search with wildcard location
        print("\n=== Wildcard Location Search ===")
        warehouse_orders = client.search_orders({
            "shipper.location_id": "WARE*",
            "orders.status": "D"
        })
        print(f"Found {len(warehouse_orders)} delivered from WARE* locations")
        
        # Search by customer
        print("\n=== Customer Search ===")
        customer_orders = client.search_orders({
            "customer.id": "HOMEATGA",
            "orders.status": "D"
        })
        print(f"Found {len(customer_orders)} delivered orders for HOMEATGA")
        
        # Search with change tracking using string date
        print("\n=== Change Tracking (String) ===")
        recent = client.search_orders(
            {"orders.status": "P"},
            changed_after_date="20251201000000-0700",
            changed_after_type="Add"
        )
        print(f"Found {len(recent)} orders added since 2025-12-01")
        
        # Search with datetime object
        print("\n=== Change Tracking (Datetime) ===")
        yesterday = datetime.now() - timedelta(days=1)
        updated = client.search_orders(
            {"orders.status": "P"},
            changed_after_date=yesterday,
            changed_after_type="Update"
        )
        print(f"Found {len(updated)} orders updated since yesterday")
        
        # Search with pagination and sorting
        print("\n=== Pagination and Sorting ===")
        page1 = client.search_orders(
            {"orders.status": "P"},
            order_by="orders.id+DESC",
            record_length=50,
            record_offset=0
        )
        print(f"Page 1: {len(page1)} orders")
        
        page2 = client.search_orders(
            {"orders.status": "P"},
            order_by="orders.id+DESC",
            record_length=50,
            record_offset=50
        )
        print(f"Page 2: {len(page2)} orders")
        
        # Search by pickup date range
        print("\n=== Sort by Pickup Date ===")
        by_pickup = client.search_orders(
            {"orders.status": "P"},
            order_by="shipper.sched_arrive_early+ASC"
        )
        print(f"Found {len(by_pickup)} in-progress orders sorted by pickup date")
        
        # Complex multi-field search
        print("\n=== Complex Search ===")
        complex_search = client.search_orders(
            {
                "shipper.state": "CA",
                "consignee.state": "TX",
                "orders.status": "P",
                "orders.equipment_type_id": "V"
            },
            changed_after_date=datetime.now() - timedelta(days=7),
            changed_after_type="Add",
            order_by="orders.id+DESC",
            record_length=100
        )
        print(f"Found {len(complex_search)} van loads CA->TX added in last 7 days")
        
        # Display sample order details
        if complex_search:
            print("\n=== Sample Order ===")
            sample = complex_search[0]
            print(f"Order ID: {sample.get('id')}")
            print(f"Status: {sample.get('status')} - {sample.get('__statusDescr')}")
            print(f"Customer: {sample.get('customer', {}).get('name', 'N/A')}")
            print(f"Equipment: {sample.get('__equipmentTypeDescr', 'N/A')}")


def example_carrier_search():
    """Searching for carriers by ID or name."""
    # Supports username/password or API key
    with TMSClient("username", "password") as client:
        # Get carrier by 8-character code (recommended for exact matches)
        carrier = client.get_carrier_by_code("SUNNTRCA")
        if carrier:
            print(f"Found: {carrier.get('name')} (ID: {carrier.get('id')})")
            drs = carrier.get('drsPayee', {})
            print(f"  MC#: {drs.get('icc_number', 'N/A')}")
            print(f"  DOT#: {drs.get('dot_number', 'N/A')}")
            print(f"  Phone: {carrier.get('phone_number', 'N/A')}")
            print(f"  Status: {carrier.get('status', 'N/A')}")
            print(f"  Address: {carrier.get('address1', 'N/A')}")
            print(f"  City: {carrier.get('city', 'N/A')}, {carrier.get('state', 'N/A')} {carrier.get('zip_code', 'N/A')}")
        
        # Get carrier from different company
        tms2_carrier = client.get_carrier_by_code("SUNNTRCA", company_id="TMS2")
        if tms2_carrier:
            print(f"\nTMS2 Carrier: {tms2_carrier.get('name')}")
        
        # Search by carrier ID (returns list, useful for partial matches)
        carriers = client.search_carriers("CONSVAWA")
        if carriers:
            carrier = carriers[0]
            print(f"\nFound: {carrier.get('name')} (ID: {carrier.get('id')})")
            print(f"  MC#: {carrier.get('mc_number', 'N/A')}")
            print(f"  DOT#: {carrier.get('dot_number', 'N/A')}")
            print(f"  Phone: {carrier.get('phone', 'N/A')}")
            print(f"  Active: {carrier.get('is_active', False)}")
        
        # Search by carrier name
        swift_carriers = client.search_carriers("Swift")
        print(f"\nFound {len(swift_carriers)} carriers matching 'Swift'")
        for carrier in swift_carriers[:5]:  # Show first 5
            print(f"  - {carrier.get('id')}: {carrier.get('name')}")
        
        # Search in different company
        tms2_carriers = client.search_carriers("CONSVAWA", company_id="TMS2")
        print(f"\nFound {len(tms2_carriers)} carrier(s) in TMS2")
        
        # Get carrier details and display key fields
        carriers = client.search_carriers("CONSVAWA")
        if carriers:
            carrier = carriers[0]
            print(f"\nCarrier details for {carrier.get('id')}:")
            print(f"  Name: {carrier.get('name')}")
            print(f"  Address: {carrier.get('address1')}")
            print(f"  City: {carrier.get('city_name')}, {carrier.get('state')} {carrier.get('zip_code')}")
            print(f"  MC Number: {carrier.get('mc_number')}")
            print(f"  DOT Number: {carrier.get('dot_number')}")


def example_factoring_company_search():
    """Retrieving factoring company information by factor code."""
    # Supports username/password or API key
    with TMSClient("username", "password") as client:
        # Get factoring company by factor code
        factor = client.get_factoring_company("APEXFOTX")
        if factor:
            print(f"Found: {factor.get('name')} (ID: {factor.get('id')})")
            print(f"  Address: {factor.get('address', 'N/A')}")
            print(f"  City: {factor.get('city', 'N/A')}, {factor.get('state', 'N/A')} {factor.get('zip_code', 'N/A')}")
            print(f"  Phone: {factor.get('phone_number', 'N/A')}")
            print(f"  Email: {factor.get('email', 'N/A')}")
            print(f"  Payment Method: {factor.get('payment_method', 'N/A')}")
            
            # Check for nested state_row if present
            if 'state_row' in factor:
                state = factor['state_row']
                print(f"  State Info: {state.get('name', 'N/A')} ({state.get('id', 'N/A')})")
        
        # Get factoring company from different company
        tms2_factor = client.get_factoring_company("APEXFOTX", company_id="TMS2")
        if tms2_factor:
            print(f"\nTMS2 Factor: {tms2_factor.get('name')}")
        
        # Check if factoring company exists
        invalid_factor = client.get_factoring_company("INVALID")
        if not invalid_factor:
            print("\nFactoring company 'INVALID' not found")
        
        # Process multiple factoring companies
        factor_codes = ["APEXFOTX", "FACTOR1", "FACTOR2"]
        for code in factor_codes:
            factor = client.get_factoring_company(code)
            if factor:
                print(f"\n{code}: {factor.get('name')}")
            else:
                print(f"\n{code}: Not found")


def example_user_search():
    """Searching for users by ID, name, or email."""
    # Supports username/password or API key
    with TMSClient("username", "password") as client:
        # Search by exact user ID
        users = client.search_users("cfaa-jthom")
        if users:
            user = users[0]
            print(f"Found: {user['name']} ({user['email_address']})")
            print(f"  ID: {user['id']}")
            print(f"  Department: {user.get('department_id', 'N/A')}")
            print(f"  Active: {user.get('is_active', False)}")
            print(f"  Phone: {user.get('phone', 'N/A')}")
        
        # Search by partial ID (finds all users starting with prefix)
        all_cfaa_users = client.search_users("cfaa")
        print(f"\nFound {len(all_cfaa_users)} users starting with 'cfaa'")
        for user in all_cfaa_users[:10]:  # Show first 10
            print(f"  - {user['id']}: {user['name']}")
        
        # Search by name
        jack_users = client.search_users("Jack")
        print(f"\nFound {len(jack_users)} users with 'Jack' in name:")
        for user in jack_users:
            print(f"  - {user['id']}: {user['name']} ({user.get('email_address', 'No email')})")
        
        # Search by email
        email_users = client.search_users("jthompson@teamcheema.com")
        if email_users:
            user = email_users[0]
            print(f"\nUser found by email: {user['name']} (ID: {user['id']})")
        
        # Search in different company
        tms2_users = client.search_users("cfaa-jthom", company_id="TMS2")
        print(f"\nFound {len(tms2_users)} user(s) in TMS2")
        
        # Check if user exists
        new_user = client.search_users("cfaa-newuser")
        if not new_user:
            print("\nUser 'cfaa-newuser' does not exist")
        
        # Get user details and display all fields
        users = client.search_users("cfaa-jthom")
        if users:
            user = users[0]
            print(f"\nAll fields for {user['name']}:")
            for key, value in sorted(user.items()):
                print(f"  {key}: {value}")
        
        # Find users by department
        logs_users = []
        for user in client.search_users("cfaa"):
            if user.get('department_id') == 'LOGS':
                logs_users.append(user)
        print(f"\nFound {len(logs_users)} users in LOGS department")
        for user in logs_users:
            print(f"  - {user['name']} ({user['id']})")
        
        # Find active vs inactive users
        active_users = [u for u in client.search_users("cfaa") if u.get('is_active')]
        inactive_users = [u for u in client.search_users("cfaa") if not u.get('is_active')]
        print(f"\nActive users: {len(active_users)}")
        print(f"Inactive users: {len(inactive_users)}")


def example_update_load():
    """Update a load with modified JSON."""
    # Works with username/password or API key
    with TMSClient("username", "password") as client:
        order_id = "5225506"
        
        # Get current order JSON
        order = client.get_load_json(order_id)
        print(f"Current reference: {order.get('reference_number')}")
        
        # Modify reference numbers
        order['reference_number'] = "NEW-REF-123"
        order['customer_reference_number'] = "CUST-REF-456"
        
        # Update the order
        updated = client.update_load(order)
        print(f"Updated order {updated['id']}")
        print(f"New reference: {updated.get('reference_number')}")
        
        # Automation example: pull, modify, update
        orders_to_update = ["5225506", "5225507", "5225508"]
        
        for order_id in orders_to_update:
            try:
                # Pull current order
                order = client.get_load_json(order_id)
                
                # Modify specific fields
                old_ref = order.get('reference_number', '')
                new_ref = f"{old_ref}-UPDATED"
                order['reference_number'] = new_ref
                
                # Update the load
                updated = client.update_load(order)
                print(f"✅ Updated order {order_id}: {new_ref}")
                
            except Exception as e:
                print(f"❌ Failed to update order {order_id}: {e}")
        
        # Modify multiple fields at once
        order = client.get_load_json("5225506")
        order['reference_number'] = "REF-001"
        order['customer_reference_number'] = "CUST-001"
        order['purchase_order_number'] = "PO-001"
        order['special_instructions'] = "Updated via automation"
        
        updated = client.update_load(order)
        print(f"Updated multiple fields for order {updated['id']}")


def example_billing_history_search():
    """Search freight billing history by bill_date and other criteria."""
    from datetime import datetime, timedelta
    
    # Username/password or API key authentication
    with TMSClient("username", "password") as client:
        # Single-page enforced pagination (100 max). If API returns more, it is trimmed.
        print("=== Single Page (enforced 100) ===")
        page = client.search_billing_history("t-1", company_id="TMS")
        print(f"Got {len(page)} rows (<=100)")
        
        # Auto-paginate to fetch all results via cursor-based pagination
        print("\n=== Auto-paginate ALL ===")
        all_rows = client.search_billing_history("t-1", company_id="TMS", auto_paginate=True)
        print(f"Got {len(all_rows)} total rows")
        
        # Range query also paginates; single page trimmed to 100, auto gets all
        print("\n=== Range Query (>=t-30) ===")
        range_page = client.search_billing_history(">=t-30", company_id="TMS")
        range_all = client.search_billing_history(">=t-30", company_id="TMS", auto_paginate=True)
        print(f"Range first page: {len(range_page)} rows (<=100)")
        print(f"Range all rows:   {len(range_all)}")
        
        # Basic search: yesterday's bills (relative date format)
        print("=== Yesterday's Bills ===")
        yesterday_bills = client.search_billing_history("t-1")
        print(f"Found {len(yesterday_bills)} bills from yesterday")
        for bill in yesterday_bills[:5]:  # Show first 5
            print(f"  Invoice: {bill.get('invoice_no_string', 'N/A')}")
            print(f"  Bill Date: {bill.get('bill_date', 'N/A')}")
            print(f"  Total: ${bill.get('total_charges_n', 0)}")
        
        # Search last 100 days (relative date format)
        print("\n=== Last 100 Days ===")
        recent_bills = client.search_billing_history("t-100")
        print(f"Found {len(recent_bills)} bills in last 100 days")
        
        # Search with comparison operator (greater than or equal to last 100 days)
        print("\n=== Comparison Operator ===")
        bills_since = client.search_billing_history(">=t-100")
        print(f"Found {len(bills_since)} bills since 100 days ago")
        
        # Search using datetime object
        print("\n=== Datetime Object ===")
        from datetime import datetime
        specific_date = datetime(2023, 4, 1, 0, 0, 0)
        bills_from_date = client.search_billing_history(specific_date)
        print(f"Found {len(bills_from_date)} bills from {specific_date.date()}")
        
        # Search using formatted string date
        print("\n=== Formatted String Date ===")
        bills_string = client.search_billing_history("20230401000000-0700")
        print(f"Found {len(bills_string)} bills from formatted date")
        
        # Include user and customer details
        print("\n=== With User and Customer Details ===")
        detailed_bills = client.search_billing_history(
            "t-1",
            include_users=True,
            include_customer=True
        )
        if detailed_bills:
            bill = detailed_bills[0]
            print(f"Invoice: {bill.get('invoice_no_string')}")
            # Check for user details
            if 'RowUsers' in bill:
                print(f"Users: {bill['RowUsers']}")
            # Check for customer details
            if 'RowCustomer' in bill:
                customer = bill['RowCustomer']
                print(f"Customer: {customer.get('name', 'N/A')}")
        
        # Search with additional filters: summary bills
        print("\n=== Summary Bills Only ===")
        summary_bills = client.search_billing_history(
            ">=t-100",
            is_summary_bill="Y"
        )
        print(f"Found {len(summary_bills)} summary bills in last 100 days")
        
        # Search with BOL pattern matching
        print("\n=== BOL Pattern Search ===")
        bol_bills = client.search_billing_history(
            ">=t-100",
            blnum="12345*"  # Wildcard pattern
        )
        print(f"Found {len(bol_bills)} bills with BOL starting with '12345'")
        
        # Complex search: summary bills with BOL pattern and ship date
        print("\n=== Complex Multi-Criteria Search ===")
        complex_bills = client.search_billing_history(
            ship_date=">=t-100",  # Shipped in last 100 days
            is_summary_bill="Y",   # Summary bills only
            blnum="12345*",        # BOL pattern
            include_users=True,
            include_customer=True
        )
        print(f"Found {len(complex_bills)} bills matching all criteria")
        
        # Process and analyze results
        if complex_bills:
            print("\n=== Analysis ===")
            total_amount = sum(bill.get('total_charges_n', 0) for bill in complex_bills)
            print(f"Total charges: ${total_amount:,.2f}")
            print(f"Average per bill: ${total_amount / len(complex_bills):,.2f}")
            
            # Group by customer
            by_customer = {}
            for bill in complex_bills:
                customer_id = bill.get('customer_id', 'Unknown')
                if customer_id not in by_customer:
                    by_customer[customer_id] = []
                by_customer[customer_id].append(bill)
            
            print(f"\nBills by customer: {len(by_customer)} customers")
            for customer_id, customer_bills in list(by_customer.items())[:5]:
                customer_total = sum(b.get('total_charges_n', 0) for b in customer_bills)
                print(f"  {customer_id}: {len(customer_bills)} bills, ${customer_total:,.2f}")
        
        # Search without date filter (all bills, may be slow)
        print("\n=== All Bills (No Date Filter) ===")
        try:
            all_bills = client.search_billing_history(None)
            print(f"Found {len(all_bills)} total bills")
        except Exception as e:
            print(f"Note: Searching without date filter may not be supported: {e}")
        
        # Search in different company
        print("\n=== Different Company ===")
        tms2_bills = client.search_billing_history(
            "t-1",
            company_id="TMS2"
        )
        print(f"Found {len(tms2_bills)} bills in TMS2 from yesterday")
        
        # Search with specific invoice number
        print("\n=== Specific Invoice ===")
        invoice_bills = client.search_billing_history(
            invoice_no_string="12345"
        )
        print(f"Found {len(invoice_bills)} bills with invoice number 12345")
        
        # Auto-paginate to get all results (API limitation: max 100 per call)
        # The API doesn't support offset pagination, so we use cursor-based pagination
        print("\n=== Auto-Pagination (Get All Results) ===")
        all_yesterday_bills = client.search_billing_history("t-1", auto_paginate=True)
        print(f"Got {len(all_yesterday_bills)} total bills from yesterday")
        print("Note: Without auto_paginate, you'd only get the first 100 results")
        
        # Display sample bill structure
        if yesterday_bills:
            print("\n=== Sample Bill Structure ===")
            sample = yesterday_bills[0]
            print("Available fields:")
            for key in sorted(sample.keys())[:20]:  # Show first 20 fields
                value = sample[key]
                if isinstance(value, (str, int, float, bool, type(None))):
                    print(f"  {key}: {value}")
                else:
                    print(f"  {key}: {type(value).__name__}")


def example_settlement_search():
    """Search settlements with flexible filters."""
    from datetime import datetime, timedelta
    
    # Username/password or API key authentication
    with TMSClient("username", "password") as client:
        # Get settlements on hold (convenience method)
        print("=== Settlements On Hold ===")
        on_hold = client.get_settlements_on_hold()
        print(f"Found {len(on_hold)} settlements on hold")
        for settlement in on_hold[:5]:  # Show first 5
            print(f"  Settlement ID: {settlement.get('id')}")
            print(f"  Payee: {settlement.get('payee_id')}")
            print(f"  Amount: ${settlement.get('amount', 0)}")
        
        # Get settlements on hold with sorting
        print("\n=== Settlements On Hold (Sorted by OK2Pay Date) ===")
        sorted_on_hold = client.get_settlements_on_hold(
            order_by="settlement.ok2pay_date+DESC"
        )
        print(f"Found {len(sorted_on_hold)} settlements")
        
        # Search settlements by ready to pay flag
        print("\n=== Search Settlements On Hold ===")
        settlements = client.search_settlements({"settlement.ready_to_pay_flag": "n"})
        print(f"Found {len(settlements)} settlements on hold")
        
        # Search by payee and ok to pay date
        print("\n=== Settlements for All Payees (Last 7 Days) ===")
        recent_settlements = client.search_settlements({
            "settlement.payee_id": "*",
            "settlement.ok2pay_date": ">=t-7"
        })
        print(f"Found {len(recent_settlements)} settlements")
        
        # Search settlements for loaded movements
        print("\n=== Settlements for Loaded Movements On Hold ===")
        loaded_settlements = client.search_settlements({
            "settlement.ready_to_pay_flag": "n",
            "movement.loaded": "L"
        })
        print(f"Found {len(loaded_settlements)} settlements")
        
        # Search with change tracking (datetime object)
        print("\n=== Recently Added Settlements ===")
        from datetime import timezone
        yesterday = datetime.now(timezone(timedelta(hours=-7))) - timedelta(days=1)
        recent_added = client.search_settlements(
            {"settlement.loaded": "L"},
            changed_after_date=yesterday,
            changed_after_type="Add"
        )
        print(f"Found {len(recent_added)} recently added settlements")
        
        # Search with change tracking (string format)
        print("\n=== Recently Updated Settlements ===")
        updated_settlements = client.search_settlements(
            {"settlement.ready_to_pay_flag": "n"},
            changed_after_date="t-1",
            changed_after_type="Update",
            record_length=100,
            record_offset=0
        )
        print(f"Found {len(updated_settlements)} recently updated settlements")
        
        # Search with custom sorting
        print("\n=== Settlements Sorted by OK2Pay Date ===")
        sorted_settlements = client.search_settlements(
            {"settlement.payee_id": "*"},
            order_by="settlement.ok2pay_date+DESC"
        )
        print(f"Found {len(sorted_settlements)} settlements")
        
        # Search with pagination
        print("\n=== Paginated Settlements ===")
        page = client.search_settlements(
            {"settlement.ready_to_pay_flag": "n"},
            record_length=100,
            record_offset=0
        )
        print(f"Page 1: {len(page)} settlements")
        
        # Search in different company
        print("\n=== Settlements in TMS2 ===")
        tms2_settlements = client.get_settlements_on_hold(company_id="TMS2")
        print(f"Found {len(tms2_settlements)} settlements on hold in TMS2")
        
        # Display sample settlement structure
        if on_hold:
            print("\n=== Sample Settlement Structure ===")
            sample = on_hold[0]
            print("Available fields:")
            for key in sorted(sample.keys())[:20]:  # Show first 20 fields
                value = sample[key]
                if isinstance(value, (str, int, float, bool, type(None))):
                    print(f"  {key}: {value}")
                else:
                    print(f"  {key}: {type(value).__name__}")


def example_update_settlement_status():
    """Update settlement and deduction process status (ready_to_pay_flag).
    
    Uses PUT /settlement/update and PUT /drs_pending_deduct/update endpoints:
    - Y = Process (ready to pay)
    - N = Hold (not ready to pay)
    - V = Void
    """
    # Works with username/password or API key
    with TMSClient("username", "password") as client:
        movement_id = "1195486"
        company = "TMS2"
        
        # Check current status
        print("=== Current Status ===")
        settlements = client.search_settlements(
            {"movement.id": movement_id}, 
            company_id=company
        )
        if settlements:
            print(f"Settlement: ready_to_pay_flag = {settlements[0].get('ready_to_pay_flag')}")
        
        deductions = client.search_deductions(
            {"drs_pending_deduct.movement_id": movement_id},
            company_id=company
        )
        for d in deductions:
            print(f"Deduction {d.get('deduct_code_id')}: ready_to_pay_flag = {d.get('ready_to_pay_flag')}")
        
        # Put settlement AND deductions on hold
        print("\n=== Putting Settlement & Deductions On Hold ===")
        result = client.update_settlement_status(movement_id, "N", company_id=company)
        print(f"Updated {len(result['settlements'])} settlement(s) to Hold (N)")
        print(f"Updated {len(result['deductions'])} deduction(s) to Hold (N)")
        
        # Mark ready to process
        print("\n=== Marking Ready to Process ===")
        result = client.update_settlement_status(movement_id, "Y", company_id=company)
        print(f"Updated {len(result['settlements'])} settlement(s) to Process (Y)")
        print(f"Updated {len(result['deductions'])} deduction(s) to Process (Y)")
        
        # Update a single deduction directly
        print("\n=== Update Single Deduction ===")
        if deductions:
            deduction_id = deductions[0].get('id')
            updated = client.update_deduction_status(deduction_id, "N", company_id=company)
            print(f"Updated deduction {deduction_id}: ready_to_pay_flag = {updated.get('ready_to_pay_flag')}")
        
        # Batch update example
        print("\n=== Batch Update Example ===")
        movement_ids = ["1195486", "1195487", "1195488"]
        for mid in movement_ids:
            try:
                result = client.update_settlement_status(mid, "N", company_id=company)
                print(f"✅ Movement {mid}: {len(result['settlements'])} settlement(s), {len(result['deductions'])} deduction(s)")
            except Exception as e:
                print(f"❌ Movement {mid}: {e}")


def example_update_settlement_ok2pay_date():
    """Update the OK to Pay Date on a settlement.
    
    Uses PUT /settlement/update endpoint to change the ok2pay_date field.
    Accepts flexible date formats: datetime, MM/DD/YYYY, YYYY-MM-DD, or API format.
    """
    from datetime import datetime
    
    with TMSClient("username", "password") as client:
        movement_id = "1195486"
        company = "TMS2"
        
        # First, find the settlement
        print("=== Finding Settlement ===")
        settlements = client.search_settlements(
            {"movement.id": movement_id},
            company_id=company
        )
        
        if not settlements:
            print(f"No settlements found for movement {movement_id}")
            return
        
        settlement = settlements[0]
        settlement_id = settlement.get('id')
        print(f"Settlement ID: {settlement_id}")
        print(f"Current OK2Pay Date: {settlement.get('ok2pay_date')}")
        
        # Update using MM/DD/YYYY format
        print("\n=== Updating OK2Pay Date (MM/DD/YYYY) ===")
        updated = client.update_settlement_ok2pay_date(
            settlement_id,
            "01/15/2026",
            company_id=company
        )
        print(f"Updated OK2Pay Date: {updated.get('ok2pay_date')}")
        
        # Update using datetime object
        print("\n=== Updating OK2Pay Date (datetime) ===")
        new_date = datetime(2026, 1, 20)
        updated = client.update_settlement_ok2pay_date(
            settlement_id,
            new_date,
            company_id=company
        )
        print(f"Updated OK2Pay Date: {updated.get('ok2pay_date')}")
        
        # Update using YYYY-MM-DD format
        print("\n=== Updating OK2Pay Date (YYYY-MM-DD) ===")
        updated = client.update_settlement_ok2pay_date(
            settlement_id,
            "2026-01-25",
            company_id=company
        )
        print(f"Updated OK2Pay Date: {updated.get('ok2pay_date')}")
        
        # Restore original date
        print("\n=== Restoring Original Date ===")
        original_date = settlement.get('ok2pay_date')
        if original_date:
            updated = client.update_settlement_ok2pay_date(
                settlement_id,
                original_date,
                company_id=company
            )
            print(f"Restored OK2Pay Date: {updated.get('ok2pay_date')}")


def example_batch_update_deductions_from_file():
    """Batch update deductions from a file of movement IDs.
    
    Useful when settlements are on hold but deductions need to be synced.
    Reads movement IDs from a file and updates all deductions to match.
    """
    with TMSClient("username", "password") as client:
        company = "TMS2"
        
        # Read movement IDs from file (one per line)
        with open("tests/put_on_hold.txt", "r") as f:
            movement_ids = [line.strip() for line in f if line.strip()]
        
        print(f"Processing {len(movement_ids)} movements...")
        
        total_deductions = 0
        for i, movement_id in enumerate(movement_ids, 1):
            try:
                # Search for deductions
                deductions = client.search_deductions(
                    {"drs_pending_deduct.movement_id": movement_id},
                    company_id=company
                )
                
                if not deductions:
                    continue
                
                # Update each deduction to Hold
                for ded in deductions:
                    if ded.get('ready_to_pay_flag') != 'N':
                        client.update_deduction_status(ded['id'], "N", company_id=company)
                        total_deductions += 1
                
                print(f"[{i}/{len(movement_ids)}] Movement {movement_id}: {len(deductions)} deduction(s)")
                
            except Exception as e:
                print(f"[{i}/{len(movement_ids)}] Movement {movement_id}: ERROR - {e}")
        
        print(f"\nTotal deductions updated: {total_deductions}")


def example_get_comments():
    """Retrieve comments for various record types.
    
    Comments can be retrieved for drivers, settlements, and other record types.
    Each comment includes details about who entered it, when, and the comment type.
    """
    with TMSClient("username", "password") as client:
        # Get driver comments using convenience method
        print("=== Driver Comments ===")
        driver_comments = client.get_driver_comments("BJM01")
        print(f"Found {len(driver_comments)} comment(s) for driver BJM01")
        for comment in driver_comments:
            user = comment.get('enteredByUser', {})
            comment_type = comment.get('commentTypeDescr', {})
            print(f"  {user.get('name', 'Unknown')} ({comment.get('entered_date', 'N/A')})")
            print(f"  Type: {comment_type.get('descr', 'N/A')}")
            print(f"  Comment: {comment.get('comments', 'N/A')}")
            print()
        
        # Get settlement comments using convenience method
        print("=== Settlement Comments ===")
        settlement_id = "zz1ivr5ucal12v8CFAATS3"
        settlement_comments = client.get_settlement_comments(settlement_id, company_id="TMS2")
        print(f"Found {len(settlement_comments)} comment(s) for settlement {settlement_id}")
        for comment in settlement_comments:
            user = comment.get('enteredByUser', {})
            comment_type = comment.get('commentTypeDescr', {})
            print(f"  {user.get('name', 'Unknown')} ({comment.get('entered_date', 'N/A')})")
            print(f"  Type: {comment_type.get('descr', 'N/A')}")
            print(f"  Comment: {comment.get('comments', 'N/A')[:100]}...")  # Truncate long comments
            print()
        
        # Generic method - works for any row type
        print("=== Generic Comment Retrieval ===")
        from tms_client import RowTypes
        comments = client.get_comments(RowTypes.DRIVER, "BJM01")
        print(f"Found {len(comments)} comment(s) using generic method")
        
        # Process comment details
        if comments:
            comment = comments[0]
            print(f"\nComment Details:")
            print(f"  ID: {comment.get('id')}")
            print(f"  Type ID: {comment.get('comment_type_id')}")
            print(f"  Entered Date: {comment.get('entered_date')}")
            print(f"  Entered By: {comment.get('entered_user_id')}")
            if 'enteredByUser' in comment:
                user = comment['enteredByUser']
                print(f"  User Name: {user.get('name')}")
                print(f"  User Email: {user.get('email_address')}")
            if 'commentTypeDescr' in comment:
                ct = comment['commentTypeDescr']
            print(f"  Comment Type: {ct.get('descr')}")
            print(f"  Type Active: {ct.get('is_active')}")


def example_delete_comments():
    """Delete comments for various record types.
    
    Comments can be deleted by their ID. Useful for cleaning up test comments
    or removing incorrect entries.
    """
    with TMSClient("username", "password") as client:
        # Delete a comment by ID
        print("=== Deleting Comment by ID ===")
        comment_id = "zz1je0gung90o24CFAATS2"
        try:
            success = client.delete_comment(comment_id, company_id="TMS2")
            if success:
                print(f"✓ Comment {comment_id} deleted successfully")
            else:
                print(f"⚠ Delete returned False")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        # Get comments first, then delete one
        print("\n=== Find and Delete Specific Comment ===")
        settlement_id = "zz1jbl5m6vq11soCFAATS3"
        comments = client.get_settlement_comments(settlement_id, company_id="TMS2")
        print(f"Found {len(comments)} comment(s)")
        
        # Find and delete a specific comment
        target_text = "test comment"
        target_type = "ACCESSOR"
        for comment in comments:
            if (comment.get('comments', '').strip() == target_text and 
                comment.get('comment_type_id', '').strip().upper() == target_type.upper()):
                print(f"\nFound target comment:")
                print(f"  ID: {comment.get('id')}")
                print(f"  Type: {comment.get('comment_type_id')}")
                print(f"  Text: {comment.get('comments')}")
                
                try:
                    success = client.delete_comment(comment['id'], company_id="TMS2")
                    if success:
                        print(f"✓ Comment deleted successfully")
                    else:
                        print(f"⚠ Delete returned False")
                except Exception as e:
                    print(f"❌ Error deleting: {e}")
                break
        else:
            print(f"⚠ Comment not found: type='{target_type}', text='{target_text}'")
        
        # Verify deletion
        print("\n=== Verifying Deletion ===")
        remaining = client.get_settlement_comments(settlement_id, company_id="TMS2")
        print(f"Remaining comments: {len(remaining)}")
        for i, comment in enumerate(remaining, 1):
            print(f"  {i}. [{comment.get('comment_type_id')}] {comment.get('comments', 'N/A')[:50]}")


def example_create_comments():
    """Create comments for various record types.
    
    Comments can be created for drivers, settlements, and other record types.
    Uses minimal payload - only required fields. API populates other fields automatically.
    """
    with TMSClient("username", "password") as client:
        # Create a settlement comment
        print("=== Creating Settlement Comment ===")
        settlement_id = "zz1j0agbbp50rfkCFAATS2"
        comment = client.create_settlement_comment(
            settlement_id=settlement_id,
            comment_type_id="AP",
            comments="Payment processed successfully",
            company_id="TMS2"
        )
        print(f"✓ Created comment ID: {comment.get('id')}")
        print(f"  Comment Type: {comment.get('comment_type_id')}")
        print(f"  Comment Text: {comment.get('comments')}")
        print(f"  Entered By: {comment.get('enteredByUser', {}).get('name', 'N/A')}")
        print(f"  Entered Date: {comment.get('entered_date', 'N/A')}")
        
        # Create a driver comment
        print("\n=== Creating Driver Comment ===")
        try:
            driver_comment = client.create_driver_comment(
                driver_id="BJM01",
                comment_type_id="GEN",
                comments="Driver called in sick"
            )
            print(f"✓ Created comment ID: {driver_comment.get('id')}")
            print(f"  Comment Text: {driver_comment.get('comments')}")
        except Exception as e:
            print(f"⚠ Could not create driver comment (driver may not exist): {e}")
        
        # Generic method - works for any row type
        print("\n=== Using Generic create_comment() Method ===")
        from tms_client import RowTypes
        comment = client.create_comment(
            parent_row_type=RowTypes.SETTLEMENT,
            parent_row_id=settlement_id,
            comment_type_id="AP",
            comments="Generic method test comment",
            company_id="TMS2"
        )
        print(f"✓ Created comment ID: {comment.get('id')}")
        
        # Verify by retrieving comments
        print("\n=== Verifying Created Comments ===")
        all_comments = client.get_settlement_comments(settlement_id, company_id="TMS2")
        print(f"✓ Found {len(all_comments)} total comment(s) for settlement {settlement_id}")
        for i, c in enumerate(all_comments[-3:], 1):  # Show last 3 comments
            print(f"\n  Comment {i}:")
            print(f"    ID: {c.get('id')}")
            print(f"    Type: {c.get('comment_type_id')}")
            print(f"    Text: {c.get('comments', 'N/A')[:50]}...")
            print(f"    Entered By: {c.get('enteredByUser', {}).get('name', 'N/A')}")


def example_authentication_methods():
    """Different ways to authenticate with the TMS client."""
    # Method 1: Username and password (positional)
    with TMSClient("username", "password") as client:
        orders = client.get_json("/orders")
    
    # Method 2: Username and password (keyword)
    with TMSClient(username="username", password="password") as client:
        orders = client.get_json("/orders")
    
    # Method 3: API key (default Bearer token)
    with TMSClient(api_key="your-api-key") as client:
        orders = client.get_json("/orders")
    
    # Method 4: API key with custom header format
    with TMSClient(api_key="your-api-key", api_key_header="ApiKey") as client:
        orders = client.get_json("/orders")
    
    # Method 5: API key with X-API-Key header
    with TMSClient(api_key="your-api-key", api_key_header="X-API-Key") as client:
        orders = client.get_json("/orders")
    
    # Method 6: Using environment variables
    # Set TMS_USERNAME, TMS_PASSWORD, or TMS_API_KEY in .env file
    # Then just call:
    # with TMSClient() as client:
    #     orders = client.get_json("/orders")


if __name__ == "__main__":
    print("TMS Client Examples")
    print("==================")
    print("This file contains example usage patterns.")
    print("Import the functions you need or run them directly.")
    print()
    print("Authentication Methods:")
    print("- Username/password (positional or keyword)")
    print("- API key (Bearer, ApiKey, or X-API-Key header)")
    print("- Environment variables (TMS_USERNAME/TMS_PASSWORD or TMS_API_KEY)")
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
    print("- example_uploading_images()")
    print("- example_working_with_doctypes()")
    print("- example_charge_codes_and_billing()")
    print("- example_order_management()")
    print("- example_bulk_charge_operations()")
    print("- example_order_search()")
    print("- example_search_movements()")
    print("- example_movement_change_monitoring()")
    print("- example_customer_search()")
    print("- example_carrier_search()")
    print("- example_factoring_company_search()")
    print("- example_user_search()")
    print("- example_update_load()")
    print("- example_billing_history_search()")
    print("- example_settlement_search()")
    print("- example_authentication_methods()")
