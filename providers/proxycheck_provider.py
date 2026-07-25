"""ProxyCheck provider (proxycheck.io)."""
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


class ProxyCheckProvider(BaseProvider):
    """Provider using proxycheck.io API (focus on proxy/VPN/TOR detection)."""

    BASE_URL = "https://proxycheck.io/"

    @property
    def name(self) -> str:
        return "proxycheck"

    def lookup(self, ip: str) -> GeoInfo:
        """Perform lookup via proxycheck.io."""
        url = f"{self.BASE_URL}v2/{ip}"
        params = {
            "vpn": "1",
            "asn": "1",
            "timeout": str(CONFIG.HTTP_TIMEOUT),
        }
        if CONFIG.PROXYCHECK_API_KEY:
            params["key"] = CONFIG.PROXYCHECK_API_KEY

        data = self._get(url, params=params)

        # Response: {"status":"ok","ip":{...}} or {"status":"error",...}
        if data.get("status") == "error":
            raise ValueError(f"ProxyCheck error: {data.get('message', 'Unknown error')}")

        ip_data = data.get(ip, {})
        if not ip_data:
            raise ValueError("No data for IP")

        # Extract proxy/vpn/tor/hosting flags
        is_proxy = ip_data.get("proxy", "no") == "yes"
        is_vpn = ip_data.get("vpn", "no") == "yes"
        is_tor = ip_data.get("tor", "no") == "yes"
        is_hosting = ip_data.get("hosting", "no") == "yes"

        # ASN from the provider (sometimes as "asn" field)
        asn = ip_data.get("asn")
        as_name = ip_data.get("asname")

        return GeoInfo(
            ip=ip,
            hostname=None,
            isp=ip_data.get("isp"),
            organization=ip_data.get("org"),
            asn=asn,
            as_name=as_name,
            continent=ip_data.get("continent"),
            country=ip_data.get("country"),
            country_code=ip_data.get("countrycode"),
            region=ip_data.get("region"),
            city=ip_data.get("city"),
            zip_code=ip_data.get("postcode"),
            latitude=ip_data.get("latitude"),
            longitude=ip_data.get("longitude"),
            timezone=ip_data.get("timezone"),
            currency=None,
            calling_code=None,
            is_proxy=is_proxy,
            is_vpn=is_vpn,
            is_tor=is_tor,
            is_hosting=is_hosting,
            provider=self.name,
            raw=data,
        )
