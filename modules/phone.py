"""Phone number information module."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from typing import Dict, Any
from core.exceptions import InvalidInputError


class PhoneInfo:
    """Retrieve information about a phone number."""

    @staticmethod
    def lookup(number: str, default_region: str = "US") -> Dict[str, Any]:
        """
        Get details for a phone number.

        Args:
            number: Phone number string.
            default_region: ISO country code for parsing.

        Returns:
            Dictionary with number details.
        """
        try:
            parsed = phonenumbers.parse(number, default_region)
        except phonenumbers.NumberParseException as e:
            raise InvalidInputError(f"Invalid phone number: {e}")

        if not phonenumbers.is_valid_number(parsed):
            raise InvalidInputError("Invalid phone number format")

        return {
            "country_code": parsed.country_code,
            "national_number": parsed.national_number,
            "region": phonenumbers.region_code_for_number(parsed),
            "carrier": carrier.name_for_number(parsed, "en"),
            "geocode": geocoder.description_for_number(parsed, "en"),
            "timezone": timezone.time_zones_for_number(parsed),
            "is_possible": phonenumbers.is_possible_number(parsed),
            "is_valid": phonenumbers.is_valid_number(parsed),
            "number_type": phonenumbers.number_type(parsed),
        }
