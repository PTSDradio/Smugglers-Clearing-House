from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates 
import datetime

from config import db

# Models go here!

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    buyer = db.Column(db.Boolean, default=False)

    # bids = db.relationship('Marketplace', backref='seller')


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    categories = db.relationship('Category', secondary="item_categories", back_populates="items")
    
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
    
class Bid(db.Model):
    __tablename__ = "bids"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # current_date = datetime.now()
    # one_week_later = current_date + timedelta(weeks=1)
    #Stretch-goal: end_date = db.Column(db.DateTime, one_week_later)

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)
    items = db.relationship('Item', secondary="item_categories", back_populates="categories")

class ItemCategory(db.Model):
    __tablename__='item_categories'
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'),primary_key=True)


