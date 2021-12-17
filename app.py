from flask import Flask
from flask_restful import Api
from classes import Welcome, MoviesList, LinksList, TagsList, RatingsList

app = Flask("MoviesAPI")
api = Api(app)

api.add_resource(Welcome, '/')
api.add_resource(MoviesList, '/movies')
api.add_resource(LinksList, '/links')
api.add_resource(TagsList, '/tags')
api.add_resource(RatingsList, '/ratings')

if __name__ == '__main__':
    app.run(debug=True)
