from app.config.database import db
from app.utils.collections import Collection
from app.users.schemas import UserIn

users_collection = db[Collection.USERS]


def create_user(user_data: UserIn):
    new_user = users_collection.insert_one(user_data.model_dump())
    return users_collection.find_one({"_id": new_user.inserted_id})


def get_users():
    return list(users_collection.find())
