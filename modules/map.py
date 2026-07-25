"""Map link generation from coordinates."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from typing import Optional


class MapLinkGenerator:
    """Generate map links for given coordinates."""

    @staticmethod
    def google_maps(lat: float, lon: float) -> str:
        """Google Maps link."""
        return f"https://www.google.com/maps?q={lat},{lon}"

    @staticmethod
    def openstreetmap(lat: float, lon: float) -> str:
        """OpenStreetMap link."""
        return f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}&zoom=12"

    @staticmethod
    def bing_maps(lat: float, lon: float) -> str:
        """Bing Maps link."""
        return f"https://www.bing.com/maps?q={lat},{lon}"

    @staticmethod
    def generate_all(lat: float, lon: float) -> dict:
        """Generate all map links."""
        return {
            "google": MapLinkGenerator.google_maps(lat, lon),
            "openstreetmap": MapLinkGenerator.openstreetmap(lat, lon),
            "bing": MapLinkGenerator.bing_maps(lat, lon),
        }
