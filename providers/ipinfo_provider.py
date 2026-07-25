"""IPInfo provider (ipinfo.io)."""
"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from typing import Dict, Any
from core.config import CONFIG
from core.models import GeoInfo
from .base_provider import BaseProvider


class IPInfoProvider(BaseProvider):
    """Provider using ipinfo.io API."""

    BASE_URL = "https://ipinfo.io/"

    @property
    def name(self) -> str:
        return "ipinfo"

    def lookup(self, ip: str) -> GeoInfo:
        """Perform lookup via ipinfo.io."""
        url = f"{self.BASE_URL}{ip}/json"
        params = {}
        if CONFIG.IPINFO_API_KEY:
            params["token"] = CONFIG.IPINFO_API_KEY

        data = self._get(url, params=params)

        # ipinfo returns 'error' on failure
        if "error" in data:
            raise ValueError(f"IPInfo error: {data.get('error', 'Unknown error')}")

        # Parse ASN details
        asn_str = data.get("org", "")
        asn = None
        as_name = None
        if asn_str and " " in asn_str:
            parts = asn_str.split(" ", 1)
            asn = parts[0]
            as_name = parts[1] if len(parts) > 1 else None

        # Location split: lat,long
        loc = data.get("loc", "")
        lat = lon = None
        if loc and "," in loc:
            parts = loc.split(",", 1)
            try:
                lat = float(parts[0])
                lon = float(parts[1])
            except ValueError:
                pass

        return GeoInfo(
            ip=data.get("ip", ip),
            hostname=None,  # not directly
            isp=None,       # same as org
            organization=data.get("org"),
            asn=asn,
            as_name=as_name,
            continent=None,
            country=data.get("country"),
            country_code=data.get("country"),
            region=data.get("region"),
            city=data.get("city"),
            zip_code=data.get("postal"),
            latitude=lat,
            longitude=lon,
            timezone=data.get("timezone"),
            currency=None,
            calling_code=None,
            is_proxy=False,  # not provided
            is_vpn=False,
            is_tor=False,
            is_hosting=False,
            provider=self.name,
            raw=data,
        )
