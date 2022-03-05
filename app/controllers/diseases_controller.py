from flask import request
from sqlalchemy.orm import Session
from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound, Unauthorized, BadRequest
from http import HTTPStatus
from app.models.diseases_detail_model import DiseasesDetailModel
from app.models.user_disease_model import UserDiseaseModel
from sqlalchemy.exc import IntegrityError, ProgrammingError, DataError
from sqlalchemy.orm.exc import UnmappedInstanceError
from app.services.diseases_services import find_diseases, serializing_all_fields, verify_update_types, verify_user_diseases_key, normalize_disease_keys
from app.models.user_model import User


@jwt_required()
def create_user_diseases():
    try:
        data = request.get_json()

        session: Session = current_app.db.session

        verify_user_diseases_key(data)
        data = normalize_disease_keys(data)
        diseases = find_diseases(data)
        user_id = get_jwt_identity()["id"]

        data["user_id"] = user_id

        diseases_datails = DiseasesDetailModel(description=data.get(
            "description"), medication=data.get("medication"))

        session.add(diseases_datails)
        session.commit()

        user_diseases = UserDiseaseModel(user_id=user_id, disease_id=diseases.id,
            disease_detail_id=diseases_datails.id)

        session.add(user_diseases)
        session.commit()

        

        return jsonify(serializing_all_fields(user_diseases.asdict())), HTTPStatus.CREATED

    except BadRequest:
        return jsonify({"Error": "The keyword 'name' does not exit"}), HTTPStatus.BAD_REQUEST


@jwt_required()
def update_diseases(disease_id):
    try:
        session: Session = current_app.db.session
        data = request.get_json()

        diseases_details_id = UserDiseaseModel.query.filter_by(
            disease_id=disease_id).first()

        diseases_details = DiseasesDetailModel.query.filter_by(
            id=diseases_details_id.disease_detail_id).first()

        for key, value in data.items():
            setattr(diseases_details, key, value)

        session.add(diseases_details)
        session.commit()

        return jsonify(diseases_details), HTTPStatus.OK

    except ProgrammingError:
        data = request.get_json()
        msg = verify_update_types(data)
        return jsonify({"Error": msg}), HTTPStatus.BAD_REQUEST

    except (DataError, AttributeError):
        return {"Error": f"disease_id {disease_id} is not valid"}, HTTPStatus.NOT_FOUND


@jwt_required()
def delete_user_diseases(disease_id):
    try:
        session: Session = current_app.db.session
        diseases = UserDiseaseModel.query.filter_by(
            disease_id=disease_id).first()
        diseases_datails = DiseasesDetailModel.query.filter_by(
            id=diseases.disease_detail_id).first()

        session.delete(diseases)
        session.commit()
        session.delete(diseases_datails)
        session.commit()
        return "", HTTPStatus.NO_CONTENT
    except (DataError, UnmappedInstanceError):
        return {"Error": f"disease_id {disease_id} is not valid"}, HTTPStatus.NOT_FOUND


@jwt_required()
def get_user_diseases():

    user_identity = get_jwt_identity()

    user = User.query.get(user_identity['id'])

    user = user.asdict()

    user_disease = serializing_all_fields(user)

    return jsonify(user_disease['diseases']), HTTPStatus.OK
