from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask import current_app, jsonify, request, session
from app.models.surgery_details_model import SurgeryDetails
from app.models.user_model import User
from app.models.user_surgery_model import UserSurgery
from app.services.surgery_services import serializing_surgery, update_surgery, validate_body_surgery, validate_body_surgery_details
from werkzeug.exceptions import BadRequest
from app.models.surgery_model import Surgery
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import DataError

def create_surgery():
    try:
        session = current_app.db.session
        data = request.get_json()
        validate_body_surgery(data)

        surgery = Surgery(**data)

        session.add(surgery)
        session.commit()

        return jsonify(surgery), HTTPStatus.CREATED

    except BadRequest:
        return {"error":"The 'name' field it's required"}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"error":"A surgery with this name already exist"}, HTTPStatus.CONFLICT



@jwt_required()
def create_surgery_user():
    try:
        session = current_app.db.session
        data = request.get_json()
        validate_body_surgery_details(data)
        user_id = get_jwt_identity()["id"]

        surgery = Surgery.query.filter_by(name=data["name"]).first()

        if not surgery:
            surgery = Surgery(name=data["name"])
            session.add(surgery)
            session.commit()

        data.pop("name")

        surgery_detail = SurgeryDetails(**data)
        session.add(surgery_detail)
        session.commit()
        
        user_surgery = UserSurgery(user_id=user_id, surgery_id = surgery.id, surgery_detail_id= surgery_detail.id)
        session.add(user_surgery)
        session.commit()

        surgery = {
            "id":surgery.id,
            "name":surgery.name,
            "description":surgery_detail.description,
            "date":surgery_detail.date
        }
        return jsonify(surgery), HTTPStatus.CREATED

    except (BadRequest, TypeError, KeyError):
        return {"error":"These are required fields  ['name','date', 'description']"}, HTTPStatus.BAD_REQUEST



@jwt_required()
def update_user_surgery(id):
    try:
        session = current_app.db.session
        data = request.get_json()
        user_surgery = UserSurgery.query.filter_by(surgery_id=id).first()
        
        if not user_surgery:
            return {"error":"This surgery doenst exists or dont belong to your user"}, HTTPStatus.NOT_FOUND

        surgery_details = SurgeryDetails.query.filter_by(id=user_surgery.surgery_detail_id).first()
        update_surgery(data, surgery_details)

        session.add(surgery_details)
        session.commit()
        surgery = Surgery.query.filter_by(id= surgery_details.surgery_name.id).first() 


        return jsonify({
            "id":surgery.id,
            "name":surgery.name,
            "description":surgery_details.description,
            "date":surgery_details.date
        }), HTTPStatus.OK
    
    except DataError:
        return {"error":"A surgery with this id was not found"}, HTTPStatus.NOT_FOUND


@jwt_required()
def delete_user_surgery(id):
    try:
        session = current_app.db.session
        user_id = get_jwt_identity()["id"]
        
        user_surgery = UserSurgery.query.filter_by(surgery_id=id).first()

        if user_surgery.user_id != user_id:
            return {"msg":"You cant delete a surgery that its not yours"}, HTTPStatus.NOT_ACCEPTABLE
        surgery_details = SurgeryDetails.query.filter_by(id = user_surgery.surgery_detail_id).first()

        session.delete(user_surgery)
        session.commit()

        session.delete(surgery_details)

        session.commit()
        return '', HTTPStatus.NO_CONTENT

    except DataError:
        return {"error":"A surgery with this id was not found"}, HTTPStatus.NOT_FOUND



@jwt_required()


def get_user_surgerys():
    user_id = get_jwt_identity()["id"]

    user = User.query.filter_by(id=user_id).first()
    user = user.asdict()

    all_surgerys =  serializing_surgery(user)
    return jsonify(all_surgerys)