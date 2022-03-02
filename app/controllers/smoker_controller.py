from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.user_smoker_model import UserSmoker
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.user_smoker_services import check_data_id, check_data_keys, get_invalid_data
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError

@jwt_required()
def create_data():
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

    new_data = UserSmoker(**data)

    session.add(new_data)
    session.commit()

    return jsonify(new_data), HTTPStatus.CREATED

@jwt_required()
def get_data(smoker_id):
    user = get_jwt_identity()
    if not smoker_id:
        return {"error":"id must be in the url"},HTTPStatus.BAD_REQUEST

    try:
        data = UserSmoker.query.filter_by(id=smoker_id).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not data:
        return {"error": "data not found"}, HTTPStatus.NOT_FOUND


    if not check_data_id(data,user):
        return{"error": "that data is not from your user"}
    return jsonify(data), HTTPStatus.OK