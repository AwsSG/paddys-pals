import os
from dotenv import load_dotenv
from flask import Flask
from flask_googlemaps import GoogleMaps

from .routes import routes

""" Create and initialise the app object """
load_dotenv()
app = Flask(__name__)
app.register_blueprint(routes)
app.config['GOOGLEMAPS_KEY'] = os.getenv('GOOGLE_API_KEY')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
GoogleMaps(app)


""" App will be available when imported """
