from flask import request, jsonify, current_app
from app.exceptions.missing_keys import MissingKeysError
from app.models.user_drug_model import UserDrugs
from app.models.user_model import User
from http import HTTPStatus
from sqlalchemy.orm import Session
from werkzeug.exceptions import NotFound, Unauthorized, BadRequest
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

@jwt_required()
def get_user_drug():
    session: Session = current_app.db.session
    user_id = get_jwt_identity()["id"]
    user_drug = session.query(UserDrugs).filter_by(user_id=user_id).first()

    return jsonify(user_drug), HTTPStatus.OK
