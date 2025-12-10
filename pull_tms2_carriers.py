#!/usr/bin/env python3
"""
Pull sample carrier profiles from TMS2 and save them to the samples directory.
"""

import json
from datetime import datetime
from pathlib import Path
from tms_client import TMSClient

def pull_tms2_carriers(num_carriers=5):
    """Pull sample carriers from TMS2."""
    samples_dir = Path("samples")
    carriers_dir = samples_dir / "carriers"
    carriers_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with TMSClient() as client:
        print(f"Searching for carriers in TMS2...")
        
        # Try some common carrier code patterns
        # Carrier codes are typically 8 characters, uppercase
        test_codes = [
            "SUNNTRCA",  # From the API docs example
            "CONSVAWA",  # Common example
        ]
        
        # Also try searching for common carrier names to find more
        found_carriers = []
        
        # Try the specific codes first
        for code in test_codes:
            try:
                carrier = client.get_carrier_by_code(code, company_id="TMS2")
                if carrier:
                    found_carriers.append(carrier)
                    print(f"    [OK] Found carrier {code}")
            except Exception as e:
                print(f"    [SKIP] Carrier {code}: {e}")
        
        # If we need more, try searching by common names
        if len(found_carriers) < num_carriers:
            search_terms = ["Swift", "Schneider", "Werner", "JB Hunt", "Knight"]
            for term in search_terms:
                if len(found_carriers) >= num_carriers:
                    break
                try:
                    carriers = client.search_carriers(term, company_id="TMS2")
                    for carrier in carriers:
                        if len(found_carriers) >= num_carriers:
                            break
                        # Avoid duplicates
                        carrier_id = carrier.get('id')
                        if carrier_id and not any(c.get('id') == carrier_id for c in found_carriers):
                            found_carriers.append(carrier)
                            print(f"    [OK] Found carrier {carrier_id} from search '{term}'")
                except Exception as e:
                    print(f"    [SKIP] Search '{term}': {e}")
        
        if not found_carriers:
            print("No carriers found in TMS2")
            return
        
        print(f"\nFound {len(found_carriers)} carriers, saving...")
        
        for i, carrier in enumerate(found_carriers[:num_carriers], 1):
            carrier_id = carrier.get('id', 'unknown')
            try:
                filename = carriers_dir / f"carrier_{carrier_id}_tms2.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(carrier, f, indent=2, ensure_ascii=False)
                
                print(f"  [{i}/{min(len(found_carriers), num_carriers)}] Saved carrier {carrier_id}")
                print(f"    Name: {carrier.get('name', 'N/A')}")
                print(f"    Status: {carrier.get('status', 'N/A')}")
                
            except Exception as e:
                print(f"  [FAIL] Failed to save carrier {carrier_id}: {e}")
        
        print(f"\nCompleted! Saved {min(len(found_carriers), num_carriers)} carriers to samples/carriers/")

if __name__ == "__main__":
    pull_tms2_carriers(num_carriers=5)

