from flask import Blueprint, render_template
from .database import mongo
from .map_functionality import generate_map

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    generate_map()
    # parties = mongo.db.parties.find()
    return render_template('main.html')


@routes.route('/map')
def map():
    return render_template('map.html')
