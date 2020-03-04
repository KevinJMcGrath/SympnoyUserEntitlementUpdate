import jsonpickle
import requests

import config

from symphony import endpoints


def get_auth_token(endpoint):
    response = requests.post(endpoint, cert=config.bot_certificate)

    if response.status_code == 200:
        resp_json = jsonpickle.decode(response.text)
        return resp_json['token']

    response.raise_for_status()


def authenticate_bot_by_cert():
    session_ep = endpoints.session_auth_cert()
    km_ep = endpoints.km_auth_cert()

    session_token = get_auth_token(session_ep)
    km_token = get_auth_token(km_ep)

    return session_token, km_token