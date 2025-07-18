"""
Add custom metric support via plugin system

Part of zynkode-monitor - Real-time GPU telemetry dashboard for AMD hardware.
"""

from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class Dashboard:
    """Implementation for: Add custom metric support via plugin system"""

    def __init__(self, config: dict = None):
        self.config = config or {}
        logger.info(f"Initialized Dashboard")

    def run(self, **kwargs) -> Any:
        """Execute the primary operation."""
        raise NotImplementedError
