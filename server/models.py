from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates 
import datetime

from config import db

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    items = db.relationship('Item',  back_populates='purchaser')
    serialize_rules = ('-item.purchaser',)

class Seller(db.Model, SerializerMixin):
    __tablename__ = 'sellers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    items = db.relationship('Item', back_populates='seller')
    serialize_rules = ('-item.seller',)

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_url = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    is_purchased = db.Column(db.Boolean, default=False)

    auction = db.relationship('Auction', back_populates='item', uselist=False)

    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'))
    seller = db.relationship("Seller", back_populates='items')

    purchaser_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    purchaser = db.relationship("User", back_populates='items')

    categories = db.relationship('Category', secondary="item_categories", back_populates="items")
    
    serialize_rules = ('-category.items','-user.items', '-seller.items', '-auction.item' )
    
    @validates('price')
    def validate_price(self, key, price): 
        if price <= 0: 
            raise ValueError('Price must be a positive number.')
        return price 
    
    @validates('name')
    def validate_name(self, key, name):
        if name is None or len(name) <= 0:
            raise ValueError("Item must have a name.")
        return name 
    
class Auction(db.Model, SerializerMixin):
    __tablename__ = "auctions"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item = db.relationship('Item', back_populates='auction')

    top_bid = db.Column(db.Integer)
    top_bid_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    top_bidder = db.Column(db.String) # might have to make another association table to handle purchasing

    end_time= db.Column(db.String) # if possible handle making timer from this but this it a placeholder for now


    
    #Stretch goal, have the item listing expire a week from listed date. 
    # current_date = datetime.now()
    # one_week_later = current_date + timedelta(weeks=1)
    # end_date = db.Column(db.DateTime, one_week_later)

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)
    items = db.relationship('Item', secondary="item_categories", back_populates="categories")

    serialize_rules =('-item.categories',)

class ItemCategory(db.Model):
    __tablename__='item_categories'
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'),primary_key=True)


