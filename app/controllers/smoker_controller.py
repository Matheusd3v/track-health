from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.user_smoker_model import UserSmoker
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.user_smoker_services import check_data_keys, get_invalid_data
from sqlalchemy.orm import Session

@jwt_required()
def create_data():
    user = get_jwt_identity()
    session = current_app.db.session

    data = request.get_json()
    if not check_data_keys(data):
        return {"error": "Invalid keys were found",
                "valid keys": ['description','frequency']
                 }, HTTPStatus.BAD_REQUEST


    invalid_data = get_invalid_data(data)
    if invalid_data:
        return {"These keys are with an invalid data type": invalid_data}, HTTPStatus.BAD_REQUEST

    if 'frequency' not in data.keys():
        return{'error': "frequency key must be in the body"}, HTTPStatus.BAD_REQUEST

    data['user_id'] = user['id']

    new_data = UserSmoker(**data)

    session.add(new_data)
    session.commit()

    return jsonify(new_data)
