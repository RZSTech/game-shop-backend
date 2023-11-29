from flask import jsonify, request, Blueprint
from extensions import db
from database.database import Product
from random import sample

products_crud = Blueprint('products_crud', __name__)


@products_crud.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify({'products': [product.to_dict() for product in products]})


@products_crud.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(name=data['name'], description=data['description'], price=data['price'], available=data['available'])
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product created successfully', 'product': new_product.to_dict()}), 201


@products_crud.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    data = request.json
    product = Product(name=data['name'], description=data['description'], price=data['price'], available=data['available'])

    db.session.commit()
    return jsonify(product.to_dict())


@products_crud.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'result': True})


@products_crud.route('/products/random', methods=['GET'])
def get3_random_products():
    products = Product.query.all()
    if len(products) < 3:
        return jsonify({'error': 'Not enough products'}), 400

    random_products = sample(products, 3)
    return jsonify({'products': [product.to_dict() for product in random_products]})
