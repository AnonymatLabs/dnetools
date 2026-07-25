"""Geolocation module with provider fallback and merging."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from typing import Optional, List
from core.models import GeoInfo
from core.exceptions import ProviderError, NetworkError
from providers import (
    IPWhoIsProvider,
    IPApiProvider,
    IPInfoProvider,
    ProxyCheckProvider,
    BaseProvider,
)
from core.config import CONFIG
import logging

logger = logging.getLogger(__name__)


class GeoEngine:
    """Main geolocation engine with provider fallback."""

    def __init__(self, provider_order: Optional[List[str]] = None):
        """Initialize with optional provider order."""
        self.provider_order = provider_order or list(CONFIG.PROVIDER_ORDER)
        self.providers: List[BaseProvider] = self._init_providers()

    def _init_providers(self) -> List[BaseProvider]:
        """Instantiate providers in order."""
        provider_map = {
            "ipwhois": IPWhoIsProvider,
            "ipapi": IPApiProvider,
            "ipinfo": IPInfoProvider,
            "proxycheck": ProxyCheckProvider,
        }
        providers = []
        for name in self.provider_order:
            if name in provider_map:
                providers.append(provider_map[name]())
        return providers

    def lookup(self, ip: str) -> GeoInfo:
        """
        Perform geolocation lookup with fallback across providers.

        Returns:
            GeoInfo merged from all successful providers.

        Raises:
            ProviderError: if all providers fail.
        """
        merged = None
        last_error = None

        for provider in self.providers:
            try:
                logger.debug(f"Trying provider: {provider.name}")
                result = provider.lookup(ip)
                if merged is None:
                    merged = result
                else:
                    merged.merge(result)
                logger.debug(f"Provider {provider.name} succeeded")
            except Exception as e:
                logger.warning(f"Provider {provider.name} failed: {e}")
                last_error = e
                continue

        if merged is None:
            raise ProviderError(f"All providers failed. Last error: {last_error}")

        return merged

    def close(self) -> None:
        """Close all provider sessions."""
        for provider in self.providers:
            try:
                provider.close()
            except Exception:
                pass
