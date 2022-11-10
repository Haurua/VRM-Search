import requests
from requests import Response


def dvla_api_request(vrm: str) -> Response:
    """Input string is UK registration number used to for an API request to DVLA.

    :parameter:
            vrm (str): user provided string (registration number) used for the payload.
    :returns:
            (Response): Response object containing relevant vehicle information from the DVLA.
    """
    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    payload = "{" + f"\n\t\"registrationNumber\": \"{vrm}\"" + "\n}"
    headers = {
        'x-api-key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url=url, headers=headers, data=payload)
    return response
