# Image Upload Implementation Notes

## Overview
Successfully implemented image upload functionality for McLeod TMS API that uploads to object history (staging area).

## Key Findings

### Upload Behavior
- Images upload to **object history/staging area**, not directly to imaging
- API returns **batch IDs** (e.g., `GKZXC6`, `G64953`) for successful uploads
- Images do **not** appear immediately in load imaging area
- Requires **"Import to Imaging" service** from McLeod to move from history to imaging

### Technical Implementation
- **Endpoint**: `POST /images/{rowType}/{rowId}/{documentTypeId}`
- **Method**: Raw binary data in request body (NOT multipart form data)
- **Content-Type**: Auto-detected from file magic bytes (`application/pdf`, `image/jpeg`, etc.)
- **Authentication**: HTTP Basic Auth with session management
- **Optional**: `movementId` query parameter

### Supported File Types
- PDF (`application/pdf`)
- JPEG (`image/jpeg`) 
- PNG (`image/png`)
- GIF (`image/gif`)
- BMP (`image/bmp`)
- TIFF (`image/tiff`)

## Functions Added

### `upload_image_to_history()`
Main function that uploads images to TMS object history.

### Supporting Functions
- `get_available_doctypes()` - Get valid document type IDs
- `get_available_images()` - List existing images
- Content type detection via file magic bytes

## Next Steps
- Contact McLeod support for "Import to Imaging" service access
- Once enabled, images should automatically move from history to imaging area
- Consider implementing batch processing status checking if API provides it

## Test Results
✅ Upload functionality working correctly  
✅ Proper error handling and logging  
✅ Multiple input formats supported (file path, file object, binary data)  
✅ Document type validation  
✅ Movement ID support  
✅ Company ID overrides
