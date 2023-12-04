from flask import jsonify, request, Blueprint
import jwt
import datetime
from flask_login import login_user
from login.user_model import User

login_controller = Blueprint('login_controller', __name__)
SECRET_KEY = 'Cyce123' 

@login_controller.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')
        print(token)
        return jsonify({'status': 'success', 'token': token}), 200
    return {'status': 'failed', 'message': 'Invalid credentials'}, 401