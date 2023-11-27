from extensions import db
from sqlalchemy import Numeric


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    category = db.Column(db.String(80))
    price = db.Column(Numeric(10, 2))
    available = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'available': self.available
        }


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'age': self.age
        }


class PaymentType(db.Model):
    __tablename__ = 'payment_types'

    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String(100), nullable=False)
    payment_time = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'payment_method': self.payment_method,
            'payment_time': self.payment_time
        }


class ShippingMethod(db.Model):
    __tablename__ = 'shipping_methods'

    id = db.Column(db.Integer, primary_key=True)
    transport = db.Column(db.String(100), nullable=False)
    waiting_time = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'transport': self.transport,
            'waiting_time': self.waiting_time
        }


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }
