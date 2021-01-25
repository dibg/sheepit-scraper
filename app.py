from backend.scheduler.scheduler import start_background_scraping
from views.views import *


if __name__ == "__main__":
    # app.debug = True
    start_background_scraping()
    app.run(host="0.0.0.0")
