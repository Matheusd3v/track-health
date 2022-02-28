from http import HTTPStatus
from flask import jsonify, request, session
from app.services.address_services import check_data_keys,get_invalid_data
from app.models.address_model import AddressModel
from flask import current_app
from sqlalchemy.orm import Session
from sqlalchemy.exc import ProgrammingError


def create_address():
    data = request.get_json()
    session: Session = current_app.db.session
    
    if not check_data_keys(data):
        return {"error": "Invalid keys"}, HTTPStatus.BAD_REQUEST

    invalid_data = get_invalid_data(data)
    if invalid_data:
        return {"These keys are with an invalid data type": invalid_data}, HTTPStatus.BAD_REQUEST


    new_address = AddressModel(**data)

    session.add(new_address)
    session.commit()
    return jsonify(new_address),HTTPStatus.CREATED

def get_address():
    data = request.get_json()

    if list(data.keys()) != ['address_id']:
        return {'msg':'Invalid body, it must be only address_id key'},HTTPStatus.BAD_REQUEST

    try:
         address : AddressModel = AddressModel.query.filter_by(id = data['address_id']).first()
    except ProgrammingError:
        return{"error": "address_id must be an UUID"},HTTPStatus.BAD_REQUEST

    if not address:
        return {'Error': 'Invalid address_id'}, HTTPStatus.NOT_FOUND
    return jsonify(address)


def patch_address():
    data = request.get_json()
    session: Session = current_app.db.session

    if 'address_id' not in data.keys():
        return {'msg':'Invalid body, it must have address_id'}, HTTPStatus.BAD_REQUEST


    if not check_data_keys(data):
        return {"error": "Invalid keys were found"}, HTTPStatus.BAD_REQUEST

    try:
         address : AddressModel = AddressModel.query.filter_by(id = data['address_id']).first()
    except ProgrammingError:
        return{"error": "Address_id must be an UUID"},HTTPStatus.BAD_REQUEST


    if not address:
        return {'Error': 'Invalid address_id'}, HTTPStatus.NOT_FOUND

    for key,value in data.items():
        setattr(address,key,value)

    session.add(address)
    session.commit()

    return jsonify(address)


def delete_address():
    data = request.get_json()
    session: Session = current_app.db.session


    if list(data.keys()) != ['address_id']:
        return {'msg':'Invalid body, it must be only address_id key'},HTTPStatus.BAD_REQUEST

    try:
         address : AddressModel = AddressModel.query.filter_by(id = data['address_id']).first()
    except ProgrammingError:
        return{"error": "address_id must be an UUID"},HTTPStatus.BAD_REQUEST

    if not address:
        return {'Error': 'Invalid address_id'}, HTTPStatus.NOT_FOUND

    session.delete(address)
    session.commit()
    return jsonify(address)