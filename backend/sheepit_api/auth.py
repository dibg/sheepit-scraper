import sys
import requests
from backend.sheepit_api.configuration.configuration import POST_URL, LOGIN_HEADERS, LOGIN_PAYLOAD
from backend.utils.storage import store_as_bin, retrieve_bin


def create_session(login_url, headers, payload):
    session = requests.session()
    login_req = session.post(login_url, headers=headers, data=payload)
    if login_req.text != "OK":
        raise ConnectionRefusedError("Login failed, please check if the provided credentials are correct or if the "
                                     "site is not accessible.")
    return session


def create_and_store_session(username, password):
    try:
        session = create_session(POST_URL, LOGIN_HEADERS, prepare_login_payload(username, password))
    except ConnectionRefusedError as cre:
        print(cre)
        sys.exit(1)
    session_filename = username
    store_as_bin(session_filename, session)
    return session


def get_session(username, password):
    session_filename = username
    try:
        session = retrieve_bin(session_filename)
    except FileNotFoundError:
        session = create_and_store_session(username, password)
    return session


def prepare_login_payload(username, password):
    payload = LOGIN_PAYLOAD
    payload["login"] = username
    payload["password"] = password
    return payload
