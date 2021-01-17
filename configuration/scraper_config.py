from configuration.credentials import USERNAME, PASSWORD

URL = "https://www.sheepit-renderfarm.com/"
POST_URL = URL + "ajax.php"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
FAILED_LOGIN_MESSAGE = "Please sign in"

PROJECT_URL = URL + "index.php?show=projects"

REFERER_LOGIN = URL + "account.php?mode=login"
LOGIN_HEADERS = {"User-Agent": USER_AGENT, "Origin": URL, "Referer": REFERER_LOGIN}
LOGIN_PAYLOAD = {
    "account_login": "account_login",
    "do_login": "do_login",
    "login": USERNAME,
    "password": PASSWORD,
    "timezone": "Europe/Athens"
}

REFERER_BLOCK = URL + "account.php?mode=profile"
BLOCK_HEADERS = {"User-Agent": USER_AGENT, "Origin": URL, "Referer": REFERER_BLOCK}
BLOCK_PAYLOAD = {
    "action": "add_blocked_owner",
    "login": ""
}

REFERER_FRAMES = URL + "index.php?show=frames"
FRAMES_HEADERS = {"User-Agent": USER_AGENT, "Origin": URL, "Referer": REFERER_FRAMES}

STORAGE_PATH = "./data/"

SCRAPING_INTERVAL_MINUTES = 15
