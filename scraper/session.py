import sys
import requests
from configuration.scraper_config import LOGIN_URL, HEADERS, PAYLOAD
from helper_functions.storage import store_as_bin


def create_session(login_url, headers, payload):
    session = requests.session()
    login_req = session.post(login_url, headers=headers, data=payload)
    if login_req.text != "OK":
        raise ConnectionRefusedError("Login failed, please check if the provided credentials are correct or if the "
                                     "site is not accessible.")
    return session


def create_and_store_session():
    try:
        session = create_session(LOGIN_URL, HEADERS, PAYLOAD)
    except ConnectionRefusedError as cre:
        print(cre)
        sys.exit(1)
    store_as_bin("session", session)
    return session
