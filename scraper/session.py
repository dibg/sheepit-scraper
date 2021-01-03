import sys
import requests
from configuration.credentials import USERNAME, PASSWORD
from configuration.scraper_config import LOGIN_ROUTE, HEADERS
from helper_functions.storage import store_as_bin


def create_session(username, password):
    payload = {
        "account_login": "account_login",
        "do_login": "do_login",
        "login": username,
        "password": password,
        "timezone": "Europe/Athens"
    }

    session = requests.session()
    login_req = session.post(LOGIN_ROUTE, headers=HEADERS, data=payload)
    if login_req.text != "OK":
        raise ConnectionRefusedError("Login failed, please check if the provided credentials are correct or if the "
                                     "site is not accessible.")
    return session


def create_and_store_session():
    try:
        session = create_session(USERNAME, PASSWORD)
    except ConnectionRefusedError as cre:
        print(cre)
        sys.exit(1)

    store_as_bin("session", session)
    return session
