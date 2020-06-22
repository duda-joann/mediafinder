import requests
from .exceptions import CallApiError

def call_api(search_api: str, search_params: dict):
    result = requests.get(search_api, params=search_params)

    if result.status_code != 200:
        raise CallApiError("Error: API request unsuccessful")

    data = result.json()

    return data
