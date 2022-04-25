"""
Business logic for health
"""
import time

from app.config import WEEVE
from flask import jsonify

startTime = time.time()


def health_check():
    """
    Returns server status and uptime
    """
    return jsonify(
        {
            "serverStatus": "Running",
            "uptime": time.time() - startTime,
            "module": WEEVE["MODULE_NAME"],
        }
    )
