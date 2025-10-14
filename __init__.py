"""McLeod TMS API Python Client."""

# Allow import both as a package and from source tree during tests
try:
    from .tms_client import TMSClient, RowTypes
except Exception:  # pragma: no cover - fallback for direct source execution
    from tms_client import TMSClient, RowTypes

__version__ = "0.1.0"
__all__ = ["TMSClient", "RowTypes"]
