from configuration.scraper_config import VISIT_PROFILE_URL
from flask_init import app
from api.api import single_data_snapshot, db_data, projects_per_user, projects_by
from flask import render_template
from helper_functions.file_filter import extract_routes_from_file

BLOCK_URL = "/v1/block?username="
PROJECTS_BY_URL = "/view_projects_by/"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/view_all_available_routes")
def available_routes():
    available_views = extract_routes_from_file("views/views.py")
    available_api_routes = extract_routes_from_file("api/api.py")
    return render_template("available_routes.html", available_views=available_views, available_api_routes=available_api_routes)


@app.route("/view_all_projects")
def view_all_projects():
    data = db_data().json  # .json is a property of jsonify that holds the data
    return render_projects(data, "All Available Data")


@app.route("/view_current_projects")
def view_current_projects():
    data = single_data_snapshot().json
    return render_projects(data, "Current Data")


@app.route("/view_projects_per_user")
def view_projects_per_user():
    data = projects_per_user().json
    return render_template("view_projects_per_user.html",
                           data=data,
                           title="Projects per user",
                           block_url=BLOCK_URL,
                           visit_profile_url=VISIT_PROFILE_URL,
                           projects_by_url=PROJECTS_BY_URL)


@app.route("/view_projects_by/<username>")
def view_projects_by(username):
    data = projects_by(username).json
    return render_template("view_projects_by.html",
                           data=data,
                           title=username+"'s projects")


def render_projects(data, title):
    return render_template("view_projects.html",
                           data=data,
                           title=title,
                           block_url=BLOCK_URL,
                           visit_profile_url=VISIT_PROFILE_URL,
                           projects_by_url=PROJECTS_BY_URL)


@app.route("/login")
def login():
    return render_template("login.html")
