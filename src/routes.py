from flask import Blueprint, render_template
from bson.objectid import ObjectId
from .database import mongo
from .map_functionality import generate_map, get_parties

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    generate_map()
    parties = get_parties()
    return render_template('main.html',parties=parties)


@routes.route('/map')
def map():
    return render_template('map.html')

@routes.route('/test_data')
def add_parties():
    mongo.db.parties.drop()
    mongo.db.parties.insert_many(
            [
                {'_id':ObjectId(),
                    'name': "Dublin Party",
                    'long': "-6.266155",
                    'lat': "53.350140",
                    'start_time': "2:00pm",
                    'end_time': "3:00pm",
                    'video_link': "test.com",
                    'party_password': "pass",
                    'description': "Party in dublin",
                },
                {'_id':ObjectId(),
                    'name': "Manchester Party",
                    'long': "-2.242631",
                    'lat': "53.480759",
                    'start_time': "2:00pm",
                    'end_time': "3:00pm",
                    'video_link': "test.com",
                    'party_password': "pass",
                    'description': "Party in Manchester",
                },
                {'_id':ObjectId(),
                    'name': "London Party",
                    'long': "-0.127758",
                    'lat': "51.507351",
                    'start_time': "2:00pm",
                    'end_time': "3:00pm",
                    'video_link': "test.com",
                    'party_password': "pass",
                    'description': "Party in dublin",
                },
            ])
    return "Added"
