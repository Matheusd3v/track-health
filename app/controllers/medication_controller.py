from http import HTTPStatus
from unicodedata import name
from flask import current_app, jsonify, request
from app.models.medication_model import Medication
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import BadRequest
from app.services.medication_services import validate_body
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
        # session.add(user_medication)
        # session.commit()

        return jsonify(user_medication), HTTPStatus.CREATED
    except BadRequest as e:
        return e.description, e.code
