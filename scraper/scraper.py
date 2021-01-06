from bs4 import BeautifulSoup as bs
from configuration.scraper_config import PROJECT_URL, FAILED_LOGIN_MESSAGE
from helper_functions.storage import store_as_bin
from scraper.extract import *


def scrape_data(session):
    project_page = session.get(PROJECT_URL).text
    soup = bs(project_page, "html.parser")
    # store_as_bin("soup", soup)  # DEBUG
    tr = soup.find_all("tr")
    stop_if_login_is_unsuccessful(soup, tr)

    results = []
    for element in tr:
        scene = extract_scene_name(element)
        username = extract_username(element)
        size = extract_size(element)
        frames = extract_frames_number(element)
        devices = extract_enabled_devices(element)

        results.append({
            "username": username,
            "scene": scene,
            "frames": frames,
            "devices": devices,
            "size": size
        })
    return results


def stop_if_login_is_unsuccessful(soup, tr):
    if tr == []:
        h4 = soup.find_all("h4")[0].text  # TODO: h4 could be extracted to the configuration file
        if h4 == FAILED_LOGIN_MESSAGE:
            raise ConnectionRefusedError("Session is not valid: {}".format(h4))


