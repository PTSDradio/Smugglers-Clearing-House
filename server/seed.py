#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Item, Bid, Category, ItemCategory

fake = Faker()

def create_items():
    items = []
    for i in range(15):
        i = Item(
            name = fake.name(),
            price = fake.random_int(),
            description = fake.text(),            
        )
        items.append(i)
    return items 

def create_users():
    users = []
    for i in range(5):
        u = User(name = fake.name(),
                 buyer = fake.boolean()
        )
        users.append(u)
    return users

def create_bids(items, users):
    bids = []
    for i in range(5):
        b = Bid(item_id = rc(items).id,
                 seller_id = rc(users).id)
        bids.append(b)
    return bids

def create_category(items):
    categories = ['Furniture', 'Sporting goods', 'Jewelry', 'Weapons', 'Questionables']
    li = []
    for c in categories:
        cats = Category(category_name=c)
        cats.items.append(rc(items))
        li.append(cats)
    return li 

# def append_cat_to_items(items, categories):
#     for item in items:
#         item.categories.append(rc(categories))
#     return items

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Item.query.delete() 
        User.query.delete() 
        Bid.query.delete()
        Category.query.delete()
        ItemCategory.query.delete()
        
        print("Seeding items")
        items = create_items()
        db.session.add_all(items)
        db.session.commit() 


        print("seeding users")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("seeding bids")
        bids = create_bids(items, users)
        db.session.add_all(bids)
        db.session.commit()
        
        print("seeding categories")
        categories = create_category(items)
        db.session.add_all(categories)
        db.session.commit()

