import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from configuration.scraper_config import SCRAPING_INTERVAL_MINUTES
import requests


def start_background_scraping():
    def task():
        requests.get("http://127.0.0.1:5000/v1/snapshot_to_db")
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=task, trigger="interval", minutes=SCRAPING_INTERVAL_MINUTES)
    scheduler.start()
    atexit.register(scheduler.shutdown)
