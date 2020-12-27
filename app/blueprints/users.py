from flask import Blueprint, request, jsonify
from app.models import User, db

users = Blueprint('users', __name__)


@users.route('/', methods=['POST'])
def create():
    user = User(
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
        address=request.json['address'],
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.json()), 201


@users.route('/', methods=['GET'])
def read_all():
    users = User.query.all()
    return jsonify([user.json() for user in users])


@users.route('/<user_id>', methods=['GET'])
def read_one(user_id):
    user = User.query.get(user_id)
    return jsonify(user.json())


@users.route('/<user_id>', methods=['PUT', 'PATCH'])
def update(user_id):
    user = User.query.get(user_id)
    if request.json.get('first_name'):
        user.first_name = request.json['first_name']
    if request.json.get('last_name'):
        user.last_name = request.json['last_name']
    if request.json.get('address'):
        user.address = request.json['address']
    db.session.commit()
    return jsonify(user.json())


@users.route('/<user_id>', methods=['DELETE'])
def delete(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
