from flask import Flask
from extensions import db
from flask_cors import CORS
from login.flask_login import init_login_manager
from blueprints import run_blueprints

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.secret_key = "12345"
db.init_app(app)
init_login_manager(app)
CORS(app)

run_blueprints(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
