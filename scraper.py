from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests
from configuration.scraper_config import *
from functions.storage import *


def extract_scene_name(element):
    scene = element.strong.text
    return scene


def extract_username(element):
    username = element.find_all("td")[1].span.text
    return username


def extract_size(element):
    size = element.find_all("td")[5].text
    return size


def extract_frames_number(element):
    frames_str = element.find(attrs={"class": "sr-only"}).text
    frames_cut_location = (frames_str.find("/") + 2)
    frames = frames_str[frames_cut_location:]
    return frames


def extract_enabled_devices(element):
    devices = element.find_all("td")[4].find_all("img")
    cpu = devices[0]["alt"]
    gpu = devices[1]["alt"]
    cpu_is_enabled = cpu.find("enabled") > 0
    gpu_is_enabled = gpu.find("enabled") > 0
    switch = {
        1: "CPU",
        2: "GPU",
        3: "CPU/GPU"
    }
    enabled_devices = switch.get(cpu_is_enabled + gpu_is_enabled * 2)
    return enabled_devices


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
    # cookies = login_req.cookies
    print(login_req)  # TODO: check if it's not 200 and report to the user
    return session


def scrape_data(session):
    project_page = session.get(SCRAPING_URL).text
    soup = bs(project_page, "html.parser")
    # store_as_bin("soup", soup)  # DEBUG
    tr = soup.find_all("tr")
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M")

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
            # "Created": timestamp
        })
    return results


def debug_routine():
    soup = retrieve_bin("soup")
    tr = soup.find_all("tr")
    print(extract_frames_number(tr[3]))
    print(extract_frames_number(tr[4]))
    print(extract_frames_number(tr[5]))
    print(extract_frames_number(tr[6]))
