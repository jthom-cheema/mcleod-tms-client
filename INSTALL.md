# Installing McLeod TMS Client in Other Projects

## Quick Setup

1. **Install as editable package** (from your other project directory):
   ```bash
   pip install -e /path/to/mcleod-tms-client
   
   # Or using relative path:
   pip install -e ../mcleod-tms-client
   ```

2. **Copy environment template** to your project:
   ```bash
   cp /path/to/mcleod-tms-client/.env.example .env
   # Edit .env with your actual TMS URL and credentials
   ```

3. **Use in your project**:
   ```python
   from tms_client import TMSClient, RowTypes
   
   with TMSClient("username", "password") as client:
       orders = client.get_json("/orders")
       images = client.get_available_images(RowTypes.ORDER, "12345")
   ```

## Benefits of Editable Install

✅ **Live updates** - Changes to the library automatically appear in your project  
✅ **No copying files** - Import like any normal package  
✅ **Easy development** - Modify library and consumer project simultaneously  
✅ **Proper packaging** - Handles dependencies automatically  

## Development Workflow

1. **Make changes** to the TMS client library
2. **Test immediately** in your consumer project (no reinstall needed)
3. **Commit changes** when ready
4. **Other team members** can pull and use updated library

## Project Structure

```
your-workspace/
├── mcleod-tms-client/          # This library
│   ├── tms_client.py
│   ├── setup.py
│   └── .env.example
└── your-other-project/         # Consumer project
    ├── main.py                 # Uses: from tms_client import TMSClient
    ├── .env                    # TMS configuration
    └── requirements.txt        # Your project deps
```

## Troubleshooting

**Import Error:**
```bash
# Make sure you're in the right environment
pip show mcleod-tms-client

# Reinstall if needed
pip uninstall mcleod-tms-client
pip install -e /path/to/mcleod-tms-client
```

**Environment Issues:**
- Make sure `.env` file exists in your consumer project
- Check that `TMS_BASE_URL` is set correctly
- Verify credentials work with the test script

## Production Deployment

For production, consider:
1. **Version pinning**: `pip install mcleod-tms-client==1.0.0`
2. **Private PyPI**: Upload to internal package repository
3. **Git tags**: Tag stable releases for reproducible builds
