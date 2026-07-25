"""Constants used throughout DNETOOLS v2."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from enum import Enum


class ExitCode(Enum):
    """System exit codes."""

    SUCCESS = 0
    ERROR = 1
    USAGE = 2
    NETWORK_ERROR = 3
    PROVIDER_ERROR = 4
    INVALID_INPUT = 5


class ProviderName(Enum):
    """Names of available providers."""

    IPWHOIS = "ipwhois"
    IPAPI = "ipapi"
    IPINFO = "ipinfo"
    PROXYCHECK = "proxycheck"


# Default provider endpoints
PROVIDER_ENDPOINTS = {
    ProviderName.IPWHOIS: "https://ipwho.is/",
    ProviderName.IPAPI: "https://ipapi.co/",
    ProviderName.IPINFO: "https://ipinfo.io/",
    ProviderName.PROXYCHECK: "https://proxycheck.io/",
}
