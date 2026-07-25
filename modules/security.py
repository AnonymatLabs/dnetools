"""IP reputation and security checks."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from typing import Dict, Any
from core.models import GeoInfo
from core.exceptions import ProviderError
from modules.geo import GeoEngine


class SecurityChecker:
    """Check IP for proxy/VPN/TOR/hosting status via geo providers."""

    def __init__(self):
        self.geo = GeoEngine()

    def check(self, ip: str) -> Dict[str, bool]:
        """
        Perform security checks on an IP.

        Returns:
            Dictionary with boolean flags.
        """
        try:
            geo_info = self.geo.lookup(ip)
            return {
                "is_proxy": geo_info.is_proxy,
                "is_vpn": geo_info.is_vpn,
                "is_tor": geo_info.is_tor,
                "is_hosting": geo_info.is_hosting,
            }
        except ProviderError as e:
            raise ProviderError(f"Security check failed: {e}")
        finally:
            self.geo.close()
