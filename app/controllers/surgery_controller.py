from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask import current_app, jsonify, request
from app.models.surgery_details_model import SurgeryDetails
from app.models.user_model import User
from app.models.user_surgery_model import UserSurgery
from app.services.surgery_services import validate_body_surgery, validate_body_surgery_details
from werkzeug.exceptions import BadRequest
from app.models.surgery_model import Surgery
from flask_jwt_extended import jwt_required, get_jwt_identity


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

        user = User.query.filter_by(id = user_id).first()
        return jsonify(user), HTTPStatus.CREATED

    except (BadRequest, TypeError, KeyError):
        return {"error":"These are required fields  ['name','date', 'description']"}, HTTPStatus.BAD_REQUEST

