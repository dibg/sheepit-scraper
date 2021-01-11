from flask_init import app
from helper_functions.database import Data
from flask import jsonify
from helper_functions.database import insert_data
from scraper.common_session_tasks import scrape_current_data, load_stored_data, get_valid_login_session
from helper_functions.storage import store_as_json, retrieve_json


@app.route("/v1/snapshot")
def single_data_snapshot():
    session = get_valid_login_session()
    current_data = scrape_current_data(session)
    data_json = jsonify(current_data)
    return data_json


@app.route("/v1/snapshot_to_db")
def snapshot_to_db():
    snapshot = single_data_snapshot()
    for entry in snapshot.json:
        data = Data(entry)
        insert_data(data)
    return "ok"


@app.route("/v1/db_data")
def db_data():
    data = Data.query.all()
    dict = []
    for datum in data:
        dict.append(datum.as_dict())
    data_json = jsonify(dict)
    return data_json


@app.route("/v1/raw_data")
def raw_data():
    data = retrieve_json("data")
    data_json = jsonify(data)
    return data_json


@app.route("/v1/load_stored_data_to_db")
def load_data():
    json_data = load_stored_data()
    for entry in json_data:
        data = Data(entry)
        insert_data(data)
    return "ok"


@app.route("/v1/db_create")
def create_db():
    db.create_all()
    return "ok"


@app.route("/v1/db_delete")
def delete_db():
    Data.query.delete()
    db.session.commit()
    return "ok"