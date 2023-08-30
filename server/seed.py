#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Item, Auction, Category, ItemCategory, Seller, ItemCategory

fake = Faker()

def create_items(seller):
    items = []
    for i in range(15):
        i = Item(
            name = fake.name(),
            price = fake.random_int(),
            image_url = """https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fdwayne-the-rock-pikmin-v0-sv7qo7tsgt2b1.jpg%3Fwidth%3D640%26crop%3Dsmart%26auto%3Dwebp%26s%3Da14114a054fc999abee8eef130e66e9b26ddfa1c""",
            description = fake.text(),
            seller_id = rc(seller).id,


            # listed_by = rc(users).id
        )
        items.append(i)
    return items 

def create_users():
    users = []
    for i in range(5):
        u = User(name = fake.name(),

        )
        users.append(u)
    return users

def create_sellers():
    users = []
    for i in range(5):
        u = Seller(name = fake.name(),
        )
        users.append(u)
    return users

def create_bids(items, users):
    bids = []
    for i in range(5):
        b = Auction(item_id = rc(items).id, end_time=fake.name(), top_bid_id = rc(users).id)
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
        Seller.query.delete() 
        Auction.query.delete()
        Category.query.delete()
        ItemCategory.query.delete()
        
        print("seeding sellers")
        sellers = create_sellers()
        db.session.add_all(sellers)
        db.session.commit()


        print("seeding users")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding items")
        items = create_items(users)
        db.session.add_all(items)
        db.session.commit() 

        print("seeding bids")
        bids = create_bids(items, users)
        db.session.add_all(bids)
        db.session.commit()
        
        print("seeding categories")
        categories = create_category(items)
        db.session.add_all(categories)
        db.session.commit()