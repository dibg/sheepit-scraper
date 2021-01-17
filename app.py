from views.views import *
from scheduler import *


if __name__ == "__main__":
    init_scheduler()
    app.debug = True
    app.run(host="0.0.0.0")


# TODO: return redirect
# TODO: return proper status in case a function fails
# TODO: document structure: header footer menu
# TODO: filter database entries base on username, scene and date
# TODO: handle exception for lost connection
# TODO: user login page for blocking with different user than the one you scrape with
# TODO: rate limit user block to avoid ban
# TODO: better way to store scraper_configuration (class)
# TODO: dark theme
