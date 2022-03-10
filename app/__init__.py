from flask import Flask
from app.configs import database, jwt_auth, migration
from app import routes
from os import getenv
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)
    
    app.config["JSON_SORT_KEYS"] = False
    app.config['MAX_CONTENT_LENGTH'] = int(getenv('MAXIMUM_FILE_SIZE'))

    database.init_app(app)
    migration.init_app(app)
    jwt_auth.init_app(app)
    routes.init_app(app)

    return app