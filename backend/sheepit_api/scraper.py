from bs4 import BeautifulSoup as bs
from backend.sheepit_api.configuration.configuration import PROJECT_URL, FAILED_LOGIN_MESSAGE
from backend.sheepit_api.extract import Extract
from backend.sheepit_api.auth import create_and_store_session


def get_projects(session):
    project_page = session.get(PROJECT_URL).text
    soup = bs(project_page, "html.parser")
    tr = soup.find_all("tr")
    stop_if_login_is_unsuccessful(soup, tr)
    # store_as_bin("soup", soup)  # DEBUG

    results = []
    for element in tr:
        extract = Extract(element)
        results.append({
            "username": extract.username(),
            "scene": extract.scene_name(),
            "frames": extract.frames_number(),
            "devices": extract.enabled_devices(),
            "size": extract.size()
        })
    return results


def stop_if_login_is_unsuccessful(soup, tr):
    if tr == []:
        h4 = soup.find_all("h4")[0].text  # TODO: h4 could be extracted to the configuration file
        if h4 == FAILED_LOGIN_MESSAGE:
            raise ConnectionRefusedError("Session is not valid: {}".format(h4))


def get_current_projects(session):
    try:
        current_data = get_projects(session)
    except ConnectionRefusedError:
        print("Creating new session")
        session = create_and_store_session()
        current_data = get_projects(session)
    return current_data
