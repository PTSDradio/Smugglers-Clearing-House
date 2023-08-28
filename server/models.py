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
    buyer = db.Column(db.Boolean, default=False)

    items = db.relationship('Item', secondary='user_items', back_populates='users')
    serialize_rules = ('-user_items.users',)

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    listed_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    users = db.relationship('User', secondary='user_items', back_populates='items')
    categories = db.relationship('Category', secondary="item_categories", back_populates="items")
    
    serialize_rules = ('-category.items','-user_item.items')
    
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
    
class User_Item(db.Model, SerializerMixin):
    __tablename__ = "user_items"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    #Stretch goal, have the item listing expire a week from listed date. 
    # current_date = datetime.now()
    # one_week_later = current_date + timedelta(weeks=1)
    # end_date = db.Column(db.DateTime, one_week_later)

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)
    items = db.relationship('Item', secondary="item_categories", back_populates="categories")

    serialize_rules =('-items.categories',)

class ItemCategory(db.Model):
    __tablename__='item_categories'
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'),primary_key=True)


