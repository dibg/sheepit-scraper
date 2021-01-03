URL = "https://www.sheepit-renderfarm.com/"
LOGIN_ROUTE = URL + "ajax.php"
REFERER = URL + "account.php?mode=login"
PROJECT_URL = URL + "index.php?show=projects"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "Origin": URL, "Referer": REFERER}

STORAGE_PATH = "./data/"