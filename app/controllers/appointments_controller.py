from http import HTTPStatus
from flask import jsonify, request ,session, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.appointment_model import AppointmentModel
from sqlalchemy.orm import Session

from app.services.appointments_services import check_data_keys, get_invalid_data, check_appointment_id


@jwt_required()
def create_controller():
    data = request.get_json()
    user = get_jwt_identity()
    session: Session = current_app.db.session

   
    if not check_data_keys(data):
        return {"error": "Invalid keys were found"},HTTPStatus.BAD_REQUEST
    
    invalid_data = get_invalid_data(data)

    if invalid_data:
        return {"invalid_keys": invalid_data},HTTPStatus.BAD_REQUEST

    data['user_id'] = user['id']
    new_appointment = AppointmentModel(**data)
    session.add(new_appointment)
    session.commit()
    return jsonify(new_appointment), HTTPStatus.CREATED

