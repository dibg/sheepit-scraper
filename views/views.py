from configuration.scraper_config import VISIT_PROFILE_URL
from flask_init import app
from api.api import single_data_snapshot, db_data, most_projects
from flask import render_template
from helper_functions.file_filter import extract_routes_from_file

BLOCK_URL = "/v1/block?username="


@app.route("/")
def index():
    available_views = extract_routes_from_file("views/views.py")
    available_api_routes = extract_routes_from_file("api/api.py")
    return render_template("index.html", available_views=available_views, available_api_routes=available_api_routes)


@app.route("/view_all_projects")
def view_all_projects():
    data = db_data().json  # .json is a property of jsonify tha t holds the data
    return render_projects(data, "All Available Data")


@app.route("/view_current_projects")
def view_current_projects():
    data = single_data_snapshot().json
    return render_projects(data, "Current Data")


@app.route("/view_projects_per_user")
def view_most_projects():
    data = most_projects().json
    return render_template("view_projects_per_user.html",
                           data=data,
                           title="Projects per user",
                           block_url=BLOCK_URL,
                           visit_profile_url=VISIT_PROFILE_URL)


def render_projects(data, title):
    return render_template("view_projects.html",
                           data=data,
                           title=title,
                           block_url=BLOCK_URL,
                           visit_profile_url=VISIT_PROFILE_URL)
