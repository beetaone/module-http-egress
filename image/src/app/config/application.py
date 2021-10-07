"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "EGRESS_URL": env("EGRESS_URL", "http://localhost:8000"),
    "METHOD": env("METHOD", "POST"),
    "LABELS": env("LABELS", ""),
    "TIMESTAMP": env("TIMESTAMP", "")
}
