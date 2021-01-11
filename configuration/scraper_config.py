from configuration.credentials import USERNAME, PASSWORD

URL = "https://www.sheepit-renderfarm.com/"
POST_URL = URL + "ajax.php"
REFERER_LOGIN = URL + "account.php?mode=login"
REFERER_BLOCK = URL + "account.php?mode=profile"
PROJECT_URL = URL + "index.php?show=projects"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"

FAILED_LOGIN_MESSAGE = "Please sign in"

LOGIN_HEADERS = {"User-Agent": USER_AGENT, "Origin": URL, "Referer": REFERER_LOGIN}

BLOCK_HEADERS = {"User-Agent": USER_AGENT, "Origin": URL, "Referer": REFERER_BLOCK}

LOGIN_PAYLOAD = {
    "account_login": "account_login",
    "do_login": "do_login",
    "login": USERNAME,
    "password": PASSWORD,
    "timezone": "Europe/Athens"
}

BLOCK_PAYLOAD = {
    "action": "add_blocked_owner",
    "login": ""
}

STORAGE_PATH = "./data/"
