from configuration.scraper_config import REFERER_BLOCK, BLOCK_PAYLOAD, POST_URL, BLOCK_HEADERS


def block_user(session, username):
    payload = BLOCK_PAYLOAD
    payload["login"] = username
    session.post(POST_URL, data=payload, headers=BLOCK_HEADERS)
    return "ok"
