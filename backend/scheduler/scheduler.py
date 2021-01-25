import atexit
import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from backend.configuration.configuration import SCRAPING_INTERVAL_MINUTES
from flask_init import app


def init_once_per_session(func, *args):  # solves the double execution problem with flask in debug mode
    if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        func(*args)


def background_scheduler(task, interval):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=task, trigger="interval", minutes=interval)
    scheduler.start()
    atexit.register(scheduler.shutdown)


def start_background_scraping():
    projects = lambda: requests.get("http://127.0.0.1:5000/v1/snapshot_to_db")
    init_once_per_session(background_scheduler, projects, SCRAPING_INTERVAL_MINUTES)

