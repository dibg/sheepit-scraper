import sys
import requests
from configuration.scraper_config import POST_URL, LOGIN_HEADERS, LOGIN_PAYLOAD
from helper_functions.storage import store_as_bin, retrieve_bin


def create_session(login_url, headers, payload):
    session = requests.session()
    login_req = session.post(login_url, headers=headers, data=payload)
    if login_req.text != "OK":
        raise ConnectionRefusedError("Login failed, please check if the provided credentials are correct or if the "
                                     "site is not accessible.")
    return session


def create_and_store_session():
    try:
        session = create_session(POST_URL, LOGIN_HEADERS, LOGIN_PAYLOAD)
    except ConnectionRefusedError as cre:
        print(cre)
        sys.exit(1)
    store_as_bin("session", session)
    return session


def get_valid_login_session():
    try:
        session = retrieve_bin("session")
    except FileNotFoundError:
        create_and_store_session()
        session = retrieve_bin("session")
    return session
