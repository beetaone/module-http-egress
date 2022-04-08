"""
All constants specific to the application
"""
from app.utils.env import env

APPLICATION = {
    "EGRESS_WEBHOOK_URL": env("EGRESS_WEBHOOK_URL", ""),
    "METHOD": env("METHOD", "POST"),
    "LABELS": env("LABELS", ""),
    "TIMESTAMP": env("TIMESTAMP", ""),
    "CONTENT_TYPE_JSON": env("CONTENT_TYPE_JSON", "no"),
    "AUTHENTICATION_REQUIRED": env("AUTHENTICATION_REQUIRED", "no"),
    "ACCESS_TOKEN": env("ACCESS_TOKEN", ""),
    "AUTHENTICATION_API_KEY": env("AUTHENTICATION_API_KEY", ""),
    "ERROR_URL": env("ERROR_URL", ""),
}
