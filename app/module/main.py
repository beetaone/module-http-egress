from requests import post, get
from app.config import APPLICATION
import time

"""
All logic related to the module's main application
Mostly only this file requires changes
"""

EGRESS_WEBHOOK_URL = APPLICATION['EGRESS_WEBHOOK_URL']
METHOD = APPLICATION['METHOD']
if APPLICATION['LABELS']:
    LABELS = [label.strip() for label in APPLICATION['LABELS'].split(',')]
else:
    LABELS = None
TIMESTAMP = APPLICATION['TIMESTAMP']

def module_main(parsed_data):
    """
    Egresses data to a chosen Webhook with POST or GET methods.

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        # build return body
        return_body = {}
        if LABELS:
            for label in LABELS:
                # check if selected input label is in input data
                if label in parsed_data.keys():
                    return_body[label] = parsed_data[label]
        else:
            return_body = parsed_data

        # add timestamp
        if not TIMESTAMP:
            return_body['timestamp'] = time.time()
        else:
            return_body['timestamp'] = TIMESTAMP

        if METHOD == "POST":
            post(url=f"{EGRESS_WEBHOOK_URL}", json=return_body, headers={'Content-Type': 'application/json'})
        elif METHOD == "GET":
            get(url=f"{EGRESS_WEBHOOK_URL}", params=return_body)

        return return_body, None
    except Exception:
        return None, "Unable to perform the module logic"
