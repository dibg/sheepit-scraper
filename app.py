from datetime import datetime
from flask import Flask, jsonify, render_template
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy
from configuration.credentials import POSTGRESQL_URI
from scraper.common_session_tasks import scrape_current_data, load_stored_data, get_valid_login_session
from helper_functions.storage import store_as_json, retrieve_json


app = Flask(__name__)
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


@app.route("/")  # SearchMe
def index():
    return render_template("index.html")


@app.route("/v1/snapshot")
def single_data_snapshot():
    session = get_valid_login_session()
    current_data = scrape_current_data(session)
    return jsonify(current_data)


@app.route("/v1/db_data")
def query_data():
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
    data = load_stored_data()
    for x in data:
        a = Data()
        a.username = x["username"]
        a.scene = x["scene"]
        a.frames = x["frames"]
        a.devices = x["devices"]
        a.size = x["size"]
        try:
            b = Data.query.filter_by(username=a.username, scene=a.scene, frames=a.frames).first()
            if b is not None:
                db.session.delete(b)
                db.session.commit()
            db.session.add(a)
            db.session.commit()
        except exc.IntegrityError as e:
            print(e.args[0])
            db.session.rollback()
    return "ok"


@app.route("/v1/db_create")
def create_db():
    db.create_all()
    return "ok"


if __name__ == "__main__":
    app.debug = True
    app.run()
