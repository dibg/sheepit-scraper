from scraper.common_session_tasks import scrape_current_data, load_stored_data, get_valid_login_session
from helper_functions.list_modifiers import unique_list
from helper_functions.storage import store_as_json
from helper_functions.html_generator import generate_html


def single_data_snapshot():
    session = get_valid_login_session()
    stored_data = load_stored_data()
    current_data = scrape_current_data(session)

    print(current_data)
    unique_data = unique_list(stored_data + current_data)
    store_as_json("data", unique_data)
    generate_html(unique_data)
