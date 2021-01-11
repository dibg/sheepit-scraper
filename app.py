from datetime import datetime
from flask import Flask, jsonify, render_template, request
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy
from configuration.credentials import POSTGRESQL_URI
from scraper.block import block_user
from scraper.common_session_tasks import scrape_current_data, load_stored_data, get_valid_login_session
from helper_functions.storage import store_as_json, retrieve_json
from helper_functions.file_filter import extract_routes_from_file

# TODO: automatically scrape data
# TODO: return redirect
# TODO: return proper status in case a function fails
# TODO: document structure: header footer menu
# TODO: filter database entries base on username, scene and date
# TODO: handle exception for lost connection

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRESQL_URI
db = SQLAlchemy(app)


class Data(db.Model):
    username = db.Column(db.String(64), nullable=False, primary_key=True)
    scene = db.Column(db.String(200), nullable=False, primary_key=True)
    frames = db.Column(db.Integer, nullable=False, primary_key=True)
    devices = db.Column(db.String(12), nullable=False)
    size = db.Column(db.String(18))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def as_dict(self):
        dict = {"username": self.username,
                "scene": self.scene,
                "frames": self.frames,
                "devices": self.devices,
                "size": self.size,
                "date_created": self.date_created
                }
        return dict

    def __init__(self, dict):
        self.username = dict["username"]
        self.scene = dict["scene"]
        self.frames = dict["frames"]
        self.devices = dict["devices"]
        self.size = dict["size"]


@app.route("/")
def index():
    available_routes = extract_routes_from_file("app.py")
    return render_template("index.html", available_routes=available_routes)


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
    return "User: " + username + " blocked"


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


def insert_data(entry):
    try:
        db_entry = Data.query.filter_by(username=entry.username, scene=entry.scene, frames=entry.frames).first()
        if db_entry is not None:
            db.session.delete(db_entry)
            db.session.commit()
        db.session.add(entry)
        db.session.commit()
    except exc.IntegrityError as e:
        print(e.args[0])
        db.session.rollback()


@app.route("/v1/db_create")
def create_db():
    db.create_all()
    return "ok"


@app.route("/v1/db_delete")
def delete_db():
    Data.query.delete()
    db.session.commit()
    return "ok"


if __name__ == "__main__":
    app.debug = True
    app.run()
