"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "EGRESS_WEBHOOK_URL": env("EGRESS_WEBHOOK_URL", "https://telegraf.wohnio.weeve.engineering/vicki"),
    "METHOD": env("METHOD", "POST"),
    "LABELS": env("LABELS", ""),
    "TIMESTAMP": env("TIMESTAMP", "timestamp"),
    "CONTENT_TYPE_JSON" : env("CONTENT_TYPE_JSON", "no"),
    "AUTHENTICATION_BEARER" : env("AUTHENTICATION_BEARER", "no"),
    "AUTHENTICATION_TOKEN" : env("AUTHENTICATION_TOKEN", ""),
}
