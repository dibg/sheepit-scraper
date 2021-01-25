from flask import jsonify, request
from sqlalchemy import and_
from datetime import datetime, timedelta
from flask_init import app
from backend.model.database import Data, db
from backend.model.database import insert_data
from backend.utils.list_modifiers import jsonify_dict
from backend.sheepit_api.scraper import scrape_current_data
from backend.sheepit_api.session import get_valid_login_session


@app.route("/v1/snapshot")
def single_data_snapshot():
    session = get_valid_login_session()
    current_data = scrape_current_data(session)
    return jsonify(current_data)


@app.route("/v1/db_data")
def db_data(last_hours=None):
    last_hours = request.args.get('last_hours')
    if last_hours is not None:
        data = Data.query.filter(Data.date_created >= datetime.today() - timedelta(hours=int(last_hours)))
    else:
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


@app.route("/v1/snapshot_to_db")
def snapshot_to_db():
    snapshot = single_data_snapshot()
    for entry in snapshot.json:
        data = Data(entry)
        insert_data(data)
    return "ok"