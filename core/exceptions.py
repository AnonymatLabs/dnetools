"""Custom exceptions for DNETOOLS."""
"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

class DNEToolsError(Exception):
    """Base exception for all DNETOOLS errors."""

    pass


class ProviderError(DNEToolsError):
    """Raised when a provider fails to return data."""

    pass


class NetworkError(DNEToolsError):
    """Raised for network-related issues."""

    pass


class InvalidInputError(DNEToolsError):
    """Raised for invalid user input."""

    pass
