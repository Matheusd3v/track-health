from email import message
from flask import request, jsonify, current_app
from app.models.address_model import AddressModel
from app.models.doctor_model import DoctorModel
from http import HTTPStatus
from sqlalchemy.orm import Session
from werkzeug.exceptions import NotFound, BadRequest
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.exceptions.missing_keys import MissingKeysError
from sqlalchemy.exc import DataError
from app.services.doctor_service import verify_fields_and_values
import re


@jwt_required()
def create_doctor():
    try:
        session: Session = current_app.db.session
        data = request.get_json()
        user_jwt = get_jwt_identity()

        data['name'] = data['name'].title()
        data['type'] = data['type'].title()
        if data.get('email'):
            data['email'] = data['email'].lower()
            if not(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data['email'])):
                return {"error": "invalid email"}, HTTPStatus.BAD_REQUEST

        if not re.fullmatch("^\([1-9]{2}\)[0-9]{5}\-[0-9]{4}$",data["phone"]):
            return {"error":"invalid format phone. Must be (xx)xxxxx-xxxx "}, HTTPStatus.BAD_REQUEST

        data['user_id'] = user_jwt['id']

        address = session.query(AddressModel).get(data["address_id"])

        if not address:
            message = {"Error": f"address_id: {data['address_id']} not found."}
            raise NotFound(description=message)

        verify_fields_and_values(data)

        doctor = DoctorModel(**data)

        session.add(doctor)
        session.commit()

        return jsonify(doctor), HTTPStatus.CREATED

    except MissingKeysError as e:
        return e.message(), e.status_code
    
    except BadRequest as e:
        return e.description, e.code
    
    except NotFound as e:
        return e.description, e.code

    except DataError as e:
        return {"error": "wrong address_id"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_doctor():
    session: Session = current_app.db.session
    user_jwt = get_jwt_identity()

    my_doctors = session.query(DoctorModel).filter_by(user_id = user_jwt["id"]).all()

    return jsonify(my_doctors), HTTPStatus.OK


@jwt_required()
def update_doctor(doctor_id):
    try:
        session: Session = current_app.db.session

        data = request.get_json()

        if data.get('name'):
            data['name'] = data['name'].title()
        if data.get('type'):
            data['type'] = data['type'].title()
        if data.get('email'):
            data['email'] = data['email'].lower()
            if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data['email']):
                return {"error": "invalid email"}, HTTPStatus.BAD_REQUEST

        if data.get('phone'):
            if not re.fullmatch("^\([1-9]{2}\)[0-9]{5}\-[0-9]{4}$",data["phone"]):
                return {"error":"invalid format phone. Must be (xx)xxxxx-xxxx "}, HTTPStatus.BAD_REQUEST

        doctor = session.query(DoctorModel).get(doctor_id)

        for key, value in data.items():
            setattr(doctor, key, value)

        session.add(doctor)
        session.commit()

        return jsonify(doctor), HTTPStatus.OK
    
    except NotFound as e:
        return e.description, e.code

    except AttributeError:
        return {"error": "wrong id"}, HTTPStatus.BAD_REQUEST

    except DataError as e:
        return {"error": "wrong id"}, e.code


@jwt_required()
def delete_doctor(doctor_id):
    try:
        session: Session = current_app.db.session

        doctor = session.query(DoctorModel).get_or_404(doctor_id)

        session.delete(doctor)
        session.commit()

        return '', HTTPStatus.NO_CONTENT
    
    except NotFound as e:
        return e.description, e.code

    except DataError as e:
        return {"error": "wrong id"}, HTTPStatus.BAD_REQUEST