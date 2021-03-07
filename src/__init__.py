import os
from dotenv import load_dotenv
from flask import Flask
from .database import mongo

from .routes import routes

""" Create and initialise the app object """
load_dotenv()
app = Flask(__name__)
app.register_blueprint(routes)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# Initialise the db object here
mongo.init_app(app)

""" App will be available when imported """
