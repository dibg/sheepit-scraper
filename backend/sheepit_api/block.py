from backend.sheepit_api.configuration.configuration import BLOCK_PAYLOAD, POST_URL, BLOCK_HEADERS


def block_user(session, username):
    payload = BLOCK_PAYLOAD
    payload["login"] = username
    session.post(POST_URL, data=payload, headers=BLOCK_HEADERS)
    return "ok"
