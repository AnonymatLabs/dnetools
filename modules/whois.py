"""WHOIS lookup module."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import whois
from typing import Dict, Any
from core.exceptions import InvalidInputError


class WhoisLookup:
    """Perform WHOIS lookup for domains."""

    def lookup(self, domain: str) -> Dict[str, Any]:
        """
        Retrieve WHOIS information for a domain.

        Returns:
            Dictionary of WHOIS data.
        """
        try:
            w = whois.whois(domain)
            return {
                "domain_name": w.domain_name,
                "registrar": w.registrar,
                "whois_server": w.whois_server,
                "creation_date": w.creation_date,
                "expiration_date": w.expiration_date,
                "updated_date": w.updated_date,
                "name_servers": w.name_servers,
                "status": w.status,
                "emails": w.emails,
                "dnssec": w.dnssec,
            }
        except whois.parser.PywhoisError as e:
            raise InvalidInputError(f"WHOIS error: {e}")
        except Exception as e:
            raise InvalidInputError(f"WHOIS failed: {e}")
