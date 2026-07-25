"""Banner for CLI application."""
"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

from rich.console import Console
from rich.text import Text
from core.version import __version__


def display_banner(console: Console) -> None:
    """Print the DNETOOLS v2 banner."""
    banner = Text()
    banner.append("  _____  _   _  _____  _____   ___   _   _   _____  _____ \n", style="cyan")
    banner.append(" |  __ \\| \\ | ||  __ \\|  ___| / _ \\ | \\ | | / ____||  __ \\\n", style="cyan")
    banner.append(" | |  \\/|  \\| || |  \\/| |_   | | | ||  \\| || |  __ | |__) |\n", style="cyan")
    banner.append(" | | __ | . ` || | __ |  _|  | | | || . ` || | |_ ||  _  /\n", style="cyan")
    banner.append(" | |_\\ \\| |\\  || |_\\ \\| |    | |_| || |\\  || |__| || | \\ \\\n", style="cyan")
    banner.append("  \\____/|_| \\_| \\____/|_|     \\___/ |_| \\_| \\_____/|_|  \\_\\\n", style="cyan")
    banner.append(f"                      v{__version__} - Network Intelligence Toolkit\n", style="yellow")
    console.print(banner)
