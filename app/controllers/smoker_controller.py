from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.user_smoker_model import UserSmoker
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.user_smoker_services import check_data_id, check_data_keys, get_invalid_data, normalized_data, remove_spaces
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError,IntegrityError

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

    data = normalized_data(data)
    data['user_id'] = user['id']

    new_data = UserSmoker(**data)

    session.add(new_data)
    try:
        session.commit()
    except IntegrityError:
        return {"error": "you can only have one data of this type"}, HTTPStatus.CONFLICT
    return jsonify(new_data), HTTPStatus.CREATED

@jwt_required()
def get_data():
    user = get_jwt_identity()
    id_user = user["id"]

    try:
        data = UserSmoker.query.filter_by(user_id=id_user).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not data:
        return jsonify([]), HTTPStatus.OK


    if not check_data_id(data,user):
        return{"error": "that data is not from your user"}
    return jsonify(data), HTTPStatus.OK



@jwt_required()
def patch_data():
    user = get_jwt_identity()
    id_user = user["id"]
    data = request.get_json()
    session:Session = current_app.db.session


    if not check_data_keys(data):
        return {"error": "Invalid keys were found",
                "valid keys": ['description','frequency']
                 }, HTTPStatus.BAD_REQUEST


    invalid_data = get_invalid_data(data)
    if invalid_data:
        return {"These keys are with an invalid data type": invalid_data}, HTTPStatus.BAD_REQUEST

    try:
        user_smoker = UserSmoker.query.filter_by(user_id=id_user).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not user_smoker:
        return {"error": "data not found"}, HTTPStatus.NOT_FOUND


    if not check_data_id(user_smoker,user):
        return{"error": "that data is not from your user"}

    for key,value in data.items():
        setattr(user_smoker,key,remove_spaces(value))

    session.add(user_smoker)
    session.commit()
    return jsonify(user_smoker), HTTPStatus.OK



@jwt_required()
def delete_data():
    user = get_jwt_identity()
    id_user = user["id"]
    session:Session = current_app.db.session

    try:
        user_smoker = UserSmoker.query.filter_by(user_id=id_user).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not user_smoker:
        return {"error": "data not found"}, HTTPStatus.NOT_FOUND


    if not check_data_id(user_smoker,user):
        return{"error": "that data is not from your user"}

    session.delete(user_smoker)
    session.commit()

    return '', HTTPStatus.NO_CONTENT