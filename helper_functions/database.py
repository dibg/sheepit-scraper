from flask_init import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from datetime import datetime

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
