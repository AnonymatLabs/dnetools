"""Abstract base class for all IP intelligence providers."""
"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import requests
from core.config import CONFIG
from core.models import GeoInfo


class BaseProvider(ABC):
    """Base provider with shared HTTP session and helper methods."""

    def __init__(self) -> None:
        """Initialize with a requests.Session."""
        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": CONFIG.USER_AGENT,
            "Accept": "application/json",
        })
        self._session.timeout = CONFIG.HTTP_TIMEOUT

    def close(self) -> None:
        """Close the underlying session."""
        self._session.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit, close session."""
        self.close()

    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Perform a GET request and return JSON response.

        Raises:
            requests.RequestException: on network or HTTP errors.
            ValueError: if response is not JSON.
        """
        response = self._session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    @abstractmethod
    def lookup(self, ip: str) -> GeoInfo:
        """
        Look up intelligence for the given IP address.

        Args:
            ip: IPv4 or IPv6 address.

        Returns:
            GeoInfo object populated with provider data.

        Raises:
            Exception: if lookup fails.
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Provider name identifier."""
        pass
