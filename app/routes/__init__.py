from flask import Flask
from app.routes.user_route import bp_user
from app.routes.address_route import bp_address

def init_app(app: Flask):
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_address)
