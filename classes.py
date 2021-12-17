from flask_restful import Resource
from read_data import MOVIES, LINKS, TAGS, RATINGS

class Welcome(Resource):
    """
    Class used for displaying welcome message.
    """
    def get(self):
        return "Welcome to main page. Try /movies, /links, /tags or /ratings endpoint!"

class MoviesList(Resource):
    """
    Class used for displaying movies list.
    """
    def get(self):
        return MOVIES

class LinksList(Resource):
    """
    Class used for displaying links list.
    """
    def get(self):
        return LINKS

class TagsList(Resource):
    """
    Class used for displaying tags list.
    """
    def get(self):
        return TAGS

class RatingsList(Resource):
    """
    Class used for displaying tags list.
    """
    def get(self):
        return RATINGS