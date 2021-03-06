from curses.ascii import HT
from flask import request, jsonify, current_app
from app.exceptions.missing_keys import MissingKeysError
from app.models.user_drug_model import UserDrugs
from http import HTTPStatus
from sqlalchemy.orm import Session
from werkzeug.exceptions import BadRequest, NotFound, Forbidden
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from app.services.user_drugs_services import data_standardized, drug_data_updated, verify_keys_and_values, verify_values

@jwt_required()
def get_user_drug():

    session: Session = current_app.db.session
    id = get_jwt_identity()["id"]

    drug_data = session.query(UserDrugs).filter_by(user_id = id).first()

    if not drug_data:
        return {}, HTTPStatus.OK

    return jsonify(drug_data), HTTPStatus.OK


@jwt_required()
def create_drug_data():
    try:
        session: Session = current_app.db.session
        user_id = get_jwt_identity()["id"]
        data = request.get_json()

        verify_keys_and_values(data)

        data = data_standardized(data=data)

        data_drugs = UserDrugs(**data, user_id=user_id)

        session.add(data_drugs)
        session.commit()

        return jsonify(data_drugs), HTTPStatus.CREATED
    
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return {"Error": "Drugs information already exists."}, HTTPStatus.CONFLICT
    
    except MissingKeysError as e:
        message = {"Error": f"Only keys {e.requireds} must be send."}
        return message, e.status_code

    except BadRequest as e:
        return e.description, e.code


@jwt_required()
def update_user_drug_data():
    try:
        session: Session = current_app.db.session
        user_id = get_jwt_identity()["id"]
        data = request.get_json()

        verify_values(list(data.values()))

        old_data = session.query(UserDrugs).filter_by(user_id = user_id).first()

        if not old_data:
            return {}, HTTPStatus.OK

        new_data =  drug_data_updated(data, old_data)

        session.add(new_data)
        session.commit()

        return jsonify(new_data), HTTPStatus.OK
    
    except BadRequest as e:
        return e.description, e.code

    except NotFound as e:
        return e.description, e.code
    
    except Forbidden as e:
        return e.description, e.code

@jwt_required()
def delete_drug_data():
    session: Session = current_app.db.session
    id = get_jwt_identity()["id"]
    drug_data = session.query(UserDrugs).filter_by(user_id = id).first()

    if not drug_data:
        return "", HTTPStatus.NO_CONTENT

    session.delete(drug_data)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
 
