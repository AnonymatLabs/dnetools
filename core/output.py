"""Rich output formatting for DNETOOLS."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from typing import Any, Dict, List, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import json
from core.models import GeoInfo


class OutputFormatter:
    """Handle all terminal output using Rich."""

    def __init__(self, console: Optional[Console] = None):
        self.console = console or Console()

    def print_geo_info(self, geo: GeoInfo) -> None:
        """Display GeoInfo in a rich table."""
        table = Table(title=f"Geolocation for {geo.ip}", show_header=False, box=None)
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="white")

        fields = [
            ("IP", geo.ip),
            ("Hostname", geo.hostname),
            ("ISP", geo.isp),
            ("Organization", geo.organization),
            ("ASN", geo.asn),
            ("AS Name", geo.as_name),
            ("Continent", geo.continent),
            ("Country", geo.country),
            ("Country Code", geo.country_code),
            ("Region", geo.region),
            ("City", geo.city),
            ("Zip Code", geo.zip_code),
            ("Latitude", geo.latitude),
            ("Longitude", geo.longitude),
            ("Timezone", geo.timezone),
            ("Currency", geo.currency),
            ("Calling Code", geo.calling_code),
            ("Provider", geo.provider),
        ]

        for label, value in fields:
            if value is not None:
                table.add_row(label, str(value))

        # Security flags
        flags = []
        if geo.is_proxy:
            flags.append("proxy")
        if geo.is_vpn:
            flags.append("VPN")
        if geo.is_tor:
            flags.append("TOR")
        if geo.is_hosting:
            flags.append("hosting")
        if flags:
            table.add_row("Security", ", ".join(flags))

        self.console.print(table)

    def print_json(self, data: Dict[str, Any]) -> None:
        """Output data as pretty JSON."""
        self.console.print(json.dumps(data, indent=2, default=str))

    def print_panel(self, title: str, content: str, style: str = "white") -> None:
        """Display a panel."""
        panel = Panel(content, title=title, style=style)
        self.console.print(panel)

    def print_error(self, message: str) -> None:
        """Display an error message."""
        self.console.print(f"[red]Error:[/red] {message}")

    def print_success(self, message: str) -> None:
        """Display a success message."""
        self.console.print(f"[green]✓[/green] {message}")

    def print_table(self, headers: List[str], rows: List[List[Any]], title: Optional[str] = None) -> None:
        """Display a generic table."""
        table = Table(title=title, show_header=True, header_style="bold cyan")
        for header in headers:
            table.add_column(header)
        for row in rows:
            table.add_row(*[str(cell) for cell in row])
        self.console.print(table)
