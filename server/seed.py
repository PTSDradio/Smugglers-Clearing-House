#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Item, Auction, Category, ItemCategory, Seller, ItemCategory

fake = Faker()

def create_items(seller, user):
    items = []
    for i in range(15):
        i = Item(
            name = fake.name(),
            price = fake.random_int(),
            image_url = """https://i.ytimg.com/vi/kPj_IeH6ZZE/maxresdefault.jpg""",
            description = fake.text(),
            seller_id = rc(seller).id,
            # purchaser_id = rc(user).id

            # listed_by = rc(users).id
        )
        items.append(i)
    return items 

def create_users():
    users = []
    for i in range(5):
        u = User(username = fake.name(),
                 password = fake.password()

        )
        users.append(u)
    return users

def create_sellers():
    users = []
    for i in range(5):
        u = Seller(username = fake.name(),
                   password = fake.password()
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
    categories = ['art', 'furniture', 'clothes', 'jelewry', 'contraband']
    li = []
    for c in categories:
        cats = Category(category_name=c)
        
        li.append(cats)
    return li 

def CatItem(items, categories):
    li = []
    for i in range(5):
        ic = ItemCategory(category_id=rc(categories).id, item_id=rc(items).id)
       
        li.append(ic) 
        print("done")
    return li


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
        items = create_items(sellers, users)
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

        print("seeding item cat relationships")
        ic = CatItem(items, categories)
        db.session.add_all(ic)
        db.session.commit()