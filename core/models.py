"""Data models using dataclasses."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class GeoInfo:
    """Geolocation and network intelligence for an IP address."""

    ip: str
    hostname: Optional[str] = None
    isp: Optional[str] = None
    organization: Optional[str] = None
    asn: Optional[str] = None
    as_name: Optional[str] = None
    continent: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    region: Optional[str] = None
    city: Optional[str] = None
    zip_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    timezone: Optional[str] = None
    currency: Optional[str] = None
    calling_code: Optional[str] = None
    is_proxy: bool = False
    is_vpn: bool = False
    is_tor: bool = False
    is_hosting: bool = False
    provider: Optional[str] = None
    raw: Dict[str, Any] = field(default_factory=dict)

    def merge(self, other: "GeoInfo") -> "GeoInfo":
        """Merge another GeoInfo into this one, preferring non-None values."""
        for field_name in self.__dataclass_fields__:
            current_val = getattr(self, field_name)
            other_val = getattr(other, field_name)
            if other_val is not None and current_val is None:
                setattr(self, field_name, other_val)
            elif isinstance(current_val, dict) and isinstance(other_val, dict):
                # Merge raw dicts
                setattr(self, field_name, {**current_val, **other_val})
        return self

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
