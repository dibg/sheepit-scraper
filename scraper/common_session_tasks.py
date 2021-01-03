from helper_functions.storage import retrieve_json, store_as_json, retrieve_bin
from scraper.scraper import scrape_data
from scraper.session import create_and_store_session


def scrape_current_data(session):
    try:
        current_data = scrape_data(session)
    except ConnectionRefusedError:
        print("Creating new session")
        session = create_and_store_session()
        current_data = scrape_data(session)
    return current_data


def load_stored_data():
    try:
        stored_data = retrieve_json("data")
    except FileNotFoundError:
        print("Creating new data file")
        empty_json = []
        store_as_json("data", empty_json)
        stored_data = retrieve_json("data")
    return stored_data


def valid_login_session():
    try:
        session = retrieve_bin("session")
    except FileNotFoundError:
        create_and_store_session()
        session = retrieve_bin("session")
    return session