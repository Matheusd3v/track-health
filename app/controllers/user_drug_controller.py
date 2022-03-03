from flask import request, jsonify, current_app
from app.exceptions.missing_keys import MissingKeysError
from app.models.user_drug_model import UserDrugs
from http import HTTPStatus
from sqlalchemy.orm import Session
from werkzeug.exceptions import NotFound, Unauthorized, BadRequest
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

from app.services.user_drugs_services import drug_data_updated

@jwt_required()
def get_user_drug():
    session: Session = current_app.db.session
    user_id = get_jwt_identity()["id"]
    user_drug = session.query(UserDrugs).filter_by(user_id=user_id).first()

    return jsonify(user_drug), HTTPStatus.OK

@jwt_required()
def create_drug_data():
    session: Session = current_app.db.session
    user_id = get_jwt_identity()["id"]
    data = request.get_json()

    data_drugs = UserDrugs(**data, user_id=user_id)

    session.add(data_drugs)
    session.commit()

    return jsonify(data_drugs), HTTPStatus.CREATED


@jwt_required()
def update_user_drug_data(drug_id: str):
    session: Session = current_app.db.session
    data = request.get_json()

    old_data = session.query(UserDrugs).get(drug_id)

    new_data =  drug_data_updated(data, old_data)

    session.add(new_data)
    session.commit()

    return jsonify(new_data), HTTPStatus.OK

@jwt_required()
def delete_drug_data(drug_id: str):
    session: Session = current_app.db.session

    drug_data = session.query(UserDrugs).get(drug_id)

    session.delete(drug_data)
    session.commit()

    return "", HTTPStatus.NO_CONTENT

 
