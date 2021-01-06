from configuration.credentials import USERNAME, PASSWORD

URL = "https://www.sheepit-renderfarm.com/"
LOGIN_URL = URL + "ajax.php"
REFERER = URL + "account.php?mode=login"
PROJECT_URL = URL + "index.php?show=projects"

PAYLOAD = {
    "account_login": "account_login",
    "do_login": "do_login",
    "login": USERNAME,
    "password": PASSWORD,
    "timezone": "Europe/Athens"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "Origin": URL, "Referer": REFERER}

FAILED_LOGIN_MESSAGE = "Please sign in"

STORAGE_PATH = "./data/"