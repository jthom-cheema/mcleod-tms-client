## Contributing

### Docs snapshot (`docs/`)
`docs/` is a **vendor documentation snapshot** (export of McLeod `/ws/docs`).

- **Treat `docs/` as read-only** (update by regenerating the snapshot, not hand-editing pages).
- **Don’t treat docs as ground truth for behavior**: validate endpoints/fields against the live server for your tenant/version/permissions before changing `tms_client.py`.
- **Never add secrets** (credentials, tokens, customer-private data) to `docs/` (or `samples/`).

