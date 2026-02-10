"""Service module for temperature business logic."""

from typing import List, Optional


# List of senseBox IDs to fetch temperature data from
SENSEBOX_IDS = [
    "5c647389a100840019eea656",
    "66268770eaca630008ec4f9e",
    "6570eb180db9850007f21abe",
]


class TemperatureService:
    """Business logic for temperature-related operations."""

    def __init__(self, sensebox_ids: Optional[List[str]] = None) -> None:
        self._sensebox_ids = (
            list(sensebox_ids) if sensebox_ids is not None else list(SENSEBOX_IDS)
        )

    def get_sensebox_ids(self) -> List[str]:
        """Return the senseBox IDs that should be used for temperature data."""
        return list(self._sensebox_ids)

    @staticmethod
    def get_temperature_status(temperature: float) -> str:
        """Determine temperature status based on the average temperature.

        Args:
            temperature: The average temperature value.

        Returns:
            Status string: "Too Cold", "Good", or "Too Hot".
        """
        if temperature < 10:
            return "Too Cold"
        elif temperature <= 36:
            return "Good"
        else:
            return "Too Hot"
