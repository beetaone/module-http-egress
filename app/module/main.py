from requests import post
from app.config import APPLICATION

"""
All logic related to the module's main application
Mostly only this file requires changes
"""

def module_main(parsed_data):
    """
    Egresses data to a chosen Webhook.

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        post(url=f"{APPLICATION['EGRESS_WEBHOOK_URL']}", json=parsed_data, headers={'Content-Type': 'application/json'})
        return parsed_data, None
    except Exception:
        return None, "Unable to perform the module logic"
