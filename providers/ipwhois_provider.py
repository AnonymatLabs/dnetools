"""IPWhoIs provider (ipwho.is)."""
"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from typing import Dict, Any
from core.models import GeoInfo
from .base_provider import BaseProvider


class IPWhoIsProvider(BaseProvider):
    """Provider using ipwho.is API."""

    BASE_URL = "https://ipwho.is/"

    @property
    def name(self) -> str:
        return "ipwhois"

    def lookup(self, ip: str) -> GeoInfo:
        """Perform lookup via ipwho.is."""
        url = f"{self.BASE_URL}{ip}"
        data = self._get(url)

        # ipwho.is returns success: false on error
        if not data.get("success", True):
            raise ValueError(f"IPWhoIs error: {data.get('message', 'Unknown error')}")

        return GeoInfo(
            ip=data.get("ip", ip),
            hostname=data.get("hostname"),
            isp=data.get("isp"),
            organization=data.get("org"),
            asn=data.get("asn"),
            as_name=data.get("as"),
            continent=data.get("continent"),
            country=data.get("country"),
            country_code=data.get("country_code"),
            region=data.get("region"),
            city=data.get("city"),
            zip_code=data.get("postal"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            timezone=data.get("timezone"),
            currency=data.get("currency"),
            calling_code=data.get("calling_code"),
            is_proxy=data.get("is_proxy", False),
            is_vpn=data.get("is_vpn", False),
            is_tor=data.get("is_tor", False),
            is_hosting=data.get("is_hosting", False),
            provider=self.name,
            raw=data,
        )
