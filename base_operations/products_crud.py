from flask import jsonify, request, Blueprint
from extensions import db
from database.database import Product

products_crud = Blueprint('products_crud', __name__)


@products_crud.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify({'products': [product.to_dict() for product in products]})
