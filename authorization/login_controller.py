from flask import jsonify, request, Blueprint
import jwt
import datetime
from flask_login import login_user
from authorization.user_model import User
SECRET_KEY = "12345"
login_controller = Blueprint('login_controller', __name__)


@login_controller.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'status': 'failed', 'message': 'Invalid credentials'}), 401

    try:
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, SECRET_KEY, algorithm='HS256')
            print(token)
            return jsonify({'status': 'success', 'token': token}), 200
    except Exception as e:
        print(f"Error encoding JWT: {e}")
        return jsonify({'status': 'failed', 'message': 'Internal server error'}), 500
    return {'status': 'failed', 'message': 'Invalid credentials'}, 401
