from http import HTTPStatus
from flask import jsonify, request
from flask import current_app
from sqlalchemy.orm import Session
from sqlalchemy.exc import ProgrammingError,DataError
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequest

from app.services.address_services import check_data_keys, get_invalid_data, address_normalize
from app.models.address_model import AddressModel


@jwt_required()
def create_address():
    try:
        data = request.get_json()
        session: Session = current_app.db.session

        if not check_data_keys(data):
            return {"error": "Invalid keys"}, HTTPStatus.BAD_REQUEST

        invalid_data = get_invalid_data(data)
        if invalid_data:
            raise BadRequest

        address_normalize(data)

        new_address = AddressModel(**data)

        session.add(new_address)
        session.commit()
        return jsonify(new_address),HTTPStatus.CREATED

    except BadRequest as e:
        return {"error": e.description}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_address():
    session: Session = current_app.db.session

    my_doctors = session.query(AddressModel).all()

    return jsonify(my_doctors), HTTPStatus.OK


@jwt_required()
def patch_address():
    data = request.get_json()
    session: Session = current_app.db.session

    if 'address_id' not in data.keys():
        return {'msg':'Invalid body, it must have address_id'}, HTTPStatus.BAD_REQUEST

    if not check_data_keys(data):
        return {"error": "Invalid keys were found"}, HTTPStatus.BAD_REQUEST

    try:
        invalid_data = get_invalid_data(data)
        if invalid_data:
            raise BadRequest(description = f"wrong type fields {', '.join(invalid_data)}")

        address_normalize(data)
        address : AddressModel = AddressModel.query.filter_by(id = data['address_id']).first()
    
    except BadRequest as e:
        return {"error": e.description}, HTTPStatus.BAD_REQUEST

    except ProgrammingError:
        return{"error": "Address_id must be an UUID"},HTTPStatus.BAD_REQUEST
    
    except DataError:
        return {"error": "address id is not valid"},HTTPStatus.BAD_REQUEST

    if not address:
        return {'Error': 'Invalid address_id'}, HTTPStatus.NOT_FOUND

    for key,value in data.items():
        setattr(address,key,value)

    session.add(address)
    session.commit()

    return jsonify(address), HTTPStatus.OK


@jwt_required()
def delete_address():
    data = request.get_json()
    session: Session = current_app.db.session

    if list(data.keys()) != ['address_id']:
        return {'msg':'Invalid body, it must be only address_id key'},HTTPStatus.BAD_REQUEST

    try:
         address : AddressModel = AddressModel.query.filter_by(id = data['address_id']).first()
    except ProgrammingError:
        return{"error": "address_id must be an UUID"},HTTPStatus.BAD_REQUEST
    except DataError:
        return {"error": "address id is not valid"},HTTPStatus.BAD_REQUEST
        
    if not address:
        return {'Error': 'Invalid address_id'}, HTTPStatus.NOT_FOUND

    session.delete(address)
    session.commit()
    return '', HTTPStatus.NO_CONTENT