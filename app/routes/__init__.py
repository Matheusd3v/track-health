from flask import Flask
from app.routes.user_route import bp_user
from app.routes.anamnesis_route import bp as bp_anamnesis


def init_app(app: Flask):
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_anamnesis)