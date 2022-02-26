from datetime import timedelta
from flask import request, jsonify, current_app, session
from app.models.user_model import User
from http import HTTPStatus
from sqlalchemy.orm import Session
from werkzeug.exceptions import NotFound, Unauthorized
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app.services.user_services import user_updated

def create_user():
    session: Session = current_app.db.session
    data = request.get_json()

    password_to_hash = data.pop("password")

    user = User(**data)
    user.password = password_to_hash

    session.add(user)
    session.commit()

    return jsonify(user), HTTPStatus.CREATED

def login():
    session: Session = current_app.db.session
    data = request.get_json()

    user = session.query(User).filter_by(email = data["email"]).first()
    password = data["password"]
    # verificar user e senha

    token = create_access_token(user, expires_delta=(timedelta(hours=4)) )

    return jsonify({"user_data": user,"access_token": token }), HTTPStatus.OK

@jwt_required()
def get_user():
    session: Session = current_app.db.session
    user_jwt = get_jwt_identity()

    user_bd = session.query(User).get(user_jwt["id"])

    return jsonify(user_bd), HTTPStatus.OK

@jwt_required()
def update_user():
    session: Session = current_app.db.session
    data = request.get_json()

    user_jwt = get_jwt_identity()

    old_user = session.query(User).get(user_jwt["id"])

    new_user = user_updated(data, old_user)

    session.add(new_user)
    session.commit()

    return jsonify(new_user), HTTPStatus.OK

@jwt_required()
def delete_user():
    session: Session = current_app.db.session
    user_id = get_jwt_identity()["id"]

    user = session.query(User).get(user_id)

    session.delete(user)
    session.commit()

    return "", HTTPStatus.NO_CONTENT




    
