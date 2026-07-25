"""ASN information module."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import requests
from typing import Dict, Any
from core.exceptions import NetworkError, InvalidInputError


class ASNLookup:
    """Retrieve ASN information using a public API."""

    def lookup(self, ip: str) -> Dict[str, Any]:
        """
        Get ASN details for an IP address using ip-api.com (free).

        Returns:
            Dictionary with ASN and related info.
        """
        url = f"http://ip-api.com/json/{ip}?fields=status,message,as,isp,org,country,regionName,city,zip,lat,lon,timezone"
        try:
            resp = requests.get(url, timeout=10)
            data = resp.json()
            if data.get("status") == "fail":
                raise InvalidInputError(f"ASN lookup failed: {data.get('message', 'Unknown error')}")
            # Extract AS number and name
            asn_str = data.get("as", "")
            asn = None
            as_name = None
            if asn_str and " " in asn_str:
                parts = asn_str.split(" ", 1)
                asn = parts[0]
                as_name = parts[1] if len(parts) > 1 else None
            return {
                "ip": ip,
                "asn": asn,
                "as_name": as_name,
                "isp": data.get("isp"),
                "org": data.get("org"),
                "country": data.get("country"),
                "region": data.get("regionName"),
                "city": data.get("city"),
                "zip": data.get("zip"),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "timezone": data.get("timezone"),
            }
        except requests.RequestException as e:
            raise NetworkError(f"Network error: {e}")
