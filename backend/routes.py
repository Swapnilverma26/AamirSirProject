from flask import Blueprint, jsonify, request
from models import User


main = Blueprint('main', __name__)

@main.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    User.create_user(username, email, password)
    return jsonify({'message': 'User registered successfully!'}), 201

@main.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User.get_user_by_email(email)
    if user and User.verify_password(user['password'], password):
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Login failed. Check your credentials.'}), 401
