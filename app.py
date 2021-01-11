from flask_init import app
from api import single_data_snapshot, db_data
from flask import render_template, request
from scraper.block import block_user
from scraper.common_session_tasks import get_valid_login_session
from helper_functions.file_filter import extract_routes_from_file


# TODO: automatically scrape data
# TODO: return redirect
# TODO: return proper status in case a function fails
# TODO: document structure: header footer menu
# TODO: filter database entries base on username, scene and date
# TODO: handle exception for lost connection
# TODO: user login page for blocking with different user than the one you scrape with


@app.route("/")
def index():
    available_views = extract_routes_from_file("app.py")
    available_api_routes = extract_routes_from_file("api.py")
    return render_template("index.html", available_views=available_views, available_api_routes=available_api_routes)


@app.route("/view_all")
def view_all():
    data = db_data().json
    return render_data(data, "All Available Data")


@app.route("/view_current")
def view_current():
    data = single_data_snapshot().json
    return render_data(data, "Current Data")


def render_data(data, title):
    block_url = "/block"
    return render_template("view_data.html", data=data, title=title, block_url=block_url)


@app.route("/block")
def block():
    username = request.args.get('username')
    if not username:
        return "Direct access to this link is not supported."
    block_user(get_valid_login_session(), username)
    return "User " + username + " is blocked"


# @app.before_first_request
# def init_scheduler():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(func=snapshot_to_db, trigger="interval", minutes=1)
#     scheduler.start()
#     atexit.register(scheduler.shutdown)


if __name__ == "__main__":
    app.debug = True
    app.run()
