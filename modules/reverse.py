"""Reverse DNS lookup module."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import dns.reversename
import dns.resolver
from typing import Optional
from core.exceptions import InvalidInputError


class ReverseLookup:
    """Perform reverse DNS lookup."""

    def __init__(self):
        self.resolver = dns.resolver.Resolver()

    def lookup(self, ip: str) -> Optional[str]:
        """
        Perform reverse DNS lookup for an IP.

        Returns:
            Hostname if found, else None.
        """
        try:
            rev_name = dns.reversename.from_address(ip)
            answers = self.resolver.resolve(rev_name, "PTR")
            return str(answers[0]) if answers else None
        except dns.resolver.NXDOMAIN:
            return None
        except dns.exception.Timeout:
            raise InvalidInputError("Reverse DNS query timed out")
        except Exception as e:
            raise InvalidInputError(f"Reverse DNS error: {e}")
