from flask_pymongo import PyMongo

"""
    Create the database object here. It is initialised in src/__init.py. To
    use it simple import it in the module you wish to use it:

    from .database import mongo

"""

mongo = PyMongo()
