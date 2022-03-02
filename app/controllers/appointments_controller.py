from http import HTTPStatus
from flask import jsonify, request ,session, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.appointment_model import AppointmentModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError
from app.services.appointments_services import check_data_keys_patch, check_data_keys_get, get_invalid_data, check_appointment_id


@jwt_required()
def create_controller():
    data = request.get_json()
    user = get_jwt_identity()
    session: Session = current_app.db.session

   
    if not check_data_keys_get(data):
        return {"error": "Invalid keys were found"},HTTPStatus.BAD_REQUEST
    
    invalid_data = get_invalid_data(data)

    if invalid_data:
        return {"invalid_keys": invalid_data},HTTPStatus.BAD_REQUEST

    data['user_id'] = user['id']
    new_appointment = AppointmentModel(**data)
    session.add(new_appointment)
    session.commit()
    return jsonify(new_appointment), HTTPStatus.CREATED


@jwt_required()
def get_appointment():
    data = request.get_json()
    user = get_jwt_identity()


    if list(data.keys()) != ['appointment_id']:
        return{"error": "body must have only the appointment_id"},HTTPStatus.OK

   
    appointment_id = data['appointment_id']
    try:
        appointment = AppointmentModel.query.filter_by(id = appointment_id).first()

    except DataError:
        return {"error": "address id is not valid"},HTTPStatus.BAD_REQUEST


    if not appointment:
        return {"error":"Appointment not found"}, HTTPStatus.NOT_FOUND

    if not check_appointment_id(appointment, user):
        return {"error":"This appointment is not from your user"}, HTTPStatus.NOT_FOUND

    return jsonify(appointment)


@jwt_required()
def patch_appointment(appointment_id):
    data = request.get_json()
    user = get_jwt_identity()
    session: Session = current_app.db.session

    if not appointment_id:
        return{"error": "url must have the appointment_id"},HTTPStatus.OK

    if not check_data_keys_patch(data):
        return {"error": "Invalid keys were found"}, HTTPStatus.BAD_REQUEST

    try:
        appointment = AppointmentModel.query.filter_by(id = appointment_id).first()

    except DataError:
        return {"error": "appointment id is not valid"},HTTPStatus.BAD_REQUEST

    if not appointment:
        return {"error":"Appointment not found"}, HTTPStatus.NOT_FOUND

    if not check_appointment_id(appointment, user):
        return {"error":"This appointment is not from your user"}, HTTPStatus.NOT_FOUND

    for key,value in data.items():
        setattr(appointment,key,value)

    session.add(appointment)
    session.commit()

    return jsonify(appointment)

@jwt_required()
def delete_appointment():
    data = request.get_json()
    user = get_jwt_identity()
    session: Session = current_app.db.session


    if list(data.keys()) != ['appointment_id']:
        return{"error": "body must have only the appointment_id"},HTTPStatus.OK

   
    appointment_id = data['appointment_id']
    try:
        appointment = AppointmentModel.query.filter_by(id = appointment_id).first()

    except DataError:
        return {"error": "appointment id is not valid"},HTTPStatus.BAD_REQUEST


    if not appointment:
        return {"error":"Appointment not found"}, HTTPStatus.NOT_FOUND
    
    if not check_appointment_id(appointment, user):
        return {"error":"This appointment is not from your user"}, HTTPStatus.NOT_FOUND
    
    session.delete(appointment)
    session.commit()

    return '',HTTPStatus.NO_CONTENT