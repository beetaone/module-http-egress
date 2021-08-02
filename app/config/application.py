"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "EGRESS_WEBHOOK_URL": env("EGRESS_WEBHOOK_URL", "http://localhost:8000"),
}
