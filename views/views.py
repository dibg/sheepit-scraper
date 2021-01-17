from flask_init import app
from api.api import single_data_snapshot, db_data
from flask import render_template
from helper_functions.file_filter import extract_routes_from_file


@app.route("/")
def index():
    available_views = extract_routes_from_file("views/views.py")
    available_api_routes = extract_routes_from_file("api/api.py")
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
    block_url = "/v1/block"
    return render_template("view_data.html", data=data, title=title, block_url=block_url)
