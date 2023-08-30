#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, jsonify, request
from flask_restful import Resource
from sqlalchemy_serializer import SerializerMixin



# Local imports
from config import app, db, api
# Add your model imports
from models import User, Item, Auction, ItemCategory, Category

# Views go here!

@app.route('/')
def index():

    return '<h1>Phase 4 Project Server</h1>'

class Users(Resource):
    def get(self):
        q = [ user.to_dict() for user in User.query.all()]
        response = make_response(q, 200)
        return response 
    
    def post(self):
        data = request.get_json()

        new_user = User(name=data['name'], buyer=data['buyer'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 200)

class UserById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if user is None:
            return make_response({"error": "User not found"}, 404)
        return make_response(user.to_dict(), 200)
    
    def patch(self, id):
        user = User.query.filter(User.id == id).first()
        if user is None:
            return make_response({"error": "User not found"}, 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(user, attr, data[attr])
            db.session.add(user)
            db.session.commit()
            response = make_response(user.to_dict(), 202)
            return response
        except ValueError as er:
            resp = make_response({"errors": [str(er)]},400)
            return resp

class UserItems(Resource):
    def get(self):
        q = [ user.to_dict() for user in Auction.query.all()]
        response = make_response(q, 200)
        return response 
    
    def post(self):
        try:
            data= request.get_json()
            new_rel = Auction(item_id=data["item_id"], buyer_id=data["buyer_id"],
                                 listed_by=data["listed_by"])
            db.session.add(new_rel)
            db.session.commit()
            return make_response(new_rel.to_dict(), 200)
        except:pass
        pass

# class UserItemById(Resource):
#     def post(self, user_id):
#         try:
#             data= request.get_json()
#             new_rel = Auction()
#         except:pass
#         pass

class Categories(Resource):
    def get (self):
        q = [ cat.to_dict() for cat in Category.query.all()]
        response = make_response(q, 200)
        return response
    
    def post(self):
        data= request.get_json()

        new_cat = Category(category_name= data['category_name'])
        db.session.add(new_cat)
        db.session.commit()
        return make_response(new_cat.to_dict(), 200)   
    
class Items(Resource):
    def get(self): 
        items = [item.to_dict(rules=('-users','-categories.items')) for item in Item.query.all()]
        return make_response(items, 200)
    
    def post(self): 
        try: 
            data = request.get_json() 
            new_item = Item(
                name = data['name'],
                price = data['price'],
                description = data['description']
            )
            db.session.add(new_item)
            db.session.commit()
            return make_response(new_item.to_dict(rules=('-users','-categories.items')), 200)
        except ValueError: 
            return make_response({"Error":["Invalid item inputs"]}, 400)

class ItemsById(Resource): 
    def get(self, id): 
        item = Item.query.filter(Item.id == id).one_or_none()
        if item is None: 
            return make_response({"Error":"Item not found"}, 404)
        return make_response(item.to_dict(rules=('-users',)), 200)
    
    def patch(self, id):
        item = Item.query.filter(Item.id == id).first()
        if item is None:
            return make_response({"error": "Item not found"}, 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(item, attr, data[attr])
            db.session.add(item)
            db.session.commit()
            response = make_response(item.to_dict(), 202)
            return response
        except ValueError as er:
            resp = make_response({"errors": [str(er)]},400)
            return resp


    def delete(self, id): 
        item = Item.query.filter(Item.id == id).one_or_none()
        if item is None: 
            return make_response({"Error":"Item not found"}, 404)
        db.session.delete(item)
        db.session.commit()
        return make_response({}, 204)



api.add_resource(Categories, '/categories')
api.add_resource(Items, '/items')
api.add_resource(ItemsById, '/items/<int:id>')
api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<int:id>')
api.add_resource(UserItems, '/users/relationships')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

