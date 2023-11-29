from flask import jsonify, request, Blueprint
from login.user_model import User
from extensions import db


register_controller = Blueprint('register_controller', __name__)


@register_controller.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'Username already exists'}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201