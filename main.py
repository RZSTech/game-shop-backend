from flask import Flask
from extensions import db
from base_operations.products_crud import products_crud
from login.login_controller import login_controller
from login.register_controller import register_controller
from flask_cors import CORS
from login.flask_login import init_login_manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.secret_key = "12345"
db.init_app(app)
init_login_manager(app)
CORS(app)


app.register_blueprint(products_crud)
app.register_blueprint(login_controller)
app.register_blueprint(register_controller)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
