from views.views import *
from scheduler import *


if __name__ == "__main__":
    start_background_scraping()
    app.debug = True
    app.run(host="0.0.0.0")


# TODO: filter database by date
# TODO: return redirect
# TODO: return proper status in case a function fails
# TODO: handle exception for lost connection
# TODO: rate limit user block to avoid ban
# TODO: document structure: header footer menu
# TODO: user login page for blocking with different user than the one you scrape with
# TODO: better way to store scraper_configuration (class)
# TODO: dark theme
