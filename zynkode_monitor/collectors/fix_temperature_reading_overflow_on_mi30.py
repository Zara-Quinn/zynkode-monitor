"""
Fix temperature reading overflow on MI300X

Part of zynkode-monitor - Real-time GPU telemetry dashboard for AMD hardware.
"""

from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class Collectors:
    """Implementation for: Fix temperature reading overflow on MI300X"""

    def __init__(self, config: dict = None):
        self.config = config or {}
        logger.info(f"Initialized Collectors")

    def run(self, **kwargs) -> Any:
        """Execute the primary operation."""
        raise NotImplementedError
