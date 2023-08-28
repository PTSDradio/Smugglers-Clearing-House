#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, jsonify, request
from flask_restful import Resource
from sqlalchemy_serializer import SerializerMixin



# Local imports
from config import app, db, api
# Add your model imports
from models import User, Item, User_Item, ItemCategory, Category

# Views go here!

@app.route('/')
def index():

    return '<h1>Phase 4 Project Server</h1>'

class Categories(Resource):
    def get (self):
        q = [ cat.to_dict(rules=('items',)) for cat in Category.query.all()]
        # q = Category.query.filter(Category.id == 1).first()
        response = make_response(q, 200)
        return response

api.add_resource(Categories, '/categories')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

