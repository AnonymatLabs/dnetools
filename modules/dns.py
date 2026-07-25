"""DNS intelligence module."""
"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import dns.resolver
from typing import List, Dict, Any
from core.exceptions import InvalidInputError


class DNSLookup:
    """Perform DNS lookups for various record types."""

    def __init__(self):
        self.resolver = dns.resolver.Resolver()

    def lookup(self, domain: str, record_type: str = "A") -> List[str]:
        """
        Perform DNS lookup for a given domain and record type.

        Args:
            domain: Domain name.
            record_type: DNS record type (A, MX, NS, TXT, etc.)

        Returns:
            List of record values.
        """
        try:
            answers = self.resolver.resolve(domain, record_type)
            return [str(r) for r in answers]
        except dns.resolver.NoAnswer:
            return []
        except dns.resolver.NXDOMAIN:
            raise InvalidInputError(f"Domain {domain} does not exist")
        except dns.exception.Timeout:
            raise InvalidInputError("DNS query timed out")
        except Exception as e:
            raise InvalidInputError(f"DNS error: {e}")

    def lookup_a(self, domain: str) -> List[str]:
        """A records."""
        return self.lookup(domain, "A")

    def lookup_mx(self, domain: str) -> List[str]:
        """MX records."""
        return self.lookup(domain, "MX")

    def lookup_ns(self, domain: str) -> List[str]:
        """NS records."""
        return self.lookup(domain, "NS")

    def lookup_txt(self, domain: str) -> List[str]:
        """TXT records."""
        return self.lookup(domain, "TXT")

    def lookup_all(self, domain: str) -> Dict[str, List[str]]:
        """Return common record types."""
        result = {}
        for rec in ["A", "MX", "NS", "TXT"]:
            try:
                result[rec] = self.lookup(domain, rec)
            except Exception:
                result[rec] = []
        return result
