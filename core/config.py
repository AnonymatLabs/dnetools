"""Configuration management for DNETOOLS v2."""
"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    """Application configuration loaded from environment variables."""

    # API keys for providers that require them
    IPINFO_API_KEY: Optional[str] = None
    PROXYCHECK_API_KEY: Optional[str] = None

    # Timeouts (seconds)
    HTTP_TIMEOUT: int = 10

    # User-Agent
    USER_AGENT: str = "DNETOOLS-v2/2.0"

    # Default provider order
    PROVIDER_ORDER: tuple = ("ipwhois", "ipapi", "ipinfo", "proxycheck")

    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables."""
        return cls(
            IPINFO_API_KEY=os.environ.get("IPINFO_API_KEY"),
            PROXYCHECK_API_KEY=os.environ.get("PROXYCHECK_API_KEY"),
            HTTP_TIMEOUT=int(os.environ.get("DNETOOLS_TIMEOUT", "10")),
            USER_AGENT=os.environ.get("DNETOOLS_USER_AGENT", "DNETOOLS-v2/2.0"),
        )


# Singleton config instance
CONFIG = Config.from_env()
