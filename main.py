from time import sleep
from scraper import create_session, scrape_data
from configuration.credentials import USERNAME, PASSWORD
from functions.storage import *
from functions.list_modifiers import unique_list
from functions.html_generator import *


session = create_session(USERNAME, PASSWORD)  # TODO: if session exist try login if fails create new session
store_as_bin("session", session)

# session = retrieve_bin("session")
while True:
    stored_data = retrieve_json("data")  # TODO: if file not exist create it
    current_data = scrape_data(session)
    print(current_data)

    unique_data = unique_list(stored_data + current_data)
    store_as_json("data", unique_data)
    generate_html(unique_data)

    sleep(600)

