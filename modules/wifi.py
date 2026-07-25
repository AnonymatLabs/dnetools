"""Local WiFi information module."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import subprocess
import platform
import re
from typing import List, Dict, Any
from core.exceptions import NetworkError


class WiFiInfo:
    """Retrieve local WiFi network information (SSID, signal, etc.)."""

    @staticmethod
    def get_ssid() -> str:
        """
        Get current WiFi SSID.

        Returns:
            SSID string or empty if not connected.
        """
        system = platform.system()
        try:
            if system == "Windows":
                output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("utf-8")
                for line in output.split("\n"):
                    if "SSID" in line and "BSSID" not in line:
                        parts = line.split(":", 1)
                        if len(parts) > 1:
                            return parts[1].strip()
            elif system == "Darwin":  # macOS
                output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]).decode("utf-8")
                for line in output.split("\n"):
                    if "SSID" in line:
                        parts = line.split(":", 1)
                        if len(parts) > 1:
                            return parts[1].strip()
            elif system == "Linux":
                output = subprocess.check_output(["iwgetid", "-r"]).decode("utf-8").strip()
                return output
        except Exception:
            pass
        return ""

    @staticmethod
    def get_signal() -> str:
        """Get signal strength (placeholder, OS-specific)."""
        # Simplified; more robust implementation would use system tools
        return "N/A"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return a dictionary of WiFi info."""
        ssid = WiFiInfo.get_ssid()
        return {
            "ssid": ssid,
            "signal": WiFiInfo.get_signal(),
            "connected": bool(ssid),
        }
