from flask import jsonify, request, Blueprint
from extensions import db
from middlewares.jwt_verification import token_required
from models.user_model import User

users_crud = Blueprint('users_crud', __name__)


@users_crud.route('/users', methods=['GET'])
@token_required
def get_users():
    users = User.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})


@users_crud.route('/users/<string:username>', methods=['GET'])
@token_required
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user.to_dict())


@users_crud.route('/users', methods=['POST'])
@token_required
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(password=data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'user': new_user.to_dict()}), 201


@users_crud.route('/users/<int:user_id>', methods=['PUT'])
@token_required
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    user = User(username=data['username'], email=data['email'])
    user.set_password(password=data['password'])

    db.session.commit()
    return jsonify(user.to_dict())


@users_crud.route('/users/<int:user_id>', methods=['DELETE'])
@token_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'result': True})
