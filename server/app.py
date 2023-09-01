#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, jsonify, session
from flask_restful import Resource
from sqlalchemy_serializer import SerializerMixin



# Local imports
from config import app, db, api
# Add your model imports
from models import User, Item, Auction, ItemCategory, Category, Seller

app.secret_key = 'BAD_SECRET_KEY'
# Views go here!

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

class Users(Resource):
    def get(self):
        q = [ user.to_dict(rules=()) for user in User.query.all()]
        response = make_response(q, 200)
        return response 
    
    def post(self):
        data = request.get_json()

        new_user = User(username=data['username'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 200)

class UserById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if user is None:
            return make_response({"error": "User not found"}, 404)
        return make_response(user.to_dict(), 200)
    
    # def patch(self, id):
    #     user = User.query.filter(User.id == id).first()
    #     if user is None:
    #         return make_response({"error": "User not found"}, 404)
    #     try:
    #         data = request.get_json()
    #         for attr in data:
    #             setattr(user, attr, data[attr])
    #         db.session.add(user)
    #         db.session.commit()
    #         response = make_response(user.to_dict(), 202)
    #         return response
    #     except ValueError as er:
    #         resp = make_response({"errors": [str(er)]},400)
    #         return resp
    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if user is None:
            return make_response({"error": "User not found"}, 404)
        db.session.delete(user)
        db.session.commit()
        return make_response("", 204)

class Sellers(Resource):
    def get(self):
        q = [ user.to_dict() for user in Seller.query.all()]
        response = make_response(q, 200)
        return response 
    
    def post(self):
        data = request.get_json()

        new_user = Seller(username=data['username'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 200)
    
class SellerById(Resource):
    def get(self, id):
        user = Seller.query.filter(Seller.id == id).first()
        if user is None:
            return make_response({"error": "Seller not found"}, 404)
        return make_response(user.to_dict(), 200)
    
    # def patch(self, id):
    #     user = User.query.filter(User.id == id).first()
    #     if user is None:
    #         return make_response({"error": "User not found"}, 404)
    #     try:
    #         data = request.get_json()
    #         for attr in data:
    #             setattr(user, attr, data[attr])
    #         db.session.add(user)
    #         db.session.commit()
    #         response = make_response(user.to_dict(), 202)
    #         return response
    #     except ValueError as er:
    #         resp = make_response({"errors": [str(er)]},400)
    #         return resp
    def delete(self, id):
        user = Seller.query.filter(Seller.id == id).first()
        if user is None:
            return make_response({"error": "Seller not found"}, 404)
        db.session.delete(user)
        db.session.commit()
        return make_response("", 204)

class Auctions(Resource):
    def get(self):
        q = [auction.to_dict() for auction in Auction.query.all()]
        response = make_response(q, 200)
        return response 

    def post(self):
        data = request.get_json()

        new_auction = Auction(item_id=data['item_id'], end_time=data['end_time'])
        db.session.add(new_auction)
        db.session.commit()
        return make_response(new_auction.to_dict(), 200)
    
class AuctionById(Resource):
    def get(self, id):
        auction = Auction.query.filter(Auction.id == id).first()
        if auction is None:
            return make_response({"error": "auction not found"}, 404)
        return make_response(auction.to_dict(), 200)
    
    def patch(self, id):
        auction = Auction.query.filter(Auction.id == id).first()
        if auction is None:
            return make_response({"error": "auction not found"}, 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(auction, attr, data[attr])
            db.session.add(auction)
            db.session.commit()
            response = make_response(auction.to_dict(), 202)
            return response
        except ValueError as er:
            resp = make_response({"errors": [str(er)]},400)
            return resp

    def delete(self, id):
        auction = Auction.query.filter(Auction.id == id).first()
        if auction is None:
            return make_response({"error": "auction not found"}, 404)
        db.session.delete(auction)
        db.session.commit()
        return make_response("", 204)
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

class CatById(Resource):
     def get(self, id):
        user = Category.query.filter(Category.id == id).first()
        if user is None:
            return make_response({"error": "Category not found"}, 404)
        return make_response(user.to_dict(), 200)
    
class Items(Resource):
    def get(self): 
        items = [item.to_dict() for item in Item.query.all()]
        return make_response(items, 200)
    
    def post(self): 
        try: 
            data = request.get_json() 
            new_item = Item(
                name = data['name'],
                price = data['price'],
                description = data['description'],
                seller_id=data['seller_id']
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

class ItemCategories(Resource):
    def get(self):
        q = [ user.to_dict() for user in ItemCategory.query.all()]
        response = make_response(q, 200)
        return response 
    
    def post(self):
        data = request.get_json()

        new_user = ItemCategory(category_id=data['category_id'], item_id=data['item_id'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 200)
    
class ICById(Resource):
    def delete(self, id): 
        item = ItemCategory.query.filter(ItemCategory.id == id).one_or_none()
        if item is None: 
            return make_response({"Error":"Item-category relation not found"}, 404)
        db.session.delete(item)
        db.session.commit()
        return make_response({}, 204)

class Login(Resource):
    def post(self):
        data = request.get_json()
        user_type = data["user_type"]
        username = data["username"]
        password = data["password"]

        if user_type == "buyer":
            user = User.query.filter(User.username == username).first()

            if user and user.password == password:
                session['user_id']= user.id
                session['user_type']= user_type
                return make_response(user.to_dict(), 200)
            return make_response({'error': 'invalid password'}, 401)
        elif user_type == "seller":
            seller = Seller.query.filter(Seller.username == username).first()

            if seller and seller.password == password:
                session['user_id']= seller.id
                session['user_type']= user_type
                return make_response(user.to_dict(), 200)
            return make_response({'error': 'invalid password'}, 401)
        return make_response({'error': '401 Unauthorized'}, 401)
    
class Register(Resource):
    def post(self):
        data = request.get_json()
        user_type = data["user_type"]
        username = data["username"]
        password = data["password"]
        if user_type == "buyer":
            new_user = User(username=data['username'], password=data['password'])
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 200)
        elif user_type == "seller":
            new_user = Seller(username=data['username'], password=data['password'])
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 200)
        return make_response("problemo", 200)

class Logout(Resource):
    def delete(self):
        if session['user_id'] and session['user_type']:
            session['user_id']= None
            session['user_type']= None
            return make_response({'message': '200: Successfully cleared session data'}, 200)
        else:
            return make_response({'error': "you're not logged in silly"}, 404)


            
api.add_resource(ItemCategories, '/item-category-relations')

api.add_resource(Categories, '/categories')
api.add_resource(CatById, '/categories/<int:id>')
api.add_resource(Items, '/items')
api.add_resource(ItemsById, '/items/<int:id>')

api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<int:id>')

api.add_resource(Sellers, '/sellers')
api.add_resource(SellerById, '/sellers/<int:id>')

api.add_resource(Auctions, '/auctions')
api.add_resource(AuctionById, '/auctions/<int:id>')


api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(Logout, '/logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)