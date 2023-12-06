from base_operations.products_crud import products_crud
from base_operations.users_crud import users_crud
from base_operations.order_crd import order_crd
from authorization.login_controller import login_controller
from authorization.register_controller import register_controller


def run_blueprints(app):
    app.register_blueprint(products_crud)
    app.register_blueprint(login_controller)
    app.register_blueprint(register_controller)
    app.register_blueprint(order_crd)
    app.register_blueprint(users_crud)
