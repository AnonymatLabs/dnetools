"""Utility functions for DNETOOLS."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import re
from typing import Optional


def is_valid_ip(ip: str) -> bool:
    """Check if the given string is a valid IPv4 or IPv6 address."""
    # Simple regex for IPv4
    ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(ipv4_pattern, ip):
        parts = ip.split(".")
        return all(0 <= int(p) <= 255 for p in parts)
    # IPv6 simple check (contains colon)
    if ":" in ip:
        # Very basic, but enough for most
        return True
    return False


def is_valid_domain(domain: str) -> bool:
    """Check if the string looks like a valid domain."""
    domain_pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.([A-Za-z]{2,6}\.)?[A-Za-z]{2,6}$"
    return bool(re.match(domain_pattern, domain))
