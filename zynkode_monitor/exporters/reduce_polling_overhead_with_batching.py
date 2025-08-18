"""
Performance: reduce polling overhead with batching

Part of zynkode-monitor - Real-time GPU telemetry dashboard for AMD hardware.
"""

from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class Exporters:
    """Implementation for: Performance: reduce polling overhead with batching"""

    def __init__(self, config: dict = None):
        self.config = config or {}
        logger.info(f"Initialized Exporters")

    def run(self, **kwargs) -> Any:
        """Execute the primary operation."""
        raise NotImplementedError
