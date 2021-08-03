from requests import post
from app.config import APPLICATION
import time

"""
All logic related to the module's main application
Mostly only this file requires changes
"""

EGRESS_WEBHOOK_URL = APPLICATION['EGRESS_WEBHOOK_URL']
METHOD = APPLICATION['METHOD']
# if APPLICATION['LABELS'] == '' 
if APPLICATION['LABELS']:
    LABELS = [label.strip() for label in APPLICATION['LABELS'].split(',')]
else:
    LABELS = None
TIMESTAMP = APPLICATION['TIMESTAMP']


def rest_post(data):
    try:
        # build return body
        return_body = {}
        if LABELS:
            for label in LABELS:
                if label in data.keys():
                    return_body[label] = data[label]
        else:
            return_body = data

        # add timestamp
        if not TIMESTAMP:
            return_body['timestamp'] = time.time()
        else:
            return_body['timestamp'] = TIMESTAMP
        
        post(url=f"{EGRESS_WEBHOOK_URL}", json=return_body, headers={'Content-Type': 'application/json'})
        return True
    except Exception:
        return False

def rest_get(data):
    return True

def module_main(parsed_data):
    """
    Egresses data to a chosen Webhook.

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        if METHOD == "POST":
            response = rest_post(parsed_data)
        
        if response:
            # success
            return parsed_data, None
        else:
            # failure
            return None, "Unable to perform the module logic" 
    except Exception:
        return None, "Unable to perform the module logic"
