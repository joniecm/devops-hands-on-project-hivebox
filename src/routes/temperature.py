"""Temperature endpoint blueprint."""

from flask import Blueprint, jsonify

from src.services.sensebox_service import SenseBoxService
from src.services.temperature_service import TemperatureService


temperature_bp = Blueprint("temperature", __name__)

sensebox_service = SenseBoxService()
temperature_service = TemperatureService()


@temperature_bp.route("/temperature", methods=["GET"])
def temperature():
    """Return the current average temperature from all senseBoxes.

    Fetches temperature data from configured senseBoxes and returns
    the average value. Only includes data from the last hour.

    Returns:
        JSON response with average_temperature field, or error message.
    """
    avg_temp = sensebox_service.get_average_temperature_for_fresh_data(
        box_ids=temperature_service.get_sensebox_ids()
    )

    if avg_temp is None:
        return jsonify({
            "error": "No temperature data available",
            "message": (
                "Unable to retrieve fresh temperature data from "
                "senseBoxes. Data may be unavailable or older than 1 hour."
            )
        }), 503

    return jsonify({
        "average_temperature": round(avg_temp, 2),
        "status": temperature_service.get_temperature_status(avg_temp)
    })
