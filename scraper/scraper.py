from bs4 import BeautifulSoup as bs
from configuration.scraper_config import PROJECT_URL
from helper_functions.storage import store_as_bin
from scraper.extract import *


def scrape_data(session):
    project_page = session.get(PROJECT_URL).text
    soup = bs(project_page, "html.parser")
    # store_as_bin("soup", soup)  # DEBUG
    tr = soup.find_all("tr")
    if tr == []:
        h4 = soup.find_all("h4")[0].text
        if h4 == "Please sign in":
            raise ConnectionRefusedError("Session is not valid: {}".format(h4))

    results = []
    for element in tr:
        scene = extract_scene_name(element)
        username = extract_username(element)
        size = extract_size(element)
        frames = extract_frames_number(element)
        devices = extract_enabled_devices(element)
        results.append({
            "Username": username,
            "Scene": scene,
            "Frames": frames,
            "Devices": devices,
            "Size": size
        })
    return results


