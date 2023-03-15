"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from os import getenv

from logging import getLogger
from requests import get, post
from json import dumps

log = getLogger("module")

if getenv("LABELS"):
    LABELS = [label.strip() for label in getenv("LABELS").split(",")]
else:
    LABELS = None


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        # build return body
        if type(received_data) == dict:
            return_body = processData(received_data)
        else:
            return_body = []
            for data in received_data:
                return_body.append(processData(data))

        # set header if necessary
        headers = {}
        if bool(getenv("CONTENT_TYPE_JSON")):
            headers.update({"Content-Type": "application/json"})

        if bool(getenv("AUTHENTICATION_REQUIRED")) and getenv("ACCESS_TOKEN") != "":
            headers.update({"Authorization": f"{getenv('ACCESS_TOKEN')}"})

        if getenv("AUTHENTICATION_API_KEY") != "":
            headers.update({"x-api-key": getenv("AUTHENTICATION_API_KEY")})

        # parse egress urls for fanout
        urls = [
            url.strip() for url in getenv("EGRESS_WEBHOOK_URLS").strip(",").split(",")
        ]

        # for collecting REST API POST responses
        failed_responses = []

        for url in urls:
            # send data out
            try:
                if getenv("METHOD") == "POST":
                    response = post(url=url, json=return_body, headers=headers)
                elif getenv("METHOD") == "GET":
                    if type(received_data) == dict:
                        response = get(url=url, params=return_body, headers=headers)
                    else:
                        response = get(
                            url=url,
                            params={"data": dumps(return_body)},
                            headers=headers,
                        )

                log.debug(
                    f"Sent data to url {url} | Response: {response.status_code} {response.reason}"
                )

                if response.status_code != 200:
                    failed_responses.append(
                        {
                            "url": url,
                            "status_code": response.status_code,
                            "message": response.reason,
                        }
                    )
            except Exception as e:
                log.error(f"Exception sending to {url}: {e}")
                failed_responses.append(
                    {
                        "url": url,
                        "status_code": None,
                        "message": str(e),
                    }
                )

        if failed_responses:
            if getenv("ERROR_URL") != "":
                log.debug(f"Sending to ERROR URL: {getenv('ERROR_URL')}")
                info = {"responses_log": failed_responses}
                post(url=getenv("ERROR_URL"), json=info)
            else:
                return f"Unable to transfer data: {failed_responses}"

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"


def processData(parsed_data):
    global LABELS
    return_body = {}
    if LABELS:
        for label in LABELS:
            # check if selected input label is in input data
            if label in parsed_data.keys():
                return_body[label] = parsed_data[label]
    else:
        return_body = parsed_data

    return return_body
