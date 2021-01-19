from flask import Flask
from configuration.credentials import POSTGRESQL_URI


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRESQL_URI
