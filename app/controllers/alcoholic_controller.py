from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.user_alcoholic_model import UserAlcoholic
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.user_alcoholic_services import check_data_id, check_data_keys, get_invalid_data
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError,IntegrityError

from app.services.user_smoker_services import normalized_data, remove_spaces

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

    data = normalized_data(data)
    data['user_id'] = user['id']

    user_alcoholic = UserAlcoholic(**data)

    session.add(user_alcoholic)
    try:
        session.commit()
    except IntegrityError:
        return {"error": "you can only have one data of this type"}, HTTPStatus.CONFLICT
    return jsonify(user_alcoholic), HTTPStatus.CREATED


@jwt_required()
def get_alcoholic():
    user = get_jwt_identity()
    id_user = user["id"]
    try:
        user_alcoholic = UserAlcoholic.query.filter_by(user_id = id_user).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not user_alcoholic:
        return {}, HTTPStatus.OK

    if not check_data_id(user_alcoholic,user):
        return{"error": "that data is not from your user"}
    return jsonify(user_alcoholic), HTTPStatus.OK



@jwt_required()
def patch_alcoholic():
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
        user_alcoholic = UserAlcoholic.query.filter_by(user_id=id_user).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not user_alcoholic:
        return {}, HTTPStatus.OK

    if not check_data_id(user_alcoholic,user):
        return{"error": "that data is not from your user"}

    for key,value in data.items():
        setattr(user_alcoholic,key,remove_spaces(value))

    session.add(user_alcoholic)
    session.commit()
    return jsonify(user_alcoholic), HTTPStatus.OK



@jwt_required()
def delete_alcoholic():
    user = get_jwt_identity()
    id_user = user["id"]
    session:Session = current_app.db.session

    try:
        user_alcoholic = UserAlcoholic.query.filter_by(user_id=id_user).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not user_alcoholic:
        return '', HTTPStatus.NO_CONTENT

    if not check_data_id(user_alcoholic,user):
        return{"error": "that data is not from your user"}

    session.delete(user_alcoholic)
    session.commit()

    return '', HTTPStatus.NO_CONTENT