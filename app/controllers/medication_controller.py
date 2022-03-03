from http import HTTPStatus
from unicodedata import name
from flask import current_app, jsonify, request
from app.models.medication_model import Medication
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import BadRequest
from app.models.user_model import User
from app.services.medication_services import serializing_medications, validate_body, validate_update
from app.models.user_medication import UserMedication


def create_medication():

    try:
        data = request.get_json()
        session = current_app.db.session

        if not data or not data.get("name"):
            return {"error":"The field 'name' its required"}, HTTPStatus.BAD_REQUEST

        medication = Medication(**data)

        session.add(medication)
        session.commit()

        return jsonify(medication), HTTPStatus.CREATED


    except IntegrityError:
        return {"error":"A medication with name already exists on the database"}, HTTPStatus.CONFLICT




@jwt_required()
def create_medication_user():
    try:
        data = request.get_json()
        validate_body(data)

        session = current_app.db.session
        user = dict(get_jwt_identity())
        medication = Medication.query.filter_by(name=data.get("name")).first()

        if not medication:
            medication = Medication(name = data.get("name"))
            session.add(medication)
            session.commit()


        user_medication_data = {"user_id": user["id"], "medication_id":medication.id, "description": data.get("description")}
        user_medication = UserMedication(**user_medication_data)
        session.add(user_medication)
        session.commit()
        return jsonify(medication), HTTPStatus.CREATED

    except BadRequest as e:
        return e.description, e.code

    except IntegrityError:
        return {"error":"Missing 'name' field"}, HTTPStatus.BAD_REQUEST

@jwt_required()
def get_medications():
    user_id= get_jwt_identity()["id"]
    user = User.query.filter_by(id = user_id).first()
    
    return jsonify(serializing_medications(user)), HTTPStatus.OK



@jwt_required()
def update_medication_user(medication_id):
    
    session = current_app.db.session
    data = request.get_json()
    user_id= get_jwt_identity()["id"]

    user_medication = UserMedication.query.filter_by(medication_id=medication_id).first()
    
    if not user_medication:
        return {"error":"A medication with this id was not found"}, HTTPStatus.NOT_FOUND
        
    if str(user_medication.user_id)  != str(user_id):
        return {"error":"You're not allowed to update this medication"}, HTTPStatus.NOT_ACCEPTABLE


    validate_update(data, user_medication)

    session.add(user_medication)
    session.commit()
    
    medication = Medication.query.filter_by(id = user_medication.medication_id).first()

    return jsonify({
        "id":medication.id,
        "name":medication.name,
        "description":user_medication.description
    }), HTTPStatus.OK



@jwt_required()
def delete_medication_user(medication_id):
    session = current_app.db.session

    user_id= get_jwt_identity()["id"]
    user_medication = UserMedication.query.filter_by(medication_id=medication_id).first()

    if not user_medication:
        return {"error":"A medication with this id was not found"}, HTTPStatus.NOT_FOUND

    if str(user_medication.user_id)  != str(user_id):
        return {"error":"You're not allowed to delete this medication"}, HTTPStatus.NOT_ACCEPTABLE

    session.delete(user_medication)
    session.commit()

    return '', HTTPStatus.NO_CONTENT