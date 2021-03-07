import os
from flask import Flask, Blueprint, render_template
from bson.objectid import ObjectId
from .database import mongo

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    parties = mongo.db.parties.find()
    print(parties.count())
    return render_template('main.html', parties=parties)
