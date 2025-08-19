# McLeod TMS Client Usage Guide

Quick reference for using the McLeod TMS API client in your projects.

## Installation

```bash
pip install mcleod-tms-client
```

## Basic Setup

```python
from mcleod_tms_client import TMSClient, RowTypes

# Initialize client (credentials from environment or direct)
with TMSClient("username", "password") as client:
    # Your API calls here
    pass
```

## Environment Variables

Create a `.env` file:
```
TMS_BASE_URL=https://your-tms-server.com/api
TMS_COMPANY_ID=TMS
```

## Common Examples

### Orders
```python
# Get orders
orders = client.get_json("/orders")
specific_order = client.get_json("/orders/5000003")

# Get orders from different company
orders_tms2 = client.get_json("/orders", company_id="TMS2")
```

### Images & Documents
```python
# Get available images for an order
images = client.get_available_images(RowTypes.ORDER, "5000003")

# Get enriched images with document type names
enriched = client.get_enriched_images(RowTypes.ORDER, "5000003")

# Download image as PDF
pdf_data = client.get_image_pdf("dta.bol.7.0.5000003")
with open("invoice.pdf", "wb") as f:
    f.write(pdf_data)

# Or save directly
client.save_image_pdf("dta.bol.7.0.5000003", "invoice")

# Upload image to order history
with open("receipt.pdf", "rb") as f:
    batch_id = client.upload_image_to_history(
        RowTypes.ORDER, "5000003", "7", f
    )
```

### Charges
```python
# Get available charge codes
codes = client.get_available_charge_codes()

# Add charge to order
success = client.add_charge(
    order_id="5000003",
    charge_id="LUM", 
    description="LUMPER",
    amount=75.00
)
```

### Web Framework Integration
```python
# Flask example
@app.route('/download/<image_id>')
def download_image(image_id):
    result = client.get_image_for_web(image_id)
    return Response(result['data'], headers=result['headers'])

# FastAPI example  
@app.get('/download/{image_id}')
def download_image(image_id: str):
    result = client.get_image_for_web(image_id)
    return Response(
        result['data'], 
        media_type="application/pdf",
        headers={"Content-Disposition": result['headers']['Content-Disposition']}
    )
```

## Row Types Constants

Use the `RowTypes` class for consistent row type values:

```python
RowTypes.ORDER      # "O" - Order
RowTypes.MOVEMENT   # "M" - Movement  
RowTypes.CUSTOMER   # "C" - Customer
RowTypes.LOCATION   # "L" - Location
RowTypes.PAYEE      # "P" - Payee
RowTypes.DRIVER     # "D" - Driver
RowTypes.TRACTOR    # "T" - Tractor
RowTypes.TRAILER    # "E" - Trailer
RowTypes.USER       # "U" - User
```

## Error Handling

```python
try:
    with TMSClient("user", "pass") as client:
        data = client.get_json("/orders/123")
except Exception as e:
    print(f"API Error: {e}")
```
