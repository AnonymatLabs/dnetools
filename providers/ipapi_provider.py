"""IPApi provider (ipapi.co)."""
"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from typing import Dict, Any
from core.models import GeoInfo
from .base_provider import BaseProvider


class IPApiProvider(BaseProvider):
    """Provider using ipapi.co API."""

    BASE_URL = "https://ipapi.co/"

    @property
    def name(self) -> str:
        return "ipapi"

    def lookup(self, ip: str) -> GeoInfo:
        """Perform lookup via ipapi.co."""
        url = f"{self.BASE_URL}{ip}/json/"
        data = self._get(url)

        # ipapi returns 'error' key on failure
        if "error" in data:
            raise ValueError(f"IPApi error: {data.get('error', 'Unknown error')}")

        return GeoInfo(
            ip=data.get("ip", ip),
            hostname=None,  # not provided
            isp=data.get("org"),
            organization=data.get("org"),  # same as ISP
            asn=data.get("asn"),
            as_name=None,
            continent=data.get("continent_code"),
            country=data.get("country_name"),
            country_code=data.get("country_code"),
            region=data.get("region"),
            city=data.get("city"),
            zip_code=data.get("postal"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            timezone=data.get("timezone"),
            currency=data.get("currency"),
            calling_code=None,
            is_proxy=False,      # not provided
            is_vpn=False,
            is_tor=False,
            is_hosting=False,
            provider=self.name,
            raw=data,
        )
