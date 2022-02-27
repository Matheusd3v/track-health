from datetime import timedelta
from flask import request, jsonify, current_app
from app.exceptions.missing_keys import MissingKeysError
from app.models.user_model import User
from http import HTTPStatus
from sqlalchemy.orm import Session
from werkzeug.exceptions import NotFound, Unauthorized, BadRequest
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from app.services.user_services import user_updated, verify_fields_and_values, verify_user, verify_user_and_password

def create_user():
    try:
        session: Session = current_app.db.session
        data = request.get_json()
        verify_fields_and_values(data)

        password_to_hash = data.pop("password")

        user = User(**data)
        user.password = password_to_hash

        session.add(user)
        session.commit()

        return jsonify(user), HTTPStatus.CREATED

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            message = {"Error": "A user with this email already exists."}
            return message, HTTPStatus.CONFLICT

    except MissingKeysError as e:
        return e.message(), e.status_code

    except BadRequest as e:
        return e.description, e.code
    

def login():
    try: 
        session: Session = current_app.db.session
        data = request.get_json()

        user = session.query(User).filter_by(email = data["email"]).first()
        password = data["password"]
        verify_user_and_password(user, password)

        token = create_access_token(user, expires_delta=(timedelta(hours=4)) )

        return jsonify({"user_data": user,"access_token": token }), HTTPStatus.OK
    
    except NotFound as e:
        return e.description, e.code
    
    except Unauthorized as e:
        return e.description, e.code

@jwt_required()
def get_user():
    try:
        session: Session = current_app.db.session
        user_jwt = get_jwt_identity()

        user_bd = session.query(User).get(user_jwt["id"])

        verify_user(user_bd)

        return jsonify(user_bd), HTTPStatus.OK
    
    except NotFound as e:
        return e.description, e.code

@jwt_required()
def update_user():
    try: 
        session: Session = current_app.db.session
        data = request.get_json()

        user_jwt = get_jwt_identity()

        old_user = session.query(User).get(user_jwt["id"])

        new_user = user_updated(data, old_user)

        session.add(new_user)
        session.commit()

        return jsonify(new_user), HTTPStatus.OK
    
    except NotFound as e:
        return e.description, e.code
    
    except BadRequest as e:
        return e.description, e.code

@jwt_required()
def delete_user():
    try:
        session: Session = current_app.db.session
        user_id = get_jwt_identity()["id"]

        user = session.query(User).get(user_id)

        verify_user(user)

        session.delete(user)
        session.commit()

        return "", HTTPStatus.NO_CONTENT
    
    except NotFound as e: 
        return e.description, e.code




    
