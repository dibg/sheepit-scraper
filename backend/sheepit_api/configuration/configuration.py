USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"

URL = "https://www.sheepit-renderfarm.com/"
POST_URL = URL + "ajax.php"
PROJECT_URL = URL + "index.php?show=projects"
VISIT_PROFILE_URL = URL + "account.php?mode=profile&login="  # + username


def prepare_headers(referer):
    return {"User-Agent": USER_AGENT, "Origin": URL, "Referer": referer}


LOGIN_HEADERS = prepare_headers(URL + "account.php?mode=login")
LOGIN_PAYLOAD = {
    "account_login": "account_login",
    "do_login": "do_login",
    "login": "",
    "password": "",
    "timezone": "Europe/Athens"
}
FAILED_LOGIN_MESSAGE = "Please sign in"


BLOCK_HEADERS = prepare_headers(URL + "account.php?mode=profile")
BLOCK_PAYLOAD = {
    "action": "add_blocked_owner",
    "login": ""
}


FRAMES_HEADERS = prepare_headers(URL + "index.php?show=frames")



