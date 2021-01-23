from views.views import *
from scraper.scheduler import *


if __name__ == "__main__":
    app.debug = True
    start_background_scraping()
    app.run(host="0.0.0.0")


# TODO: decouple api from views
# TODO: document structure: header footer menu
# TODO: return redirect
# TODO: return proper status in case a function fails
# TODO: handle exception for lost connection
# TODO: rate limit user block to avoid ban
# TODO: user login page for blocking with different user than the one you scrape with
# TODO: better way to store scraper_configuration (class)
# TODO: show if user is new to the service
