import atexit
import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from configuration.scraper_config import SCRAPING_INTERVAL_MINUTES
from flask_init import app


def init_once_per_session(func):
    if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        func()


def start_background_scraping():
    init_once_per_session(background_scraping)


def background_scraping():
    def task():
        requests.get("http://127.0.0.1:5000/v1/snapshot_to_db")

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=task, trigger="interval", minutes=SCRAPING_INTERVAL_MINUTES)
    scheduler.start()
    atexit.register(scheduler.shutdown)
