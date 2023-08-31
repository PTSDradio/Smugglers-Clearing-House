from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates 
from sqlalchemy.ext.hybrid import hybrid_property
import datetime

from config import db

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    items = db.relationship('Item',  back_populates='purchaser')
    serialize_rules = ('-items.purchaser',)

class Seller(db.Model, SerializerMixin):
    __tablename__ = 'sellers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    listings = db.relationship('Item', cascade='all, delete', back_populates='seller')
    serialize_rules = ('-listings.seller',)

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

    auction = db.relationship('Auction', cascade='all, delete', back_populates='item', uselist=False)

    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'))
    seller = db.relationship("Seller", cascade='all, delete', back_populates='listings')

    purchaser_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    purchaser = db.relationship("User", cascade='all, delete', back_populates='items')

    categories = db.relationship('Category', secondary="item_categories", cascade='all, delete', back_populates="items")
    
    serialize_rules = ('-categories.items', '-seller.listings', '-auction.item', '-purchaser.items' )
    
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
    item = db.relationship('Item', cascade='all, delete', back_populates='auction')

    top_bid = db.Column(db.Integer, default=0)
    top_bid_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    top_bidder = db.Column(db.String) # might have to make another association table to handle purchasing

    end_time= db.Column(db.String) # if possible handle making timer from this but this it a placeholder for now

    serialize_rules=('-item.auction',)
    
    #Stretch goal, have the item listing expire a week from listed date. 
    # current_date = datetime.now()
    # one_week_later = current_date + timedelta(weeks=1)
    # end_date = db.Column(db.DateTime, one_week_later)

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)
    items = db.relationship('Item', secondary="item_categories", cascade='all, delete', back_populates="categories")

    serialize_rules =('-item.categories',)

class ItemCategory(db.Model, SerializerMixin):
    __tablename__='item_categories'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))