from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash
from .database import mongo

class Party:
    """ Object to represent user created parties. Contains all information
        related to the party and allows us to easily display it to the user
        or update the database via getters / setters.
    """

    def __init__(self, _id, longitude, latitude, start_time, end_time, video_link,
            party_password, description, name="St Patrick Party!"):

        self._id = ObjectId(_id)
        self._name = name
        self._longitude = longitude
        self._latitude = latitude
        self._start_time = start_time
        # Todo: workout time the party needs to be removed.
        self._end_time = end_time
        self._video_link = video_link
        self._party_password = party_password
        self._description = description
        #Used to select the correct database record
        self._filter = {'_id': self._id}

    @property
    def name(self):
        return self._name

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def video_link(self):
        return self._video_link

    @property
    def party_password(self):
        return self._party_password

    @property
    def description(self):
        return self._description

    @description.setter
    def description (self,value):
        self.description = value
        mongo.db.parties.update_one(self._filter, {"$set": { "description": value }})

    @name.setter
    def name(self,value):
        self._name = value
        mongo.db.parties.update_one(self._filter, {"$set": { "name": value }})

    @longitude.setter
    def longitude(self, value):
        self.longitutde = value
        mongo.db.parties.update_one(self._filter, {"$set": { "long": value }})

    @latitude.setter
    def latitude(self,value):
        self.latitude = value
        mongo.db.parties.update_one(self._filter, {"$set": { "lat": value }})

    @start_time.setter
    def start_time(self,value):
        self.start_time = value
        mongo.db.parties.update_one(self._filter, {"$set": { "start_time": value }})

    @end_time.setter
    def end_time(self,value):
        self.end_time = value
        mongo.db.parties.update_one(self._filter, {"$set": { "end_time": value }})

    @video_link.setter
    def video_link(self,value):
        self.video_link = value
        mongo.db.parties.update_one(self._filter, {"$set": { "video_link": value }})

    @party_password.setter
    def party_password(self,value):
        #TODO: Take a password and confirm password from user and check they match first.
        mongo.db.parties.update_one(self._filter, {"$set": { "password": generate_password_hash( value ) }})

