from http import HTTPStatus
from flask import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from app.services.anamnesis_services import verify_fields_and_values, updating
from app.models.anamnesis_model import Anamnesis


@jwt_required()
def create_anamnesis():

    user = get_jwt_identity()
    data = request.get_json()
    session = current_app.db.session

    invalid_fields, required_fields = verify_fields_and_values(data)
    data["user_id"] = user["id"]
    
    if invalid_fields:
        return {"msg":"Missing fields or the type is wrong","invalid_fields":invalid_fields, "valid_fields":required_fields}, HTTPStatus.BAD_REQUEST

    
    anamnesis = Anamnesis(**data)

    session.add(anamnesis)
    session.commit()

    return '', HTTPStatus.NO_CONTENT


@jwt_required()
def update_anamnesis():
    
    user = get_jwt_identity()
    data = request.get_json()
    session = current_app.db.session

    anamnesis = Anamnesis.query.filter_by(user_id = user["id"]).first()

    updating(data, anamnesis)
    
    session.add(anamnesis)
    session.commit()

    return '', HTTPStatus.NO_CONTENT
   