from base_operations.products_crud import products_crud
from base_operations.order_crd import order_crd
from login.login_controller import login_controller
from login.register_controller import register_controller


def run_blueprints(app):
    app.register_blueprint(products_crud)
    app.register_blueprint(login_controller)
    app.register_blueprint(register_controller)
    app.register_blueprint(order_crd)
