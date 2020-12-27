from flask import Blueprint, request, jsonify
from app.models import User, db
users = Blueprint('users', __name__)


@users.route('/', methods=['POST'])
def create():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    address = request.json['address']

    new_user = User(first_name=first_name, last_name=last_name, address=address)
    db.session.add(new_user)
    db.session.commit()

    return 'new user was created'


@users.route('/', methods=['GET'])
def read_all():
    all_users = db.session.query(User).all()
    return jsonify([user.serialize for user in all_users])


@users.route('/<user_id>', methods=['GET'])
def read_one(user_id):
    user = db.session.query(User).get(user_id)
    return user.serialize


@users.route('/<user_id>', methods=['PUT'])
def update(user_id):
    if request.json.get('first_name'):
        first_name = request.json['first_name']
        db.session.query(User).filter(User.id == user_id).update(
            {User.first_name: first_name}, synchronize_session=False)
    if request.json.get('last_name'):
        last_name = request.json['last_name']
        db.session.query(User).filter(User.id == user_id).update(
            {User.last_name: last_name}, synchronize_session=False)
    if request.json.get('address'):
        address = request.json['address']
        db.session.query(User).filter(User.id == user_id).update(
            {User.address: address}, synchronize_session=False)
    db.session.commit()
    return f'User {user_id} was updated with next data {request.json}'


@users.route('/<user_id>', methods=['DELETE'])
def delete(user_id):
    user = db.session.query(User).get(user_id)
    db.session.delete(user)
    db.session.commit()

    return f'User with id {user_id} was deleted'
