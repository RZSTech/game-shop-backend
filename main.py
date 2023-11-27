from flask import Flask
from extensions import db
from base_operations.products_crud import products_crud
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db.init_app(app)
CORS(app)


app.register_blueprint(products_crud)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
