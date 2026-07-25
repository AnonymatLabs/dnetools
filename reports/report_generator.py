"""Report generation in JSON and TXT formats."""

"""
DNETOOLS v2

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""

import json
from datetime import datetime
from typing import Dict, Any, Optional
from pathlib import Path
from core.models import GeoInfo


class ReportGenerator:
    """Generate reports from data."""

    @staticmethod
    def generate_json(data: Dict[str, Any], output_file: Optional[str] = None) -> str:
        """
        Generate a JSON report.

        Args:
            data: Dictionary containing report data.
            output_file: If provided, save to file.

        Returns:
            JSON string.
        """
        report = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "data": data,
        }
        json_str = json.dumps(report, indent=2, default=str)
        if output_file:
            Path(output_file).write_text(json_str)
        return json_str

    @staticmethod
    def generate_txt(data: Dict[str, Any], output_file: Optional[str] = None) -> str:
        """
        Generate a plain text report.

        Args:
            data: Dictionary containing report data.
            output_file: If provided, save to file.

        Returns:
            Text string.
        """
        lines = []
        lines.append("=" * 60)
        lines.append("DNETOOLS v2 Report")
        lines.append(f"Generated: {datetime.utcnow().isoformat()}Z")
        lines.append("=" * 60)
        for key, value in data.items():
            if isinstance(value, dict):
                lines.append(f"\n{key.upper()}:")
                for sub_key, sub_val in value.items():
                    lines.append(f"  {sub_key}: {sub_val}")
            else:
                lines.append(f"{key}: {value}")
        txt = "\n".join(lines)
        if output_file:
            Path(output_file).write_text(txt)
        return txt

    @staticmethod
    def geo_to_report(geo: GeoInfo) -> Dict[str, Any]:
        """Convert GeoInfo to a dictionary suitable for reporting."""
        return geo.to_dict()
