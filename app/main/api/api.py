import requests
from main.exceptions import CallApiError


def call_api(search_api: str, search_params: dict) -> dict:

    """
     connect with  youtube api and get data
    :param search_api: api url address
    :param search_params:  dictionary with requested paarams
    :return: json object of the result
    """

    result = requests.get(search_api, params=search_params)

    if result.status_code != 200:
        raise CallApiError("Error: API request unsuccessful")

    data = result.json()

    return data
