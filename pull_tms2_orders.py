#!/usr/bin/env python3
"""
Pull sample orders from TMS2 and save them to the samples directory.
"""

import json
from datetime import datetime
from pathlib import Path
from tms_client import TMSClient

def pull_tms2_orders(num_orders=5):
    """Pull sample orders from TMS2."""
    samples_dir = Path("samples")
    samples_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with TMSClient() as client:
        print(f"Fetching orders from TMS2...")
        
        # Try to get orders list directly from /orders endpoint
        try:
            orders_list = client.get_json("/orders", company_id="TMS2", params={"recordLength": num_orders})
            if isinstance(orders_list, list):
                order_ids = [o.get('id') for o in orders_list if o.get('id')]
            else:
                # If it's not a list, try to extract order IDs from the response
                order_ids = []
                print("Unexpected response format from /orders endpoint")
        except Exception as e:
            print(f"Could not fetch orders list: {e}")
            print("Trying to fetch specific order IDs from TMS2 (starting with 30)...")
            # TMS2 orders start with 30
            order_ids = []
            # Try a smaller range first, starting from higher numbers (more recent)
            start_id = 3050000
            end_id = 3000000
            step = -10  # Skip by 10 to go faster
            
            print(f"    Scanning TMS2 order IDs from {start_id} down to {end_id} (step: {abs(step)})...")
            for test_id in range(start_id, end_id, step):
                if len(order_ids) >= num_orders:
                    break
                try:
                    test_order = client.get_load_json(str(test_id), company_id="TMS2")
                    if test_order and test_order.get('id'):
                        order_ids.append(str(test_id))
                        print(f"    [OK] Found order {test_id}")
                except:
                    continue
            
            # If we didn't find enough, try a different range
            if len(order_ids) < num_orders:
                print(f"    Only found {len(order_ids)} orders, trying range 3000100-3001000...")
                for test_id in range(3001000, 3000100, -10):
                    if len(order_ids) >= num_orders:
                        break
                    try:
                        test_order = client.get_load_json(str(test_id), company_id="TMS2")
                        if test_order and test_order.get('id'):
                            order_ids.append(str(test_id))
                            print(f"    [OK] Found order {test_id}")
                    except:
                        continue
        
        if not order_ids:
            print("No orders found in TMS2")
            return
        
        print(f"Found {len(order_ids)} order IDs, fetching full details...")
        
        for i, order_id in enumerate(order_ids[:num_orders], 1):
            try:
                print(f"  [{i}/{min(len(order_ids), num_orders)}] Fetching order {order_id}...")
                full_order = client.get_load_json(order_id, company_id="TMS2")
                
                # Save as direct order JSON
                filename = samples_dir / f"order_{order_id}_direct_tms2.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(full_order, f, indent=2, ensure_ascii=False)
                
                print(f"    [OK] Saved to {filename}")
                
            except Exception as e:
                print(f"    [FAIL] Failed to fetch order {order_id}: {e}")
        
        print(f"\nCompleted! Saved {min(len(order_ids), num_orders)} orders to samples/")

if __name__ == "__main__":
    pull_tms2_orders(num_orders=5)

