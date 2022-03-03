from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.user_alcoholic_model import UserAlcoholic
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.user_alcoholic_services import check_data_id, check_data_keys, get_invalid_data
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError

@jwt_required()
def create_alcoholic():
    user = get_jwt_identity()
    session:Session = current_app.db.session

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

    user_alcoholic = UserAlcoholic(**data)

    session.add(user_alcoholic)
    session.commit()

    return jsonify(user_alcoholic), HTTPStatus.CREATED

