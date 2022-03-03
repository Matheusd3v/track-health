from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.user_alcoholic_model import UserAlcoholic
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.user_alcoholic_services import check_data_id, check_data_keys, get_invalid_data
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError,IntegrityError

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
    try:
        session.commit()
    except IntegrityError:
        return {"error": "you can only have one data of this type"}, HTTPStatus.CONFLICT
    return jsonify(user_alcoholic), HTTPStatus.CREATED


@jwt_required()
def get_alcoholic(alcoholic_id):
    user = get_jwt_identity()
    if not alcoholic_id:
        return {"error":"id must be in the url"},HTTPStatus.BAD_REQUEST

    try:
        user_alcoholic = UserAlcoholic.query.filter_by(id=alcoholic_id).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not user_alcoholic:
        return {"error": "data not found"}, HTTPStatus.NOT_FOUND


    if not check_data_id(user_alcoholic,user):
        return{"error": "that data is not from your user"}
    return jsonify(user_alcoholic), HTTPStatus.OK



@jwt_required()
def patch_alcoholic(alcoholic_id):
    user = get_jwt_identity()
    data = request.get_json()
    session:Session = current_app.db.session


    if not alcoholic_id:
        return {"error":"id must be in the url"},HTTPStatus.BAD_REQUEST

    if not check_data_keys(data):
        return {"error": "Invalid keys were found",
                "valid keys": ['description','frequency']
                 }, HTTPStatus.BAD_REQUEST


    invalid_data = get_invalid_data(data)
    if invalid_data:
        return {"These keys are with an invalid data type": invalid_data}, HTTPStatus.BAD_REQUEST

    try:
        user_alcoholic = UserAlcoholic.query.filter_by(id=alcoholic_id).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not user_alcoholic:
        return {"error": "data not found"}, HTTPStatus.NOT_FOUND

    if not check_data_id(user_alcoholic,user):
        return{"error": "that data is not from your user"}

    for key,value in data.items():
        setattr(user_alcoholic,key,value)

    session.add(user_alcoholic)
    session.commit()
    return jsonify(user_alcoholic), HTTPStatus.OK



@jwt_required()
def delete_alcoholic(alcoholic_id):
    user = get_jwt_identity()
    session:Session = current_app.db.session


    if not alcoholic_id:
        return {"error":"id must be in the url"},HTTPStatus.BAD_REQUEST

    try:
        user_alcoholic = UserAlcoholic.query.filter_by(id=alcoholic_id).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not user_alcoholic:
        return {"error": "data not found"}, HTTPStatus.NOT_FOUND


    if not check_data_id(user_alcoholic,user):
        return{"error": "that data is not from your user"}

    session.delete(user_alcoholic)
    session.commit()

    return '', HTTPStatus.NO_CONTENT