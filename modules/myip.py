"""Public IP detection module."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import requests
from typing import Optional
from core.exceptions import NetworkError


class MyIP:
    """Detect the public IP address of the current machine."""

    PROVIDERS = [
        "https://api.ipify.org?format=json",
        "https://icanhazip.com",
        "https://ifconfig.me/ip",
    ]

    @classmethod
    def get_ip(cls) -> str:
        """
        Retrieve public IP address using multiple providers.

        Returns:
            IP address as string.

        Raises:
            NetworkError: if all providers fail.
        """
        for url in cls.PROVIDERS:
            try:
                resp = requests.get(url, timeout=10)
                if resp.status_code == 200:
                    if "json" in url:
                        data = resp.json()
                        ip = data.get("ip")
                        if ip:
                            return ip
                    else:
                        ip = resp.text.strip()
                        if ip:
                            return ip
            except Exception:
                continue
        raise NetworkError("Unable to determine public IP")
