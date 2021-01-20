from flask import jsonify, request
from sqlalchemy import and_
from datetime import datetime, timedelta
from flask_init import app
from helper_functions.database import Data, db
from helper_functions.database import insert_data
from helper_functions.list_modifiers import jsonify_dict
from helper_functions.storage import retrieve_json, load_or_if_not_exits_create_json_file
from scraper.block import block_user
from scraper.scraper import scrape_current_data
from scraper.session import get_valid_login_session


@app.route("/v1/snapshot")
def single_data_snapshot():
    session = get_valid_login_session()
    current_data = scrape_current_data(session)
    return jsonify(current_data)


@app.route("/v1/db_data")
def db_data():
    data = Data.query.all()
    return jsonify_dict(data)


@app.route("/v1/projects_per_user")
def projects_per_user(last_hours=None):
    last_hours = request.args.get('last_hours')
    if last_hours is not None:
        q = "SELECT username, COUNT(username) as cnt FROM data WHERE date_created >= NOW() - " \
            "'{} hours'::INTERVAL  GROUP BY username ORDER BY cnt DESC".format(last_hours)
    else:
        q = "SELECT username, COUNT(username) as cnt FROM data GROUP BY username ORDER BY cnt DESC"
    data = db.engine.execute(q)
    dict = [({"username": datum[0], "cnt": datum[1]}) for datum in data]
    return jsonify(dict)


@app.route("/v1/projects_by/<username>")
def projects_by(username, last_hours=None):
    last_hours = request.args.get('last_hours')
    if last_hours is not None:
        projects = Data.query.filter(and_(Data.date_created >= datetime.today() - timedelta(hours=int(last_hours)),
                                     Data.username == username))
    else:
        projects = Data.query.filter_by(username=username)
    return jsonify_dict(projects)


@app.route("/v1/block")
def block():
    username = request.args.get('username')
    if not username:
        return "Direct access to this link is not supported."
    block_user(get_valid_login_session(), username)
    return "User " + username + " is blocked"


@app.route("/v1/raw_data")
def raw_data():
    data = retrieve_json("data")
    return jsonify(data)


@app.route("/v1/snapshot_to_db")
def snapshot_to_db():
    snapshot = single_data_snapshot()
    for entry in snapshot.json:
        data = Data(entry)
        insert_data(data)
    return "ok"


@app.route("/v1/load_stored_data_to_db")
def load_data():
    json_data = load_or_if_not_exits_create_json_file("data")
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
