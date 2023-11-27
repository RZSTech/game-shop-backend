from flask import jsonify, request, Blueprint
from extensions import db
from database.database import Order

order_crd = Blueprint('order_crd', __name__)


@order_crd.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify({'orders': [order.to_dict() for order in orders]})


@order_crd.route('/orders', methods=['POST'])
def create_order():
    data = request.json

    if 'name' not in data or 'status' not in data:
        return jsonify({'error': 'Both "name" and "status" fields are required'}), 400

    new_order = Order(name=data['name'], status=data['status'])
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order created successfully', 'order': new_order.to_dict()}), 201


@order_crd.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)

    if not order:
        return jsonify({'error': 'Order not found'}), 404

    data = request.json

    if 'name' in data:
        order.name = data['name']
    if 'status' in data:
        order.status = data['status']

    db.session.commit()

    return jsonify({'message': 'Order updated successfully', 'order': order.to_dict()})


@order_crd.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)

    if not order:
        return jsonify({'error': 'Order not found'}), 404

    db.session.delete(order)
    db.session.commit()

    return jsonify({'message': 'Order deleted successfully'})
