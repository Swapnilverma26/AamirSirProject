from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

mongo = PyMongo()

class User:
    @staticmethod
    def create_user(username, email, password):
        password_hash = generate_password_hash(password)
        return mongo.db.users.insert_one({
            "username": username,
            "email": email,
            "password": password_hash
        })

    @staticmethod
    def get_user_by_email(email):
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def verify_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)
