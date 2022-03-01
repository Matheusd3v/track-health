from flask import request
from sqlalchemy.orm import Session
from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound, Unauthorized, BadRequest
from http import HTTPStatus
from app.models.diseases_detail_model import DiseasesDetailModel
from app.models.user_disease_model import UserDiseaseModel

from app.services.diseases_services import find_diseases, verify_user_diseases_key

# diseases


@jwt_required()
def create_user_diseases():
    try:
        data = request.get_json()

        session: Session = current_app.db.session

        verify_user_diseases_key(data)

        diseases = find_diseases(data)
        user_id = get_jwt_identity()["id"]

        data["user_id"] = user_id

        diseases_datails = DiseasesDetailModel(**data)

        session.add(diseases_datails)
        session.commit()

        user_diseases = UserDiseaseModel(user_id=user_id, diseases_id=diseases.id,
                                         diseases_details_id=diseases_datails.id)

        session.add(user_diseases)
        session.commit()
        return jsonify(user_diseases), HTTPStatus.CREATED
    except BadRequest:
        return jsonify({"Error": "The keyword 'name' does not exit"}), HTTPStatus.BAD_REQUEST
