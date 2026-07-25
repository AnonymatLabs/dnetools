#!/usr/bin/env python3
"""DNETOOLS v2 - Main CLI application."""

import argparse
import sys
import json
from typing import List, Optional
from rich.console import Console
from core.banner import display_banner
from core.output import OutputFormatter
from core.exceptions import DNEToolsError, InvalidInputError, ProviderError, NetworkError
from core.version import __version__
from core.utils import is_valid_ip, is_valid_domain
from modules.geo import GeoEngine
from modules.dns import DNSLookup
from modules.reverse import ReverseLookup
from modules.whois import WhoisLookup
from modules.asn import ASNLookup
from modules.map import MapLinkGenerator
from modules.phone import PhoneInfo
from modules.wifi import WiFiInfo
from modules.myip import MyIP
from modules.security import SecurityChecker
from reports.report_generator import ReportGenerator
import traceback


console = Console()
output = OutputFormatter(console)


def error_exit(msg: str, code: int = 1) -> None:
    """Print error and exit."""
    output.print_error(msg)
    sys.exit(code)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog="dnetools",
        description="DNETOOLS v2 - Network Intelligence Toolkit",
        epilog="For more help, visit https://github.com/yourname/dnetools",
    )
    parser.add_argument("-v", "--version", action="version", version=f"DNETOOLS v{__version__}")

    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to run")

    # geo
    geo_parser = subparsers.add_parser("geo", help="IP geolocation lookup")
    geo_parser.add_argument("ip", help="IP address to lookup")
    geo_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # dns
    dns_parser = subparsers.add_parser("dns", help="DNS lookup")
    dns_parser.add_argument("domain", help="Domain to lookup")
    dns_parser.add_argument("--type", choices=["A", "MX", "NS", "TXT", "ALL"], default="ALL", help="Record type")

    # whois
    whois_parser = subparsers.add_parser("whois", help="WHOIS lookup")
    whois_parser.add_argument("domain", help="Domain to lookup")
    whois_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # reverse
    reverse_parser = subparsers.add_parser("reverse", help="Reverse DNS lookup")
    reverse_parser.add_argument("ip", help="IP address")

    # asn
    asn_parser = subparsers.add_parser("asn", help="ASN information")
    asn_parser.add_argument("ip", help="IP address")
    asn_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # myip
    subparsers.add_parser("myip", help="Get your public IP")

    # map
    map_parser = subparsers.add_parser("map", help="Generate map links from coordinates")
    map_parser.add_argument("lat", type=float, help="Latitude")
    map_parser.add_argument("lon", type=float, help="Longitude")

    # phone
    phone_parser = subparsers.add_parser("phone", help="Phone number information")
    phone_parser.add_argument("number", help="Phone number")
    phone_parser.add_argument("--region", default="US", help="ISO country code for parsing")

    # wifi
    subparsers.add_parser("wifi", help="Show local WiFi information")

    # security
    security_parser = subparsers.add_parser("security", help="IP security reputation check")
    security_parser.add_argument("ip", help="IP address")
    security_parser.add_argument("--json", action="store_true", help="Output as JSON")

    return parser.parse_args()


def main() -> None:
    """Main entry point."""
    try:
        display_banner(console)
        args = parse_args()

        if args.command == "geo":
            if not is_valid_ip(args.ip):
                error_exit("Invalid IP address")
            engine = GeoEngine()
            try:
                geo = engine.lookup(args.ip)
                if args.json:
                    output.print_json(geo.to_dict())
                else:
                    output.print_geo_info(geo)
                # Optionally generate report? We'll keep it simple.
            finally:
                engine.close()

        elif args.command == "dns":
            if not is_valid_domain(args.domain):
                error_exit("Invalid domain")
            dns = DNSLookup()
            if args.type == "ALL":
                result = dns.lookup_all(args.domain)
                for rec_type, records in result.items():
                    if records:
                        output.print_panel(f"{rec_type} Records", "\n".join(records))
                    else:
                        output.print_panel(f"{rec_type} Records", "No records found", style="yellow")
            else:
                records = dns.lookup(args.domain, args.type)
                if records:
                    output.print_panel(f"{args.type} Records", "\n".join(records))
                else:
                    output.print_panel(f"{args.type} Records", "No records found", style="yellow")

        elif args.command == "whois":
            if not is_valid_domain(args.domain):
                error_exit("Invalid domain")
            whois = WhoisLookup()
            data = whois.lookup(args.domain)
            if args.json:
                output.print_json(data)
            else:
                # Show as table
                rows = [[k, v] for k, v in data.items() if v]
                output.print_table(["Field", "Value"], rows, title=f"WHOIS for {args.domain}")

        elif args.command == "reverse":
            if not is_valid_ip(args.ip):
                error_exit("Invalid IP")
            rev = ReverseLookup()
            hostname = rev.lookup(args.ip)
            if hostname:
                output.print_success(f"Hostname: {hostname}")
            else:
                output.print_panel("Reverse DNS", "No PTR record found", style="yellow")

        elif args.command == "asn":
            if not is_valid_ip(args.ip):
                error_exit("Invalid IP")
            asn = ASNLookup()
            data = asn.lookup(args.ip)
            if args.json:
                output.print_json(data)
            else:
                rows = [[k, v] for k, v in data.items() if v]
                output.print_table(["Field", "Value"], rows, title=f"ASN for {args.ip}")

        elif args.command == "myip":
            try:
                ip = MyIP.get_ip()
                output.print_success(f"Your public IP: {ip}")
            except NetworkError as e:
                error_exit(str(e))

        elif args.command == "map":
            links = MapLinkGenerator.generate_all(args.lat, args.lon)
            for name, url in links.items():
                output.print_panel(f"{name.capitalize()} Map", url)

        elif args.command == "phone":
            info = PhoneInfo.lookup(args.number, args.region)
            rows = [[k, v] for k, v in info.items() if v is not None]
            output.print_table(["Field", "Value"], rows, title=f"Phone info for {args.number}")

        elif args.command == "wifi":
            wifi = WiFiInfo.get_info()
            rows = [[k, v] for k, v in wifi.items()]
            output.print_table(["Field", "Value"], rows, title="WiFi Information")

        elif args.command == "security":
            if not is_valid_ip(args.ip):
                error_exit("Invalid IP")
            checker = SecurityChecker()
            result = checker.check(args.ip)
            if args.json:
                output.print_json(result)
            else:
                rows = [[k, v] for k, v in result.items()]
                output.print_table(["Threat", "Detected"], rows, title=f"Security Report for {args.ip}")

        else:
            error_exit("Unknown command", 2)

    except KeyboardInterrupt:
        output.print_error("Interrupted by user")
        sys.exit(1)
    except (ProviderError, NetworkError, InvalidInputError) as e:
        output.print_error(str(e))
        sys.exit(1)
    except DNEToolsError as e:
        output.print_error(str(e))
        sys.exit(1)
    except Exception as e:
        output.print_error(f"Unexpected error: {e}")
        if console.is_tty:
            console.print("[dim]Use --debug for traceback[/dim]")
        else:
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
