from flask import Blueprint, render_template, request, redirect, url_for
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

@routes.route('/add_party', methods=['POST'])
def add_party():
    if (request.json['name'] and
    request.json['longitude'] and
    request.json['latitude'] and
    request.json['start_time'] and
    request.json['end_time'] and
    request.json['video_link'] and
    request.json['party_password'] and
    request.json['description']):
        mongo.db.parties.insert_one({
            'name': request.json['name'],
            'longitude': request.json['longitude'],
            'latitude': request.json['latitude'],
            'start_time': request.json['start_time'],
            'end_time': request.json['end_time'],
            'video_link': request.json['video_link'],
            'party_password': request.json['party_password'],
            'description': request.json['description'],
            })
    return redirect('/')

@routes.route('/test_data')
def add_parties():
    mongo.db.parties.drop()
    mongo.db.parties.insert_many(
            [
                {'_id':ObjectId(),
                    'name': "Dublin Party",
                    'longitude': "-6.266155",
                    'latitude': "53.350140",
                    'start_time': "2:00pm",
                    'end_time': "3:00pm",
                    'video_link': "test.com",
                    'party_password': "pass",
                    'description': "Party in dublin",
                },
                {'_id':ObjectId(),
                    'name': "Manchester Party",
                    'longitude': "-2.242631",
                    'latitude': "53.480759",
                    'start_time': "2:00pm",
                    'end_time': "3:00pm",
                    'video_link': "test.com",
                    'party_password': "pass",
                    'description': "Party in Manchester",
                },
                {'_id':ObjectId(),
                    'name': "London Party",
                    'longitude': "-0.127758",
                    'latitude': "51.507351",
                    'start_time': "2:00pm",
                    'end_time': "3:00pm",
                    'video_link': "test.com",
                    'party_password': "pass",
                    'description': "Party in dublin",
                },
            ])
    return "Added"
