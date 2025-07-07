from app.config.database import db
from app.utils.collections import Collection
from bson.objectid import ObjectId

users_collection = db[Collection.USERS]


def create_user():
    user_data = {
        "username": "obrunodev",
        "email": "Brunorpdev@gmail.com",
        "password": "senha123",
    }
    new_user = users_collection.insert_one(user_data)
    return users_collection.find_one({"_id": new_user.inserted_id})


def get_user(user_id: str):
    return users_collection.find_one({"_id": ObjectId(user_id)})


def get_all_users():
    return list(users_collection.find())
