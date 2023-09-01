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
    # for i in range(15):
    #     i = Item(
    #         name = fake.name(),
    #         price = fake.random_int(),
    #         image_url = """https://i.ytimg.com/vi/kPj_IeH6ZZE/maxresdefault.jpg""",
    #         description = fake.text(),
    #         seller_id = rc(seller).id,
    #         # purchaser_id = rc(user).id
    #         #item1(nme= des='')
    #         # listed_by = rc(users).id
    #     )
    #     items.append(i)
    item1 = Item(
        name = "Howl’s Enchanted Jewelry",
        price = 2000,
        image_url = "https://i.etsystatic.com/32899286/r/il/cf9871/4620014758/il_680x540.4620014758_ej9r.jpg",
        description = "Why settle for ordinary when you can own a piece of magic? Howl’s jewelry collection is not just an accessory; it’s an invitation to a world of fantasy and intrigue. Elevate your style to a whole new realm with these captivating earrings; the intricate and ornate design draws the eye, leaving onlookers spellbound. Suitable for any occasion, whether you’re attending a lavish soiree or simply strolling through a hidden garden. They are a must-have for those who appreciate the finer details of life and desire to make a statement wherever they go.",
        seller_id = rc(seller).id
    )
    items.append(item1)
    
    item2 = Item(
        name = "Levistone Pendant",
        price = 50000,
        image_url = "https://i.etsystatic.com/11841135/r/il/802dfd/4368597671/il_1588xN.4368597671_ez4m.jpg",
        description = "Unlock the secrets of a forgotten world with the Levistone, the Pendant of Laputa, this remarkable jewelry piece is not just an accessory; it’s a connection to a realm of magic and adventure. While wearing it, you’ll feel the presence of Laputa and its rich history, as if you’re embarking on your own skyborne adventure. The Levistone Pendant complements a wide range of styles, from casual to formal. Limited availability makes this the perfect addition to any collection.",
        seller_id = rc(seller).id
    )
    items.append(item2)

    item3 = Item(
        name = "LightSaber",
        price = 75000,
        image_url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c220b922-e1a5-499e-8a11-d6d8df8d6c4a/da7xp1e-1a4102f7-3cf4-4b44-a7e4-1e5cec9c0222.png/v1/fill/w_1024,h_615,q_80,strp/green_tri_blade_lightsaber_by_chingoryu_da7xp1e-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjE1IiwicGF0aCI6IlwvZlwvYzIyMGI5MjItZTFhNS00OTllLThhMTEtZDZkOGRmOGQ2YzRhXC9kYTd4cDFlLTFhNDEwMmY3LTNjZjQtNGI0NC1hN2U0LTFlNWNlYzljMDIyMi5wbmciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.HpZl8Nh5S2m5KcOKSWVm-pUC6wSBbrxXrCC6KxlIREg ",
        description = "Are you ready to step into a galaxy far, far away and become a hero of epic proportions? When you wield a lightsaber, you’re not just holding a weapon; you’re harnessing the power of the Force itself. It’s a symbol of hope, courage, and the eternal battle between light and dark. Don’t miss your opportunity to join the ranks of famous Jedis and Sith Lords!",
        seller_id = rc(seller).id
    )
    items.append(item3)

    item4 = Item(
        name = "One Ring to Rule Them All",
        price = 250000,
        image_url = "https://files.cults3d.com/uploaders/14073265/illustration-file/2204685a-9fdc-45a0-acc5-e2ee2c651949/prev.jpg",
        description = "Prepare to embark on an epic journey that will shape the fate of Middle earth itself with the One Ring, the most powerful and iconic artifact in the realm of fantasy. This isn’t just any piece of jewelry; it’s a piece of history, a vessel of power, and a ticket to adventure. Crafted in the fires of Mount Doom, the One Ring holds immeasurable power. With it, you can command the armies of Mordor and bend the will of others to your desires. Embrace the dark side or resist its corrupting influence- the choice is yours. Are you up to the challenge?",
        seller_id = rc(seller).id
    )
    items.append(item4)

    item5 = Item(
        name = "Lamp of Wonders",
        price = 85000,
        image_url = "https://tools.toywiz.com/_images/_webp/_products/lg/disaladdinlamprep.webp",
        description = "Unleash the enchantment of a thousand and one nights with the Lamp of Wonders. This isn’t just a lamp; it’s a gateway to a world of limitless possibilities and extraordinary adventures. Its ancient Arabian design evokes the mystique and charm of Agrabah, making it a captivating addition to any decor.",
        seller_id = rc(seller).id
    )
    items.append(item5)

    item6 = Item(
        name = "Howl’s Moving Castle",
        price = 15000000,
        image_url = "https://i.guim.co.uk/img/media/18e0b02b77238d312812c835c23144cc63baa86a/0_0_923_554/master/923.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=c640a0f676e4a724c16e15624f4686a0",
        description = "Step into a world where magic reigns supreme with the opportunity to own Howl’s Moving Castle, a masterpiece of fantasy and wonder. This isn’t just a castle; it’s a mobile fortress that brings your dreams of adventure and enchantment to life.",
        seller_id = rc(seller).id
    )
    items.append(item6)

    item7 = Item(
        name = "Dagger of Time",
        price = 150000,
        image_url = "https://static.wikia.nocookie.net/princeofpersia/images/7/7e/Dagger-of-time-1549.jpg/revision/latest?cb=20110330063618&path-prefix=en",
        description = "Prepare to step into the shoes of a legendary hero with the Dagger of Time, a relic of unimaginable power. This isn’t just a dagger; it’s a key to rewriting history, defying fate, and embarking on epic quests. The Dagger of Time is imbued with the incredible ability to manipulate time. With a simple press of the button, you can rewind and manipulate time, correcting mistakes, and overcoming impossible obstacles. ",
        seller_id = rc(seller).id
    )
    items.append(item7)

    item8 = Item(
        name = "The Elder Wand",
        price = 190000,
        image_url = "https://img1.cgtrader.com/items/2704987/8738ed65de/large/harry-potter-elders-wand-3d-model-3d-model-low-poly-obj-3ds-fbx-blend.jpg",
        description = "Unleash the unparalleled power of the Elder Wand, the most coveted and formidable magical artifact in the wizarding world. This isn’t just a wand; it’s a symbol of unparalleled strength, a connection to wizarding history, and the ultimate toll for mastering magic. The Elder Wand comes with a rich and storied history, having passed through the hands of legendary wizards and witches throughout the ages.",
        seller_id = rc(seller).id
    )
    items.append(item8)
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