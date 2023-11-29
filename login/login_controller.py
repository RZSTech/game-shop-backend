from flask import jsonify, request, Blueprint
from flask_login import login_user
from login.user_model import User

login_controller = Blueprint('login_controller', __name__)


@login_controller.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return {'status': 'success'}, 200
    return {'status': 'failed', 'message': 'Invalid credentials'}, 401
