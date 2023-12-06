from flask import request, jsonify
import jwt
from jwt import ExpiredSignatureError
from functools import wraps
from authorization.user_model import User

SECRET_KEY = "12345"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', type=str)
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            token = token.replace('Bearer ', '', 1)
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = User.query.get(data['user_id'])
            if current_user is None:
                return jsonify({'message': 'User does not exist!'}), 404
        except jwt.exceptions.DecodeError:
            return jsonify({'message': 'Token is invalid!'}), 403
        except ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
