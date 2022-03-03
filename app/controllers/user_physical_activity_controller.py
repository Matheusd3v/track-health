from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.user_physical_activity_model import UserPhysicalActivity
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.user_physical_activity_services import check_data_id, check_data_keys, get_invalid_data
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError

@jwt_required()
def create_physical_activity():
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

    new_physical_activity = UserPhysicalActivity(**data)

    session.add(new_physical_activity)
    session.commit()

    return jsonify(new_physical_activity), HTTPStatus.CREATED


@jwt_required()
def get_physical_activity(physical_activity_id):
    user = get_jwt_identity()
    if not physical_activity_id:
        return {"error":"id must be in the url"},HTTPStatus.BAD_REQUEST

    try:
        physical_activity = UserPhysicalActivity.query.filter_by(id=physical_activity_id).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not physical_activity:
        return {"error": "data not found"}, HTTPStatus.NOT_FOUND


    if not check_data_id(physical_activity,user):
        return{"error": "that data is not from your user"}
    return jsonify(physical_activity), HTTPStatus.OK



@jwt_required()
def patch_physical_activity(physical_activity_id):
    user = get_jwt_identity()
    data = request.get_json()
    session:Session = current_app.db.session


    if not physical_activity_id:
        return {"error":"id must be in the url"},HTTPStatus.BAD_REQUEST

    if not check_data_keys(data):
        return {"error": "Invalid keys were found",
                "valid keys": ['description','frequency']
                 }, HTTPStatus.BAD_REQUEST


    invalid_data = get_invalid_data(data)
    if invalid_data:
        return {"These keys are with an invalid data type": invalid_data}, HTTPStatus.BAD_REQUEST

    try:
        physical_activity = UserPhysicalActivity.query.filter_by(id=physical_activity_id).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not physical_activity:
        return {"error": "data not found"}, HTTPStatus.NOT_FOUND


    if not check_data_id(physical_activity,user):
        return{"error": "that data is not from your user"}

    for key,value in data.items():
        setattr(physical_activity,key,value)

    session.add(physical_activity)
    session.commit()
    return jsonify(physical_activity), HTTPStatus.OK



@jwt_required()
def delete_physical_activity(physical_activity_id):
    user = get_jwt_identity()
    session:Session = current_app.db.session


    if not physical_activity_id:
        return {"error":"id must be in the url"},HTTPStatus.BAD_REQUEST

    try:
        physical_activity = UserPhysicalActivity.query.filter_by(id=physical_activity_id).first()
    except DataError:
        return {"error": "Appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not physical_activity:
        return {"error": "data not found"}, HTTPStatus.NOT_FOUND


    if not check_data_id(physical_activity,user):
        return{"error": "that data is not from your user"}

    session.delete(physical_activity)
    session.commit()

    return '', HTTPStatus.NO_CONTENT